# Get two array with the lists [dates, values, regression values]
def common_dates(values_one, values_two):
    dates_one = set(values_one[0])  # Datumswerte aus dem ersten Ticker
    dates_two = set(values_two[0])  # Datumswerte aus dem zweiten Ticker
    
    # Bestimme die gemeinsamen Datumswerte
    common_dates = dates_one.intersection(dates_two)
    
    # Filtere die Datums- und Wertelisten in ticker_values basierend auf den gemeinsamen Datumswerten
    filtered_dates_one = [date for date in values_one[0] if date in common_dates]
    filtered_values_one = [value for date, value in zip(values_one[0], values_one[1]) if date in common_dates]
    filtered_regres_one = [regres for date, regres in zip(values_one[0], values_one[2]) if date in common_dates]
    
    filtered_dates_two = [date for date in values_two[0] if date in common_dates]
    filtered_values_two = [value for date, value in zip(values_two[0], values_two[1]) if date in common_dates]
    filtered_regres_two = [regres for date, regres in zip(values_two[0], values_two[2]) if date in common_dates]
    
    # Aktualisiere ticker_values, sodass es nur noch die Arrays mit gemeinsamen Datumswerten und zugehörigen Werten enthält
    return [filtered_dates_one, filtered_dates_two], [filtered_values_one, filtered_values_two], [filtered_regres_one, filtered_regres_two]