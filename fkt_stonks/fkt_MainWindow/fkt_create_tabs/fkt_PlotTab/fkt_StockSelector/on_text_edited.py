from fkt_stonks.fkt_MainWindow.fkt_create_tabs.fkt_PlotTab.fkt_StockSelector.fkt_on_text_edited.filter_list import filter_list

def on_text_edited(instance, text):
    # Wenn Text im Entry-Feld steht, filtere die Liste
    if text:
        filter_list(instance, text)
        instance.list_widget.show()  # Liste anzeigen
    else:
        instance.list_widget.hide()  # Liste ausblenden, wenn kein Text
        