def double_dates(values):
    # Erstelle eine Liste von (Datum, Wert)-Paaren
    date_value_pairs = list(zip(values[0], values[1]))
    
    # Verwende ein Dictionary, um doppelte Paare zu entfernen, da Keys einzigartig sind
    unique_date_value_dict = {date: value for date, value in date_value_pairs}
    unique_dates = list(unique_date_value_dict.keys())
    unique_values = list(unique_date_value_dict.values())
    
    # Aktualisiere ticker_values mit den eindeutigen Datums- und Wertearrays
    return [unique_dates, unique_values]