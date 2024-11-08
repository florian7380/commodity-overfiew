import sqlite3
from datetime import datetime

def Upload_PolyIO_Data(polygon_data, db_name="PolygonIOStonks.db"):
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
    for result in polygon_data["results"]:
        date = datetime.utcfromtimestamp(result["t"] / 1000).strftime('%Y-%m-%d')  # Convert timestamp to date
        ticker = result["T"]
        close_price = result["c"]
        
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