import fkt_stonks.fkt_MainWindow.fkt_create_tabs.fkt_PlotTab.fkt_save_data.fkt_update_plot as fkt
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate
import pyqtgraph as pg

def update_plot(plot_tab):
    """Update the plot with the currently selected data."""
    if plot_tab.start_date == QDate() or plot_tab.end_date == QDate() or plot_tab.start_date < plot_tab.end_date:
    
        # Clear the existing plot
        plot_tab.plot.clear()
        
        primary_share = None
        dates_primary = []
        values_primary = []
        
        secondary_share = None
        dates_secondary = []
        values_secondary = []
        
        # Get the data for both shares and get values for a comparison
        if plot_tab.share1 != "":
            primary_share = fkt.get_values(plot_tab.share1)
        if plot_tab.share2 != "":
            secondary_share = fkt.get_values(plot_tab.share2)
        
        # Adjust the data to the wanted timeframe and convert dates from string to date format
        if primary_share:
            # cut away not wanted dates with thier values, so only the wanted timeframe is shown
            filtered_primary_share = fkt.cut_time(primary_share, plot_tab.start_date, plot_tab.end_date, plot_tab.compare)
            # Separate the filtered dates and values into two lists
            dates_primary = [date.timestamp() for date, value in filtered_primary_share]
            values_primary = [value for date, value in filtered_primary_share]
        
        # Same process for secondary share
        if secondary_share:
            filtered_secondary_share = fkt.cut_time(secondary_share, plot_tab.start_date, plot_tab.end_date, plot_tab.compare)
            dates_secondary = [date.timestamp() for date, value in filtered_secondary_share]
            values_secondary = [value for date, value in filtered_secondary_share]
        
        # Plot graphs plot(x values, y values, colour, name)
        if dates_primary and values_primary:
            if plot_tab.compare in ("200 Day average", "200 Day av + sigma"):
                plot_tab.plot.plot(dates_primary[136:], values_primary[136:], pen='r', name=plot_tab.share1)
            else:
                plot_tab.plot.plot(dates_primary, values_primary, pen='r', name=plot_tab.share1)
        if dates_secondary and values_secondary:
            if plot_tab.compare in ("200 Day average", "200 Day av + sigma"):
                plot_tab.plot.plot(dates_secondary[136:], values_secondary[136:], pen='light blue', name=plot_tab.share2)
            else:
                plot_tab.plot.plot(dates_secondary, values_secondary, pen='light blue', name=plot_tab.share2)
        if plot_tab.compare:
            # Additional calculations in hte compare function
            fkt.get_comparison(plot_tab, dates_primary, values_primary, dates_secondary, values_secondary)
        
        # Setting up the DateAxisItem for date formatting
        axis = pg.graphicsItems.DateAxisItem.DateAxisItem(orientation='bottom')
        plot_tab.plot.setAxisItems({'bottom': axis})
        
        plot_tab.plot.setLabel('bottom', "Datum")
        plot_tab.plot.setLabel('left', "Wert in USD")
        
    else:
        QMessageBox.warning(plot_tab, "Ungültiges Datum", "Startdatum muss vor dem Enddatum liegen!")