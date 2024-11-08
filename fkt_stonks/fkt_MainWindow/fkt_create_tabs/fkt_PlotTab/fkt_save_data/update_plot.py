import fkt_stonks.fkt_MainWindow.fkt_create_tabs.fkt_PlotTab.fkt_save_data.fkt_update_plot as fkt

def update_plot(plot_tab):
    """Update the plot with the currently selected data."""
    if plot_tab.share1 or plot_tab.share2:
        # Clear the existing plot
        plot_tab.plot.clear()
        primary_share = None
        dates_primary = []
        values_primary = []
        
        secondary_share = None
        dates_secondary = []
        values_secondary = []
        
        # Get the data for both shares and get values for a comparison
        if plot_tab.share1:
            primary_share = fkt.get_values(plot_tab.share1)
        if plot_tab.share2:
            secondary_share = fkt.get_values(plot_tab.share2)
        
        # Adjust the data to the wanted timeframe and convert dates from string to date format
        if primary_share and (plot_tab.start_date or plot_tab.end_date):
            # cut away not wanted dates with thier values, so only the wanted timeframe is shown
            filtered_primary_share = fkt.cut_time(primary_share, plot_tab.start_date, plot_tab.end_date)
            # Separate the filtered dates and values into two lists
            dates_primary = [date.timestamp() for date, value in filtered_primary_share]
            values_primary = [value for date, value in filtered_primary_share]
        # Same process for secondary share
        if secondary_share and (plot_tab.start_date or plot_tab.end_date):
            filtered_secondary_share = fkt.cut_time(secondary_share, plot_tab.start_date, plot_tab.end_date)
            dates_secondary = [date.timestamp() for date, value in filtered_secondary_share]
            values_secondary = [value for date, value in filtered_secondary_share]
        
        # Plot graphs plot(x values, y values, colour, name)
        if dates_primary and values_primary:
            plot_tab.plot.plot(dates_primary, values_primary, pen='r', name=plot_tab.share1)
        if dates_secondary and values_secondary:
            plot_tab.plot.plot(dates_secondary, values_secondary, pen='b', name=plot_tab.share2)
        if plot_tab.compare:
            # Additional calculations in hte compare function
            fkt.get_comparison(plot_tab, dates_primary, values_primary, dates_secondary, values_secondary)