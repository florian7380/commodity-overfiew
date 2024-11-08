import fkt_stonks.fkt_MainWindow.fkt_create_tabs.fkt_PlotTab.fkt_save_data.fkt_update_plot.fkt_get_comparison as fkt

def get_comparison(plot_tab, dates_primary, values_primary, dates_secondary, values_secondary):
    values = [None, None, None, None]
    reg_ra = [None, None]
    regres = [None, None]
    two_y_axis = False

    if plot_tab.compare in ("exp regres.","regres to real abs","regres to real %","regres to regres","rel_to_rel", "1 & 2 Sigma"):
        # Berechnung der exponentiellen Regression
        if dates_primary and values_primary:
            regres[0] = fkt.exp_regres(dates_primary, values_primary)
            values[0] = regres[0]
        if dates_secondary and values_secondary:
            regres[1] = fkt.exp_regres(dates_secondary, values_secondary)
            values[1] = regres[1]
        # Berechnung der Differenz zwischen der Regression und den Reralen Werten absolut und relativ
        if plot_tab.compare in ("regres to real abs","regres to real %","regres to regres","rel_to_rel", "1 & 2 Sigma"):
            # Berechnung der absoluten Differenzen
            if dates_primary and values_primary:
                values[0] = fkt.regres_real_abs(values_primary, values[0])
            if dates_secondary and values_secondary:
                values[1]= fkt.regres_real_abs(values_secondary, values[1])
            # Berechnung der relativen Differenzen zur Regression
            if plot_tab.compare == "1 & 2 Sigma":
                if dates_primary and values_primary:
                    fkt.sigma(dates_primary, values[0], regres[0], plot_tab, True)
                    values[0] = regres[0]
                if dates_secondary and values_secondary:
                    fkt.sigma(dates_secondary, values[1], regres[1], plot_tab, False)
                    values[1] = regres[1]
            if plot_tab.compare == "regres to real %" and values_primary and values_secondary:
                # Da der relative Wert deutlich kleiner ist wird eine neue y-Achse verwendet
                two_y_axis = True
                if dates_primary and values_primary:
                    values[0] = fkt.regres_real_rel(values_primary, values[0])
                if dates_secondary and values_secondary:
                    values[1] = fkt.regres_real_rel(values_secondary, values[1])
                if plot_tab.compare == "regres_to_regres" and dates_primary and values_primary and dates_secondary and values_secondary:
                    values[2] = fkt.regres_regres()
                if plot_tab.compare == "rel to rel":
                    if dates_primary and values_primary and dates_secondary and values_secondary:
                        values[2] = fkt.rel_rel()
    if plot_tab.compare == "200 day average":
        if dates_primary and values_primary and dates_secondary and values_secondary:
            values[0] = fkt.twoh_av(dates_primary, values_primary)
        if dates_secondary and values_secondary:
            values[1] = fkt.twoh_av(dates_secondary, values_secondary)
            
    
    # Plot the values from the comparison
    if values[0]:
        plot_tab.plot.plot(dates_primary ,values[0], name="exp. regres. share 1", pen ='y')
    if values[1]:
        plot_tab.plot.plot(dates_secondary,values[1], name="exp. regres. share 2", pen ='g')