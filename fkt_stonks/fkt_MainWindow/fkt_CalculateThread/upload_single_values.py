import sqlite3

def upload_single_values(values):
    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect("calc_single_values.db")
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

    # Check if there are already saved tickers
    cursor.execute('SELECT * FROM single_values WHERE ticker = ?', (values[0], ))
    if cursor.fetchone():
        
        # Update the existing record
        cursor.execute('''
                       UPDATE single_values 
                       SET exp_param = ?, day_av = ? 
                       WHERE ticker = ?
                       ''', (values[1], values[2], values[0]))
    else:
        # Insert a new record if none exists
        cursor.execute('''
                       INSERT INTO single_values (ticker, exp_param, day_av) 
                       VALUES (?, ?, ?)
                       ''', (values[0], values[1], values[2]))
    
    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()