from datetime import datetime

def convert_timestamps_to_days(timestamps):
    # Convert timestamps to datetime objects
    dates = [datetime.fromtimestamp(ts) for ts in timestamps]
    
    # Set the first date as the reference (day 0)
    first_date = dates[0]
    
    # Calculate days since the first date
    days = [(date - first_date).days for date in dates]
    
    return days