from datetime import datetime, timedelta

def cut_time(share, start, end, compare):
    filtered_results = None
    # Parse start and end dates
    start_date = datetime(start.year(), start.month(), start.day()) if start else None
    end_date = datetime(end.year(), end.month(), end.day()) if end else None
    
    if compare in  ("200 Day average", "200 Day av + sigma") and start_date is not None:
        start_date -= timedelta(days=200)
    # Convert date strings to datetime objects and filter by the start and end date
    filtered_results = [
        (datetime.strptime(date_str, '%Y-%m-%d'), value) 
        for date_str, value in share
        if (not start_date or datetime.strptime(date_str, '%Y-%m-%d') >= start_date) and
           (not end_date or datetime.strptime(date_str, '%Y-%m-%d') <= end_date)
    ]
    return filtered_results