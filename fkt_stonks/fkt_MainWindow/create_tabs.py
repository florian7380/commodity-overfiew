from PyQt5.QtWidgets import QWidget

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
          
    fkt.create_koeff_table(koeff_tab)
    fkt.create_vergl_table(vergl_tab)
    # StockSelector in den Kurs-Reiter hinzufügen
    fkt.PlotTab(kurse_tab)