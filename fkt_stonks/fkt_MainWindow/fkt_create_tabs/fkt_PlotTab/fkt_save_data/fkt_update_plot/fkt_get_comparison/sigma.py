import math

def sigma(time, values, regres, plot_tab, share_one):
    sig = 0.0
    m = len(values)
    n_sig = [-2, -1, 1, 2]
    
    # Compute mean squared error (sigma)
    for value in values:
        sig += value ** 2 / m
    sig = math.sqrt(sig)
    
    r = 0
    g = 0
    b = 0
    
    # Get fitting colors to the shares. If share_one == True sind die values von der ersten Aktie
    if share_one == True:
        # Colour Orange
        r = 255
        g = 165
    else:
        # Colour turkis
        r = 83
        g = 195
        b = 189
    
    # Step 2: Plot each sigma line
    for n in n_sig:
        # Create sigma line by adjusting each value in regres by sig * m
        sigma_line = [reg + sig * n for reg in regres]
        plot_tab.plot.plot(time, sigma_line, name=f"{n} sigma line", pen=(r,g,b))