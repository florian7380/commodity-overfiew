import sqlite3

def get_tickers(db_name):
    try:
        # Verbindung zur SQLite-Datenbank herstellen
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        print(db_name)
        
        # Abfrage aller einzigartigen Ticker
        cursor.execute('''SELECT DISTINCT ticker FROM eod_data''')
    
        # Ergebnis abrufen und die Ticker in eine Liste umwandeln
        tickers = [row[0] for row in cursor.fetchall()]
    
        # Verbindung schließen
        conn.close()

        return tickers
    except sqlite3.Error as e:
        print(f"Database error: {e}")