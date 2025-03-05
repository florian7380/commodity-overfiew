from fkt_stonks.fkt_MainWindow.fkt_create_tabs.fkt_PlotTab.fkt_save_data.fkt_update_plot.get_values import get_values
from fkt_stonks.fkt_MainWindow.fkt_create_tabs.fkt_PlotTab.fkt_save_data.fkt_update_plot.fkt_get_comparison.exp_regres import exp_regres
from fkt_stonks.fkt_MainWindow.fkt_create_tabs.fkt_PlotTab.fkt_save_data.fkt_update_plot.fkt_get_comparison.regres_real_abs import regres_real_abs
from fkt_stonks.fkt_MainWindow.fkt_create_tabs.fkt_PlotTab.fkt_save_data.fkt_update_plot.fkt_get_comparison.regres_real_rel import regres_real_rel

import fkt_stonks.fkt_MainWindow.fkt_CalculateThread as fkt

from Lists.TickerList import TickerList

from PyQt5.QtCore import QThread
from datetime import datetime

class CalculateThread(QThread):
    
    def __init__(self):
        super().__init__()
        self._is_running = True
        
    def stop(self):
        print("stop Funktion triggered, CalculateThread stopping")
        self._is_running = False
    
    def run(self):
        # get the last ticker which got calculated at [0] and the last ticker it got calcultaed with at [1]. Both hold another array which has dates at [0] and values at [1]
        last_tickers = fkt.load_tickers()
        
        # Make the second run start from beginning
        first_loop = True
        start_index_tic = 0
        start_index_cal_tic = 0
        if last_tickers != None:
            # get the indexes of the tickers to start the for loops at the fitting point
            start_index_tic = TickerList.index(last_tickers[0]) if last_tickers[0] in TickerList else 0
            start_index_cal_tic = TickerList.index(last_tickers[1]) if last_tickers[1] in TickerList else 0
            start_index_cal_tic += 1
            # start loop again if it is run through. len(TickerList)-2 because the len(List) is one larger then the index and the last ticker doesn't get saved because it doesn't get compared
            if start_index_tic == len(TickerList)-2:
                start_index_tic = 0
            if start_index_cal_tic == len(TickerList)-1:
                start_index_cal_tic = TickerList.index(last_tickers[0])
                start_index_cal_tic += 1
        
        # Durchlaufe TickerList ab den gefundenen Indizes
        for tic in TickerList[start_index_tic:]:
            
            db_values = []  # Array for values which get uplopaded in the DB
            db_values.append(tic)
            
            # Initiate arrays for values
            ticker_values = [None, None]        # values ffrom tickers [0] ticker tic, [1] ticker tic_cal, [0][0] dates from tic, [0][1] values from tic likewise with [1][0] and [1][0]
            exp_ticker_v = [None, None]         # values of exponential regression
            dif_abs = [None, None]              # values of absolut difference between regression and real values
            dif_rel = [None, None]              # relative difference between regression and real values
            exp_param = 0.0                     # der Parametere der exponentiellen Regression b von a*exp^bx
            # get data for tic from database
            ticker_values[0] = get_values(tic)
            
            if ticker_values[0] != [] and len(ticker_values[0]) > 10:
                # Extrahiere Datumswerte und Float-Werte jeweils separat
                ticker_dates_0 = [datetime.strptime(date, '%Y-%m-%d').timestamp() for date, _ in ticker_values[0]]
                ticker_values_0 = [value for _, value in ticker_values[0]]
                
                # Aktualisiere ticker_values mit den getrennten Arrays für leichtere Zugänglichkeit
                ticker_values[0] = [ticker_dates_0, ticker_values_0]
                # exponential regression for tic
                exp_ticker_v[0], exp_param = fkt.exp_regres_param(ticker_values[0][0], ticker_values[0][1])
                db_values.append(exp_param)
                # absolut difference between regression and real values
                dif_abs[0] = regres_real_abs(ticker_values[0][1], exp_ticker_v[0])
                # relative difference between regression and real values
                dif_rel[0] = regres_real_rel(dif_abs[0], exp_ticker_v[0])
                
                day_av = 0.0
                # calculation of the average  relative difference
                for day in dif_rel[0]:
                    day_av += abs(day)
                day_av /= len(dif_rel)
                db_values.append(day_av)    # Aufnahme des Durchschnitts in die Werte für die Datenbank
                
                fkt.upload_single_values(db_values)
                
                # set ticker to one higher then the last one inserted
                if first_loop == False:
                    start_index_cal_tic = TickerList.index(tic)
                    start_index_cal_tic += 1
                # Vergleich des ersten Tickers mit den anderen
                for cal_tic in TickerList[start_index_cal_tic:]:
                    db_values = []
                    db_values.append(tic + "/" + cal_tic)
                    # Stopping when signal is coming
                    if not self._is_running:
                        return
                    ticker_values[1] = get_values(cal_tic)          # get the values from the DB for the secound ticker
                    
                    if ticker_values[1] != [] and len(ticker_values[1]) > 10:           # check for empty or too short arrays
                        
                        # Extrahiere Datumswerte und Float-Werte jeweils separat
                        ticker_dates_1 = [datetime.strptime(date, '%Y-%m-%d').timestamp() for date, _ in ticker_values[1]]
                        ticker_values_1 = [value for _, value in ticker_values[1]]
                        
                        # Aktualisiere ticker_values mit den getrennten Arrays für leichtere Zugänglichkeit
                        ticker_values[1] = [ticker_dates_1, ticker_values_1]
                        
                        # Get first and last dates for both tickers
                        min_date = max(ticker_values[0][0][0], ticker_values[1][0][0])
                        max_date = min(ticker_values[0][0][-1], ticker_values[1][0][-1])
                        
                        # check for overlap in the data
                        if max_date > min_date:
                            # prepare the secound ticker tic_cal
                            exp_ticker_v[1] = exp_regres(ticker_values[1][0], ticker_values[1][1])       # get the exponential regression for the tickers
                            dif_abs[1] = regres_real_abs(ticker_values[1][1], exp_ticker_v[1])                   # get the absolut difference between the exponential regression and the real data
                            dif_rel[1] = regres_real_rel(dif_abs[1], exp_ticker_v[1])                             # get the relative difference between the regression and the real data
                            
                            # Filter each ticker to include only data within the common date range
                            filtered_ticker_values = []
                            for ticker, rel in zip(ticker_values, dif_rel):
                                filtered_ticker_values.append(fkt.filter_ticker_values([ticker[0], rel], min_date, max_date))
                            filtered_ticker_values = fkt.common_dates(filtered_ticker_values)       # filter dates that only exist for one ticker
                            for i, fil_tic_val in enumerate(filtered_ticker_values):
                                filtered_ticker_values[i] = fkt.double_dates(fil_tic_val)
                                
                            # Berechnung der durchschnittlichen Differenz zwischen den relativen Differenzen der Wertpapiere, ohne zeitliche Versetzung
                            comp_zero = fkt.compare_shares(filtered_ticker_values[0][1], filtered_ticker_values[1][1])
                            db_values.append(comp_zero)     # in this array is: day_av, comp_zero
                            
                            n = fkt.previous_year_index(filtered_ticker_values[0][0])
                            comp_max = comp_zero
                            date_max = 0
                            
                            
                            if n == None:
                                n = len(filtered_ticker_values[0][0])
                                for i in range(n):
                                    calc_share = filtered_ticker_values[0][1][i:]
                                    comp_share = filtered_ticker_values[1][1][:(len(filtered_ticker_values[1][1])-i)]
                                    #if i % 5 == 0:
                                        #print(len(calc_share), len(comp_share))
                                    comp_i = fkt.compare_shares(calc_share, comp_share)
                                    if comp_i > comp_max:
                                        comp_max = comp_i
                                        date_max = filtered_ticker_values[0][0][i]-filtered_ticker_values[0][0][0]
                            db_values.append(comp_max)
                            db_values.append(date_max)      # in this array is: day_av, comp_zero, comp_max, date_max
                            
                            fkt.upload_compare_values(db_values)
                            fkt.save_tickers(tic, cal_tic)
                            
                    # Make the loop start from the beginning
                first_loop = False
                print("Upload finished for: ", tic)