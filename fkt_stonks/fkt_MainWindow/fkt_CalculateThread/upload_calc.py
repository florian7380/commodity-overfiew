"""
übergeben werden zwei Ticker, die miteinander verglichen wurden. Für den ersten sind noch weitere Werte übergeben.
Im "values" array ist: day_av, comp_zero, comp_max, date_max
"""

import sqlite3

def upload_calc(tic, cal_tic, values):
    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect("Calculation.db")
    cursor = conn.cursor()
    
    # Erstelle Tabelle, wenn sie nicht existiert
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS calc_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tic TEXT,
        cal_tic TEXT,
        day_av REAL,
        comp_zero REAL,
        comp_max REAL,
        date_max TEXT
    )
    ''')
    
    #Speichern der Werte
    cursor.execute('''
    INSERT INTO calc_results (tic, cal_tic, day_av, comp_zero, comp_max, date_max)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (tic, cal_tic, values[0], values[1], values[2], values[3]))

    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()