from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
import pyqtgraph as pg
import fkt_stonks.fkt_MainWindow.fkt_create_tabs.fkt_PlotTab as fkt

class PlotTab(QWidget):
    def __init__(self, tab):
        super().__init__()
        self.tab = tab
        self.share1 = None
        self.share2 = None
        self.start_date = None
        self.end_date = None
        self.compare = None
        
        # Beispiel Wertpapier-Liste
        self.ticker_list = []
        
        db_list = ["AlphaVantageStonks.db", "PolygonIOStonks.db", "StockDataStonks.db"]
        
        for db in db_list:
            tickers = fkt.get_tickers(db)
            if tickers != None:
                self.ticker_list.extend(tickers)
        
        # Create layout and selectors
        self.main_layout = QVBoxLayout(self)
        self.selector_layout = QHBoxLayout()
        
        # Create two StockSelector widgets
        self.stock_selector_1 = fkt.StockSelector(self.ticker_list)
        self.stock_selector_2 = fkt.StockSelector(self.ticker_list)
        
        #Create DateSelectors for start and end date
        self.date_selector = fkt.DateSelector()
        
        #Create CompareSelector
        self.compare_selector = fkt.CompareSelector()
        
        # Add selectors to layout
        self.selector_layout.addWidget(self.stock_selector_1)
        self.selector_layout.addWidget(self.stock_selector_2)
        self.selector_layout.addWidget(self.date_selector)
        self.selector_layout.addWidget(self.compare_selector)
        self.main_layout.addLayout(self.selector_layout)
        #Creating PyQtGraph widget
        self.plot_widget = pg.GraphicsLayoutWidget()
        self.plot = self.plot_widget.addPlot() # adding Plot
        
        self.main_layout.addWidget(self.plot_widget) # Adding the plotwidget to the layout
        
        # Connect signals
        self.stock_selector_1.stock_selected.connect(lambda ticker: fkt.save_data(self, 1, ticker))
        self.stock_selector_2.stock_selected.connect(lambda ticker: fkt.save_data(self, 2, ticker))
        self.date_selector.start_date_selected.connect(lambda date: fkt.save_data(self, 3, date))
        self.date_selector.end_date_selected.connect(lambda date: fkt.save_data(self, 4, date))
        self.compare_selector.compare_selected.connect(lambda compare: fkt.save_data(self, 5, compare))
        
        # Spacer for the selecotrs
        self.main_layout.addLayout(self.selector_layout)
        
        self.tab.setLayout(self.main_layout)
