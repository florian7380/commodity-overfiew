from PyQt5.QtCore import QThread
import requests
from datetime import date
from dateutil.relativedelta import relativedelta
from datetime import datetime
from Lists import StockDataList
from Lists.TokenList import sd_token
from fkt_stonks.fkt_MainWindow.fkt_StockDataThread import Upload_StockData_Data
import fkt_stonks.fkt_MainWindow.fkt_for_Threads as fkt

class StockdataThread(QThread):
    
    def __init__(self):
        super().__init__()
        self._is_running = True
        
    def stop(self):
        print("stop Funktion triggered")
        self._is_running = False
        
    
    def run(self):
        
        # Load the last saved ticker
        last_ticker = fkt.load_last_ticker("StockData_last_ticker.db")

        # Find the index to resume from
        start_index = StockDataList.index(last_ticker) if last_ticker in StockDataList else 0
        #if all inxes were loaded in the DB , start again.
        if start_index == len(StockDataList)-1:
            start_index = 0
        # Download the data from Stockdata.org
        api_token = sd_token
        for name in StockDataList[start_index:]:
            
            # Stopping when signal is coming
            if not self._is_running:
                return
            
            # Set up date range for last 5 years or to the last date in db
            end_date = date.today() - relativedelta(days=1)
            start_date = fkt.get_latest_date_for_ticker(name)
            if start_date == None:
                start_date = end_date - relativedelta(years=5) # max time to get responses for
            
            if isinstance(start_date, str):
                # Convert start_date to date object
                start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            
            #running as long as the date is accessable from Stockdata
            while start_date < end_date:
                next_date = start_date + relativedelta(days=180)  # Add 6 months - max time frame to get data for
                if next_date > date.today():
                    next_date = date.today() - relativedelta(days=1)
                    
                url = f"https://api.stockdata.org/v1/data/eod?symbols={name}&date_from={start_date}&date_to={next_date}&api_token={api_token}"
                # Update the current date
                start_date = next_date + relativedelta(days=1)
                
                response = requests.get(url)
                # Check for valid response
                if response.status_code == 200:
                    stock_data = response.json()
                    
                    # Check if the response contains valid data
                    if "data" in stock_data and len(stock_data["data"]) > 0:
                        Upload_StockData_Data(stock_data, name)  # Upload data to DB
                        fkt.save_last_ticker(name, "StockData_last_ticker.db")
                        print("Stockdata: ", name)
                    else:
                        print("StockdataThread: ", f"No valid data found for {name} in the API response.")
                        print(url)
                        return
                else:
                    print("StockdataThread: ", f"Error fetching data from Stockdata.org for {name}")
                    print(url)
                    return