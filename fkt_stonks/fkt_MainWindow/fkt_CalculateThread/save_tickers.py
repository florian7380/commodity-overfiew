import sqlite3

# Function to save the last ticker
def save_tickers(ticker, calc_ticker):
    conn = sqlite3.connect("calculate_last_ticker.db")
    cursor = conn.cursor()
    
    # Create a table to store the last uploaded ticker if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS upload_progress (
        id INTEGER PRIMARY KEY,
        ticker TEXT,
        calc_ticker TEXT
    )
    ''')
    
    # Check if there are already saved tickers
    cursor.execute('SELECT * FROM upload_progress WHERE id = 1')
    if cursor.fetchone():
        # Update the existing record
        cursor.execute('UPDATE upload_progress SET ticker = ?, calc_ticker = ? WHERE id = 1', (ticker, calc_ticker))
    else:
        # Insert a new record if none exists
        cursor.execute('INSERT INTO upload_progress (id, ticker, calc_ticker) VALUES (1, ?, ?)', (ticker, calc_ticker))
    
    conn.commit()
    conn.close()