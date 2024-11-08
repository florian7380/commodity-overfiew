import sqlite3
from datetime import datetime

# Funktion zum Einfügen der Daten in die SQLite-Datenbank
def Upload_StockData_Data(stock_data, ticker, db_name="StockDataStonks.db"):
    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Erstelle Tabelle, wenn sie nicht existiert
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS eod_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ticker TEXT,
        date TEXT,
        close REAL,
        UNIQUE(ticker, date)  -- Table-level constraint to enforce uniqueness
    )
    ''')

    # Werte aus dem JSON extrahieren und in die Tabelle einfügen
    for result in stock_data["data"]:
        date = datetime.strptime(result["date"], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d')  # Convert timestamp to date
        close_price = result["close"]
        
        try:
            # Attempt to insert data, skip if ticker and date are already in the table
            cursor.execute('''
            INSERT OR IGNORE INTO eod_data (ticker, date, close)
            VALUES (?, ?, ?)
            ''', (ticker, date, close_price))
        except sqlite3.IntegrityError as e:
            print(f"Duplicate entry skipped for {ticker} on {date}: {e}")
    
    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()