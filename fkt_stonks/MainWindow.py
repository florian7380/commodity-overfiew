from PyQt5.QtWidgets import QMainWindow, QTabWidget
import fkt_stonks.fkt_MainWindow as fkt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #fkt.delete_double_dates()
        # Upload in neuem Thread starten
        self.polygonio_thread = fkt.PolygonIOThread()
        self.alphavantage_thread = fkt.AlphaVantageThread()
        self.stockdata_thread = fkt.StockdataThread()
        self.calculate_thread = fkt.CalculateThread()
        
        # Hauptfenster
        self.setWindowTitle("Aktien- und Wertpapierverwaltung")
        self.setGeometry(100, 100, 1200, 800)

        # Tab-Controller
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        # Reiter erstellen
        fkt.create_tabs(self.tabs)
        
        self.polygonio_thread.start()
        self.alphavantage_thread.start()
        self.stockdata_thread.start()
        self.calculate_thread.start()
        
    def closeEvent(self, event):
        # This method is called when the window is closed
        print("Closing the application...")
        # Set the stop flag to True to stop all running threads
        
        threads = [self.polygonio_thread, self.alphavantage_thread, self.stockdata_thread, self.calculate_thread]
        
        for thread in threads:
            if thread.isRunning():
                thread.stop()
                thread.wait()
                print(thread, " stopped")
        
        # Call the parent class closeEvent to ensure normal closing behavior
        event.accept()