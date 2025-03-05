from PyQt5.QtCore import QThread
import requests
from Lists import AlphaVantageList
from Lists.TokenList import av_token
from fkt_stonks.fkt_MainWindow.fkt_AlphaVantageThread import Upload_AlpVan_Data
from fkt_stonks.fkt_MainWindow.fkt_for_Threads import save_last_ticker, load_last_ticker

class AlphaVantageThread(QThread):
    
    def __init__(self):
        super().__init__()
        self._is_running = True
        
    def stop(self):
        print("stop Funktion triggered")
        self._is_running = False
    
    def run(self):

        # Load the last saved ticker
        last_ticker = load_last_ticker("AlphaVantage_last_ticker.db")

        # Find the index to resume from
        start_index = AlphaVantageList.index(last_ticker) + 1 if last_ticker in AlphaVantageList else 0
        # If all indices were loaded in the DB, start again.
        if start_index == len(AlphaVantageList):
            start_index = 0
            
        # Download the data from AlphaVantage, starting from where we left off
        api_token = av_token
        for name in AlphaVantageList[start_index:]:
            
            # Stop if the thread is no longer running
            if not self._is_running:
                print(self._is_running)
                return
            
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={name}&outputsize=full&apikey={api_token}'
            response = requests.get(url)
            if response.status_code == 200:
                stock_data = response.json()
                
                # Check if the response contains an 'Error Message' or 'Information' key
                if "Time Series (Daily)" in stock_data:
                    Upload_AlpVan_Data(stock_data)  # Process and upload the data
                    # Save the current ticker to resume later
                    print("alpha vantage: ", name)
                    save_last_ticker(name, "AlphaVantage_last_ticker.db")
                elif "Error Message" in stock_data:
                    print("AlphaVantageThread: ", f"Stopping further requests: {stock_data['Error Message']}")
                    print(url)
                    break
                elif "Information" in stock_data:
                    print("AlphaVantageThread: ", f"Stopping further requests: {stock_data['Information']}")
                    print(url)
                    break
                
            else:
                print("AlphaVantageThread: ", f"Error fetching data from AlphaVantage for {name}")
                print(url)