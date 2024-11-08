
def on_item_clicked(instance, item):
    # Den Text des angeklickten Eintrags ins Entry-Feld uebernehmen
    instance.entry.setText(item.text())
    instance.list_widget.hide()  # Liste wieder ausblenden
