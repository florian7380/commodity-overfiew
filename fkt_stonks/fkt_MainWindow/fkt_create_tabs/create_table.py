from PyQt5.QtWidgets import QVBoxLayout, QTableWidget, QTableWidgetItem
import fkt_stonks.fkt_MainWindow.fkt_create_tabs.fkt_create_table as fkt

def create_table(tab, columns, nr):
    layout = QVBoxLayout()
    table = QTableWidget()
    
    # Setze die Anzahl der Spalten entsprechend der Anzahl der Spalten (Ticker-Kombinationen)
    table.setColumnCount(len(columns))
    table.setHorizontalHeaderLabels(columns)
    
    # Definiere die Row-Namen basierend auf nr
    if nr == 1:
        row_names = ["exp_param", "day_av"]
    elif nr == 2:
        row_names = ["comp_zero", "comp_max", "dif in days"]

    # Erstellen der Daten als key (Ticker-Paar)
    data = {}
    if nr == 1:
        for ticker in columns:
            single_data = fkt.get_single_data(ticker)
            if single_data != []:
                data[ticker] = list(single_data[0])
            else:
                data[ticker] = single_data
    elif nr == 2:
        for ticker_pair in columns:
            pair_data = fkt.get_compair_data(ticker_pair)
            if pair_data != []:
                data[ticker_pair] = list(pair_data[0])
            else: 
                data[ticker_pair] = pair_data
    
    # Setze die Anzahl der Zeilen basierend auf den Daten (z.B. die Länge der Daten, je nach wie viele Werte du hast)
    rows = len(next(iter(data.values())))  # Anzahl der Zeilen basiert auf der Länge der Daten
    table.setRowCount(rows)

    # Setze die vertikalen Header-Labels
    if row_names and len(row_names) == rows:
        table.setVerticalHeaderLabels(row_names)

    # Füllen der Tabelle mit den entsprechenden Werten aus `data`
    for col_index, column in enumerate(columns):
        values = data.get(column, [])
        for row_index, value in enumerate(values):
            # Runde die ersten beiden Werte auf fünf Nachkommastellen
            if nr == 1 and row_index < 2:
                value = round(value, 5)
            elif nr == 2:
                if row_index < 2:
                    value = round(value, 5)
                elif row_index == 2:
                    # Konvertiere den Timestamp in Tage
                    value = value / 86400
            
            table.setItem(row_index, col_index, QTableWidgetItem(f"{value}"))

    layout.addWidget(table)
    tab.setLayout(layout)