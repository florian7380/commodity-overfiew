import sqlite3

def delete_double_dates():
    dblist = ["StockDataStonks.db", "AlphaVantageStonks.db", "PolygonIOStonks.db"]
    
    for db in dblist:
        # Connect to SQLite database
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        
        # Fetch the last 20 entries based on the ID (assuming ID is incrementing over time)
        cursor.execute("""
        SELECT * FROM eod_data 
        ORDER BY date DESC, id DESC 
        LIMIT 20
        """)
        
        # Fetch and print the results
        last_20_entries = cursor.fetchall()
        
        print(f"Last 20 entries in {db}:")
        for row in last_20_entries:
            print(row)
        
    """
    dblist = ["StockDataStonks.db", "AlphaVantageStonks.db", "PolygonIOStonks.db"]
    print("Deleting duplicates...")

    for db in dblist:
        # Connect to SQLite database
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        
        # Find duplicate rows (excluding the one with the smallest ID)
        cursor.execute(
        SELECT * FROM eod_data 
        WHERE id NOT IN (
            SELECT MIN(id) 
            FROM eod_data 
            GROUP BY ticker, date
        )
        )
        duplicates = cursor.fetchall()  # Fetch all duplicate entries
        
        if duplicates:
            print(f"Duplicate entries in {db}:")
            for row in duplicates:
                print(row)  # Print deleted rows before deletion
        
            # Delete the duplicates
            cursor.execute(
            DELETE FROM eod_data 
            WHERE id NOT IN (
                SELECT MIN(id) 
                FROM eod_data 
                GROUP BY ticker, date
            )
            )
            print(f"Deleted {len(duplicates)} duplicates from {db}.")
        else:
            print(f"No duplicates found in {db}.")

        # Commit changes and close connection
        conn.commit()
        conn.close()
        """