import sqlite3

# Function to load the last saved ticker
def load_last_ticker(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS upload_progress (
        id INTEGER PRIMARY KEY,
        ticker TEXT
    )
    ''')

    # Check if there's already a last ticker saved
    cursor.execute('SELECT ticker FROM upload_progress WHERE id = 1')
    row = cursor.fetchone()

    conn.close()
    
    return row[0] if row else None