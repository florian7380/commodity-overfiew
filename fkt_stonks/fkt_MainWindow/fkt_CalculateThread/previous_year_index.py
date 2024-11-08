from datetime import datetime
from dateutil.relativedelta import relativedelta

def previous_year_index(filtered_dates):
    # Berechne das Ziel-Datum ein Jahr früher
    target_date = datetime.fromtimestamp(filtered_dates[0])
    target_date += relativedelta(years=1)
    target_date = target_date.timestamp()
    
    # Suche nach dem Index des Datums mit gleichem Monat und Tag wie das Ziel-Datum
    for i, date in enumerate(filtered_dates):
        # Überprüfe auf das richtige Datum
        if date >= target_date:
            return i  # Index des gesuchten Datums