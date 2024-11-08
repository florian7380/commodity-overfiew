from PyQt5.QtWidgets import QWidget

from Lists.TickerList import TickerList

# Importiere die benötigten Funktionen direkt
import fkt_stonks.fkt_MainWindow.fkt_create_tabs as fkt

def create_tabs(tab_widget):
    # Reiter: Depot, Kurse, Koeffizienten, Fundamentaldaten, Upload
    kurse_tab = QWidget()
    koeff_tab = QWidget()
    vergl_tab = QWidget()
    
    # Tabs hinzufügen
    tab_widget.addTab(kurse_tab, "Kurse")
    tab_widget.addTab(koeff_tab, "Koeffizienten")
    tab_widget.addTab(vergl_tab, "Vergleich")
    # Tabellen in Tabs hinzufügen
    # Spalten für Koeffizienten kreieren
    columns = []
    for i, ticker in enumerate(TickerList):
        if i+1 < len(TickerList):
            for comparer in TickerList[i+ 1:]:
                columns.append(ticker + "/" + comparer)
            
    fkt.create_table(koeff_tab, TickerList, 1)
    fkt.create_table(vergl_tab, columns, 2)
    # StockSelector in den Kurs-Reiter hinzufügen
    fkt.PlotTab(kurse_tab)