from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QDateEdit, QPushButton
from PyQt5.QtCore import pyqtSignal, QDate

class DateSelector(QWidget):
    # Define signals for start and end date changes
    start_date_selected = pyqtSignal(QDate)
    end_date_selected = pyqtSignal(QDate)

    def __init__(self):
        super().__init__()

        # Hauptlayout
        self.main_layout = QVBoxLayout()

        # Horizontales Layout für die obere Zeile mit Entry-Feldern und Datumseingaben
        self.top_layout = QHBoxLayout()

        # start date label
        self.start_date = QDateEdit()
        self.start_date.setCalendarPopup(True)
        self.start_date.setDisplayFormat("dd.MM.yyyy")
        self.top_layout.addWidget(QLabel("Startdatum:"))
        self.top_layout.addWidget(self.start_date)
        
        # Delete button
        self.start_date_delete_button = QPushButton("x")
        self.top_layout.addWidget(self.start_date_delete_button)
        self.start_date_delete_button.clicked.connect(self.delete_start_date)
        
        # End date label
        self.end_date = QDateEdit()
        self.end_date.setCalendarPopup(True)
        self.end_date.setDisplayFormat("dd.MM.yyyy")
        self.top_layout.addWidget(QLabel("Enddatum:"))
        self.top_layout.addWidget(self.end_date)
        
        # Delete button
        self.end_date_delete_button = QPushButton("x")
        self.top_layout.addWidget(self.end_date_delete_button)
        self.end_date_delete_button.clicked.connect(self.delete_end_date)

        # Connect date changes to emit signals
        self.start_date.dateChanged.connect(self.on_start_date_changed)
        self.end_date.dateChanged.connect(self.on_end_date_changed)

        # Layout zusammenstellen
        self.main_layout.addLayout(self.top_layout)
        self.setLayout(self.main_layout)

    # Emit signal when start date is changed
    def on_start_date_changed(self, date):
        self.start_date_selected.emit(date)

    # Emit signal when end date is changed
    def on_end_date_changed(self, date):
        self.end_date_selected.emit(date)
    
    def delete_start_date(self):
        self.start_date_selected.emit(QDate())
    def delete_end_date(self):
        self.end_date_selected.emit(QDate())