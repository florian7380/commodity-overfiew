import numpy as np
from scipy.optimize import curve_fit
from fkt_stonks.fkt_MainWindow.fkt_create_tabs.fkt_PlotTab.fkt_save_data.fkt_update_plot.fkt_get_comparison.fkt_exp_regres.convert_timestamps_to_days import convert_timestamps_to_days

def exp_regres_param(dates, values):
    days = convert_timestamps_to_days(dates)
    
    # Definition der exponentiellen Funktion: f(x) = a * e^(b * x)
    def exp_func(x, a, b):
        return a * np.exp(b * x)
    
    # Initial guess
    initial_guess = [np.mean(values), 0.001]
    
    # Filter NaN/Inf Werte heraus
    days = np.array(days)
    values = np.array(values)
    mask = np.isfinite(days) & np.isfinite(values)
    days = days[mask]
    values = values[mask]

    # Curve fitting mit höherem maxfev-Wert
    params, covariance = curve_fit(exp_func, days, values, p0=initial_guess, maxfev=2000)
    
    a, b = params
    fitted_values = [exp_func(day, a, b) for day in days]
    
    return fitted_values, b