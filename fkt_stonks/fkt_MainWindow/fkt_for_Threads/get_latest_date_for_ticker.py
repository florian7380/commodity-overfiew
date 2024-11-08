import sqlite3
import os

# Funktion zum Abrufen des Datums, das am nächsten zur Gegenwart liegt
def get_latest_date_for_ticker(ticker, db_name="StockDataStonks.db"):
    # Überprüfen, ob die Datenbankdatei existiert
    if not os.path.exists(db_name):
        return None  # Rückgabe von None, wenn die Datenbank nicht existiert
    
    try:
        # Verbindung zur SQLite-Datenbank herstellen
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # SQL-Abfrage, um das späteste Datum für das angegebene Ticker zu finden
        cursor.execute('''
        SELECT MAX(date) 
        FROM eod_data 
        WHERE ticker = ?
        ''', (ticker,))

        # Datum abrufen
        result = cursor.fetchone()
        conn.close()

        if result and result[0]:
            return result[0]  # Rückgabe des Datums als String (YYYY-MM-DD)
        else:
            return None  # Falls kein Eintrag gefunden wurde
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None