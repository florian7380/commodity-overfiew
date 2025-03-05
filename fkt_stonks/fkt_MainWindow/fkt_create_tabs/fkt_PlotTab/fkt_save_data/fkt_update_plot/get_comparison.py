import fkt_stonks.fkt_MainWindow.fkt_create_tabs.fkt_PlotTab.fkt_save_data.fkt_update_plot.fkt_get_comparison as fkt
import pyqtgraph as pg

def get_comparison(plot_tab, dates_primary, values_primary, dates_secondary, values_secondary):
    values = [None, None]
    regres = [None, None]
    #clear plot if the share calues are taking too much space in the plot
    if plot_tab.compare in ("regres to real abs", "regres to real %", "regres to regres", "rel to rel"):
        plot_tab.plot.clear()
    
    if plot_tab.compare in ("exp regres.","regres to real abs","regres to real %","regres to regres","rel to rel", "1 & 2 Sigma"):
        # Berechnung der exponentiellen Regression
        if dates_primary and values_primary:
            regres[0] = fkt.exp_regres(dates_primary, values_primary)
            values[0] = regres[0]
        if dates_secondary and values_secondary:
            regres[1] = fkt.exp_regres(dates_secondary, values_secondary)
            values[1] = regres[1]
        # Berechnung der Differenz zwischen der Regression und den realen Werten absolut und relativ
        if plot_tab.compare in ("regres to real abs","regres to real %","regres to regres","rel to rel", "1 & 2 Sigma"):
            # Berechnung der absoluten Differenzen
            if dates_primary and values_primary:
                values[0] = fkt.get_dif([values_primary, values[0]])
            if dates_secondary and values_secondary:
                values[1]= fkt.get_dif([values_secondary, values[1]])
            # Berechnung der Standardabweichung
            if plot_tab.compare == "1 & 2 Sigma":
                if dates_primary and values_primary:
                    fkt.sigma(dates_primary, values[0], regres[0], plot_tab, True)
                    values[0] = regres[0]
                if dates_secondary and values_secondary:
                    fkt.sigma(dates_secondary, values[1], regres[1], plot_tab, False)
                    values[1] = regres[1]
            # Berechnung der relativen Differenzen zur Regression
            if plot_tab.compare in ("regres to real %", "rel to rel", "regres to regres") and dates_primary and dates_secondary:
                dates, values, regres = fkt.common_dates([dates_primary, values[0], regres[0]],[dates_secondary, values[1], regres[1]])
                dates_primary = dates[0]
                dates_secondary = dates[1]
                if plot_tab.compare in ("regres to real %", "rel to rel"):
                    # Da der relative Wert deutlich kleiner ist wird eine neue y-Achse verwendet
                    if dates_primary and values_primary:
                        values[0] = fkt.regres_real_rel(values[0], regres[0])
                    if dates_secondary and values_secondary:
                        values[1] = fkt.regres_real_rel(values[1], regres[1])
                    # Berechnung der Differenz zwischen den relativen Differenzen zur Regression
                    if plot_tab.compare == "rel to rel":
                        if dates_primary and values_primary and dates_secondary and values_secondary:
                            values.append(fkt.get_dif(values))
                if plot_tab.compare == "regres to regres" and dates_primary and values_primary and dates_secondary and values_secondary:
                    values.append(fkt.get_dif(regres))
                    values[0] = regres[0]
                    values[1] = regres[1]
    if plot_tab.compare in  ("200 Day average", "200 Day av + sigma"):
        if dates_primary and values_primary:
            values[0] = fkt.twoh_av(dates_primary, values_primary)
            dates_primary = dates_primary[135:]
        if dates_secondary and values_secondary:
            values[1] = fkt.twoh_av(dates_secondary, values_secondary)
            dates_secondary = dates_secondary[135:]
        if plot_tab.compare == "200 Day av + sigma":
            if dates_primary and values_primary:
                day_av_dif = fkt.get_dif([values_primary[136:],values[0]])
                fkt.sigma(dates_primary, day_av_dif, values[0], plot_tab, True)
            if dates_secondary and values_secondary:
                day_av_dif = fkt.get_dif([values_secondary[136:],values[1]])
                fkt.sigma(dates_secondary, day_av_dif, values[1], plot_tab, False)
        
    # Getting the dates for the comaprison
    dates_compare = []
    if plot_tab.compare in ("rel to rel", "regres to regres"):
        for date in dates_primary:
            if date in dates_secondary:
                dates_compare.append(date)
    # Plot the values from the comparison
    if values[0]:
        plot_tab.plot.plot(dates_primary ,values[0], name=(plot_tab.compare, "share 1"), pen ='y')
    if values[1]:
        plot_tab.plot.plot(dates_secondary,values[1], name=(plot_tab.compare, "share 2"), pen ='g')
    if len(values) == 3:
        if values[2]:
            plot_tab.plot.plot(dates_compare, values[2], name=plot_tab.compare, pen ='white')
    # Add a horizontal white line at y=0 if needed
    if plot_tab.compare in ("rel to rel", "regres to real %", "regres to real abs", "rel to rel"):
        line = pg.InfiniteLine(pos=0, angle=0, pen=pg.mkPen('white', width=1))
        plot_tab.plot.addItem(line)