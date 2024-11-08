"""
Dises Programm wurde mit Hilfe von ChatGPT geschrieben.
Es werden automatisch Kursdaten verschiedener Wertpapiere herunter geladen und in Datenbanken eingepfflegt, die dann ausgelesen, verglichen und dargestellt werden können.
Benötigt wird ein ein API-Key von AlphaVantage, Polygon IO und StockData. Der frei zugängliche genügt.
"""

from PyQt5.QtWidgets import QApplication
import sys
import fkt_stonks as fkt

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(fkt.dark_stylesheet)
    window = fkt.MainWindow()
    window.show()

    sys.exit(app.exec_())