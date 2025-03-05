from PyQt5.QtWidgets import QTableWidgetItem
import fkt_stonks.fkt_MainWindow.fkt_create_tabs.fkt_create_vergl_table.fkt_create_table as fkt

from Lists.TickerList import TickerList

def create_table(ticker, table):
    # Spalten für Koeffizienten kreieren
    rows = []
    ticker_index = TickerList.index(ticker)
    for i, tic in enumerate(TickerList):
        if i < ticker_index:
            rows.append(tic + "/" + ticker)
        if i > ticker_index:
            rows.append(ticker + "/" + tic)
            
    # Definiere die Column-Namen basierend auf nr
    column_names = ["comp_zero", "comp_max", "dif in days"]
    
    # Setze die Anzahl der Spalten entsprechend der Anzahl der Spalten
    table.setColumnCount(len(column_names))
    table.setHorizontalHeaderLabels(column_names)
    
    # getting the data as dictionair
    data = fkt.get_compair_data(rows)
    
    # Setze die Anzahl der Zeilen basierend auf den Daten
    table.setRowCount(len(rows))

    # Setze die vertikalen Header-Labels
    table.setVerticalHeaderLabels(rows)

    # Füllen der Tabelle mit den entsprechenden Werten aus `data`
    for row_index, row in enumerate(rows):
        values = data.get(row, [])
        for col_index, value in enumerate(values):
            # Runde die ersten beiden Werte auf fünf Nachkommastellen
            if col_index < 2:
                value = round(value, 5)
            elif col_index == 2:
                # Konvertiere den Timestamp in Tage
                value = round(value / 86400, 0)
            table.setItem(row_index, col_index, QTableWidgetItem(f"{value}"))