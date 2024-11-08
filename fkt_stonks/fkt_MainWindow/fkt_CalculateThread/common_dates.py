# Extrahiere die Datumswerte für beide Ticker als Sets
def common_dates(ticker_values):
    dates_tic = set(ticker_values[0][0])  # Datumswerte aus dem ersten Ticker
    dates_cal_tic = set(ticker_values[1][0])  # Datumswerte aus dem zweiten Ticker
    
    # Bestimme die gemeinsamen Datumswerte
    common_dates = dates_tic.intersection(dates_cal_tic)
    
    # Filtere die Datums- und Wertelisten in ticker_values basierend auf den gemeinsamen Datumswerten
    filtered_dates_1 = [date for date in ticker_values[0][0] if date in common_dates]
    filtered_values_1 = [value for date, value in zip(ticker_values[0][0], ticker_values[0][1]) if date in common_dates]
    
    filtered_dates_2 = [date for date in ticker_values[1][0] if date in common_dates]
    filtered_values_2 = [value for date, value in zip(ticker_values[1][0], ticker_values[1][1]) if date in common_dates]
    
    # Aktualisiere ticker_values, sodass es nur noch die Arrays mit gemeinsamen Datumswerten und zugehörigen Werten enthält
    return [
        [filtered_dates_1, filtered_values_1],  # Gefilterte Daten und Werte für Ticker 1
        [filtered_dates_2, filtered_values_2]   # Gefilterte Daten und Werte für Ticker 2
    ]