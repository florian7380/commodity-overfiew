from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QCompleter, QPushButton
from PyQt5.QtCore import Qt, QEvent, pyqtSignal


class StockSelector(QWidget):
    # Signal to emit the selected item
    stock_selected = pyqtSignal(str)

    def __init__(self, stock_list):
        super().__init__()

        # Hauptlayout
        self.main_layout = QVBoxLayout()

        # Horizontales Layout für die obere Zeile mit Entry-Feldern
        self.top_layout = QHBoxLayout()

        # Entry-Feld für Aktienauswahl
        self.entry = QLineEdit()
        self.entry.setPlaceholderText("Aktie auswählen")
        self.top_layout.addWidget(self.entry)
        
        # Delete button
        self.delete_button = QPushButton("x")
        self.top_layout.addWidget(self.delete_button)
        self.delete_button.clicked.connect(self.delete_share)

        # QCompleter mit dem Stock-List-Modell
        self.completer = QCompleter(stock_list)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)  # Nur Liste zeigen, wenn Text eingegeben wird
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)  # Groß/Kleinschreibung ignorieren
        self.entry.setCompleter(self.completer)

        # Hauptlayout hinzufügen
        self.main_layout.addLayout(self.top_layout)
        self.setLayout(self.main_layout)

        # Connect signals for focus and selection
        self.entry.textEdited.connect(self.on_text_edited)
        self.completer.activated.connect(self.on_item_selected)

        # Installiere den Event-Filter für das Entry-Feld
        self.entry.installEventFilter(self)

    def on_text_edited(self, text):
        if text:
            self.completer.complete()  # Zeige die Liste bei Texteingabe
        else:
            self.completer.popup().hide()  # Verstecke die Liste, wenn kein Text vorhanden

    def on_item_selected(self, text):
        # Den ausgewählten Text ins Entry-Feld übernehmen
        self.entry.setText(text)
        # Liste nach Auswahl ausblenden
        self.completer.popup().hide()
        # Emit the selected stock ticker
        self.stock_selected.emit(text)

    def eventFilter(self, obj, event):
        # Wenn das Entry-Feld den Fokus bekommt, Liste anzeigen
        if obj == self.entry and event.type() == QEvent.FocusIn:
            self.completer.complete()  # Liste sofort anzeigen
        return super().eventFilter(obj, event)
    
    def delete_share(self):
        self.entry.setText("")
        self.stock_selected.emit("")