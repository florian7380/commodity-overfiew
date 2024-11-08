import sqlite3

# Funktion zum Einfügen der Daten in die SQLite-Datenbank
def Upload_AlpVan_Data(alpha_vantage_data, db_name="AlphaVantageStonks.db"):
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
    
    # Werte aus dem JSON extrahieren und nur neue Daten in die Tabelle einfügen
    ticker = alpha_vantage_data["Meta Data"]["2. Symbol"]
    
    for date, result in alpha_vantage_data["Time Series (Daily)"].items():
        close_price = result["4. close"]
        
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