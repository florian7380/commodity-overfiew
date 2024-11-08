import sqlite3

def get_compair_data(ticker_pair):
    #Find the DB the ticker is in
    db = "calc_compare_values.db"
    
    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    
    # Erstelle Tabelle, wenn sie nicht existiert
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS compare_values (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tickers TEXT,
        comp_zero REAL,
        comp_max REAL,
        date_max REAL
    )
    ''')
    
    query = f'SELECT comp_zero, comp_max, date_max FROM compare_values WHERE tickers = ?'

    # Abfrage aller einzigartigen Ticker
    cursor.execute(query, (ticker_pair,))

    # Ergebnis abrufen und die Ticker in eine Liste umwandeln
    results = cursor.fetchall()

    # Verbindung schließen
    conn.close()

    return results