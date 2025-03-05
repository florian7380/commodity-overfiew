from PyQt5.QtWidgets import QVBoxLayout, QTableWidget
import fkt_stonks.fkt_MainWindow.fkt_create_tabs.fkt_create_vergl_table as fkt
from fkt_stonks.fkt_MainWindow.fkt_create_tabs.fkt_PlotTab.StockSelector import StockSelector
from Lists.TickerList import TickerList

def create_vergl_table(tab):
    layout = QVBoxLayout()
    table = QTableWidget()
    
    # Einstellung für den Header, um eine Aktion auszuführen, wenn geklickt wird
    header = table.horizontalHeader()
    header.sectionClicked.connect(lambda index: fkt.sort_table_by_column(table, index))

    # Getting a stock and displaying the data from the compared stock
    stock_selector = StockSelector(TickerList)
    stock_selector.stock_selected.connect(lambda ticker: fkt.create_table(ticker, table))
            
    layout.addWidget(stock_selector)
    layout.addWidget(table)
    tab.setLayout(layout)