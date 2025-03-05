import sqlite3

def get_compair_data(rows):
    # Create the data dictionary
    data = {}

    # Define database path
    db = "calc_compare_values.db"

    # Use a context manager for the database connection
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()

        # Create the table if it doesn't exist (if needed)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS compare_values (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tickers TEXT,
            comp_zero REAL,
            comp_max REAL,
            date_max REAL
        )
        ''')

        # Use a single query to fetch all data at once
        query = f"SELECT tickers, comp_zero, comp_max, date_max FROM compare_values WHERE tickers IN ({','.join(['?'] * len(rows))})"
        cursor.execute(query, rows)
        all_results = cursor.fetchall()

        # Populate the `data` dictionary with results
        for result in all_results:
            tickers, comp_zero, comp_max, date_max = result
            data[tickers] = [comp_zero, comp_max, date_max]

        # Handle missing ticker pairs
        for ticker_pair in rows:
            if ticker_pair not in data:
                data[ticker_pair] = []

    return data