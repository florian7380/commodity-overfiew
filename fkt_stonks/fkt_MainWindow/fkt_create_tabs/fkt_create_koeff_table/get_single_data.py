import sqlite3

def get_single_data(ticker_list):
    
    # Create the data dictionary
    data = {}

    # Define database path
    db = "calc_single_values.db"

    # Use a context manager for the database connection
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()

        # Create the table if it doesn't exist (if needed)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS single_values (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT,
            exp_param REAL,
            day_av REAL
        )
        ''')

        # Use a single query to fetch all data at once
        query = f"SELECT ticker, exp_param, day_av FROM single_values WHERE ticker IN ({','.join(['?'] * len(ticker_list))})"
        cursor.execute(query, ticker_list)
        all_results = cursor.fetchall()

        # Populate the `data` dictionary with results
        for result in all_results:
            ticker, exp_param, day_av = result
            data[ticker] = [exp_param, day_av]

        # Handle missing ticker pairs
        for ticker_pair in ticker_list:
            if ticker_pair not in data:
                data[ticker_pair] = []

    return data