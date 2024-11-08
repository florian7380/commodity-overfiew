from PyQt5.QtCore import QThread
from  time import sleep
import requests
from dateutil.relativedelta import relativedelta
from datetime import date
import fkt_stonks.fkt_MainWindow.fkt_PolygonIOThread as fkt

class PolygonIOThread(QThread):
    def __init__(self):
        super().__init__()
        self._is_running = True
        
    def stop(self):
        print("stop Funktion triggered")
        self._is_running = False
    
    def run(self):
        api_token = ""
        day = date.today() - relativedelta(days=1)
        recieved_data = True
        existing_dates = fkt.get_existing_dates()

        while recieved_data:
            get_data = True

            # Check if the date is already in the database
            if existing_dates[1] != None and existing_dates[0] != None:
                if existing_dates[1] >= day >= existing_dates[0]:
                    get_data = False
            
            if get_data:
                url = f'https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/{day}?adjusted=true&apiKey={api_token}'
                response = requests.get(url)
                
                if response.status_code == 200:
                    stock_data = response.json()

                    # Check if the response contains a 'NOT_AUTHORIZED' or similar status
                    if stock_data.get("status") != "OK":
                        print("PolygonIOThread: ", f"Stopping further requests: {stock_data['message']}")
                        print(url)
                        recieved_data = False
                        return
                    elif stock_data.get("resultsCount") == 0:
                        print("PolyIO no results")
                        print(url)
                    else:
                        fkt.Upload_PolyIO_Data(stock_data)  # Upload the data to the database
                else:
                    print("PolygonIOThread: ", f"Error fetching data for {day}: {response.status_code}")
                    print(url)
                    recieved_data = False  # Stop the loop if we get an error response
                
                # To comply with API rate limits
                for f in range(12):  # Break down the sleep into 1-second intervals
                    if not self._is_running:
                        return
                    sleep(1)
                
            day -= relativedelta(days=1)  # Move to the previous day