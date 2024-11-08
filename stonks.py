"""
Dieses Programm wurde mit Hilfe von ChatGPT geschrieben.
Es werden automatisch Kursdaten verschiedener Wertpapiere heruntergeladen und in Datenbanken eingepflegt, die dann ausgelesen, verglichen und dargestellt werden können.
Benötigt wird ein API-Key von AlphaVantage, Polygon IO und StockData. Der frei zugängliche genügt. Die entsprechende API-Keys müssen in den entsprechenden Threads eingefügt werden.
Die Liste der dargestellten Daten ist unter List.TickerList und stark gekürzt, da der Vergleich schnell viel Leistung fordert.
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
