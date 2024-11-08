from fkt_stonks.fkt_MainWindow.fkt_create_tabs.fkt_PlotTab.fkt_save_data.update_plot import update_plot

def save_data(plot_tab, number, value):
    #Save selected ticker, dates, or comparison type.
    if number == 1:
        plot_tab.share1 = value
    elif number == 2:
        plot_tab.share2 = value
    elif number == 3:
        plot_tab.start_date = value
    elif number == 4:
        plot_tab.end_date = value
    elif number == 5:
        plot_tab.compare = value
    
    if plot_tab.share1 or plot_tab.share2:
        update_plot(plot_tab)