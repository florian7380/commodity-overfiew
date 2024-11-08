
def filter_list(self, text):
    for index in range(self.list_widget.count()):
        item = self.list_widget.item(index)
        item.setHidden(text.lower() not in item.text().lower())  # Nur passende Einträge anzeigen