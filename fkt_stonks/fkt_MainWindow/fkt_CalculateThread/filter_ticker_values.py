
def filter_ticker_values(ticker, min_date, max_date):
    filtered_dates = []
    filtered_prices = []
    # get the dates between given max and min date
    for i, date in enumerate(ticker[0]):
        if min_date <= date <= max_date:
            filtered_dates.append(date)
            filtered_prices.append(ticker[1][i])
    return[filtered_dates, filtered_prices]