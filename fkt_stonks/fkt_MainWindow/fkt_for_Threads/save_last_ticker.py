import sqlite3

# Function to save the last ticker
def save_last_ticker(ticker, db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Create a table to store the last uploaded ticker if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS upload_progress (
        id INTEGER PRIMARY KEY,
        ticker TEXT
    )
    ''')
    
    # Check if there are already a last ticker saved
    cursor.execute('SELECT * FROM upload_progress WHERE id = 1')
    if cursor.fetchone():
        # Update the existing record
        cursor.execute('UPDATE upload_progress SET ticker = ? WHERE id = 1', (ticker,))
    else:
        # Insert a new record if none exists
        cursor.execute('INSERT INTO upload_progress (id, ticker) VALUES (1, ?)', (ticker,))
    
    conn.commit()
    conn.close()