import Lists
import sqlite3

def get_values(ticker):
    #Find the DB the ticker is in
    db = None
    if ticker in Lists.AlphaVantageList:
        db = "AlphaVantageStonks.db"
    elif ticker in Lists.PolygonIOList:
        db = "PolygonIOStonks.db"
    elif ticker in Lists.StockDataList:
        db = "StockDataStonks.db"
    else:
        print("Ticker not in any DB")
    
    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS eod_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ticker TEXT,
        date TEXT,
        close REAL,
        UNIQUE(ticker, date)  -- Table-level constraint to enforce uniqueness
    )
    ''')
    
    query = f'SELECT date, close FROM eod_data WHERE ticker = ? ORDER BY date ASC'

    # Abfrage aller einzigartigen Ticker
    cursor.execute(query, (ticker,))

    # Ergebnis abrufen und die Ticker in eine Liste umwandeln
    results = cursor.fetchall()

    # Verbindung schließen
    conn.close()

    return results