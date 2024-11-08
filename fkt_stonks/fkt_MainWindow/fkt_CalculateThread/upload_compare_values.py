import sqlite3

def upload_compare_values(values):
    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect("calc_compare_values.db")
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

    # Check if there are already saved tickers
    cursor.execute('SELECT * FROM compare_values WHERE tickers = ?', (values[0], ))
    if cursor.fetchone():
        # Update the existing record
        cursor.execute('''
                       UPDATE compare_values 
                       SET comp_zero = ?, comp_max = ?, date_max = ?
                       WHERE tickers = ?
                       ''', (values[1], values[2], values[3], values[0]))
    else:
        # Insert a new record if none exists
        cursor.execute('''
                       INSERT INTO compare_values (tickers, comp_zero, comp_max, date_max) 
                       VALUES (?, ?, ?, ?)
                       ''', (values[0], values[1], values[2], values[3]))
    
    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()