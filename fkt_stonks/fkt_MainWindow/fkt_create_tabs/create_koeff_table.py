from PyQt5.QtWidgets import QVBoxLayout, QTableWidget, QTableWidgetItem
import fkt_stonks.fkt_MainWindow.fkt_create_tabs.fkt_create_koeff_table as fkt
import fkt_stonks.fkt_MainWindow.fkt_create_tabs.fkt_create_vergl_table as ext
from Lists.TickerList import TickerList

def create_koeff_table(tab):
    layout = QVBoxLayout()
    table = QTableWidget()
    
    table.setRowCount(len(TickerList))
    table.setVerticalHeaderLabels(TickerList)
    
    # Einstellung für den Header, um eine Aktion auszuführen, wenn geklickt wird
    header = table.horizontalHeader()
    header.sectionClicked.connect(lambda index: ext.sort_table_by_column(table, index))
    
    # Erstellen der Daten als key (Ticker-Paar)
    data = fkt.get_single_data(TickerList)
            
    # Setze die Anzahl der Zeilen basierend auf den Daten (z.B. die Länge der Daten, je nach wie viele Werte du hast)
    columns = len(next(iter(data.values())))  # Anzahl der Zeilen basiert auf der Länge der Daten
    table.setColumnCount(columns)
    
    # set vertical header labels
    col_names = ["exp_param", "day_av"]
    table.setHorizontalHeaderLabels(col_names)


    # fill the table with the values from `data`
    for row_index, row in enumerate(TickerList):
        values = data.get(row, [])
        for col_index, value in enumerate(values):
            value = round(value, 5)
            table.setItem(col_index, row_index, QTableWidgetItem(f"{value}"))
            
    layout.addWidget(table)
    tab.setLayout(layout)