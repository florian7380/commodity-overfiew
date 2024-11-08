import sqlite3

def get_single_data(ticker):
    #Find the DB the ticker is in
    db = "calc_single_values.db"
    
    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    
    # Erstelle Tabelle, wenn sie nicht existiert
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS single_values (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ticker TEXT,
        exp_param REAL,
        day_av REAL
    )
    ''')
    
    query = f'SELECT exp_param, day_av FROM single_values WHERE ticker = ?'

    # Abfrage aller einzigartigen Ticker
    cursor.execute(query, (ticker,))

    # Ergebnis abrufen und die Ticker in eine Liste umwandeln
    results = cursor.fetchall()

    # Verbindung schließen
    conn.close()

    return results