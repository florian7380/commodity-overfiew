import os
import sqlite3
from datetime import datetime


def get_existing_dates(db_name="PolygonIOStonks.db"):
    # Check if the database exists
    db_exists = os.path.exists(db_name)
    
    if db_exists:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        # Select the minimum (oldest) and maximum (most recent) dates
        cursor.execute('''
        SELECT MIN(date), MAX(date) FROM eod_data
        ''')
        
        # Fetch the result (oldest and most recent dates)
        result = cursor.fetchone()
        
        # Close the database connection
        conn.close()
        
        # Convert string dates to datetime.date objects
        min_date = datetime.strptime(result[0], '%Y-%m-%d').date() if result[0] else None
        max_date = datetime.strptime(result[1], '%Y-%m-%d').date() if result[1] else None
        
        # Return the oldest and most recent dates
        return (min_date, max_date)
    
    else:
        # If there is no DB, return None for both dates
        return (None, None)