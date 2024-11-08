from PyQt5.QtWidgets import QApplication

# Dark Theme als Style Sheet
dark_stylesheet = """
    QWidget {
        background-color: #2b2b2b;
        color: #ffffff;
    }
    
    QLineEdit, QComboBox, QListView {
        background-color: #3c3f41;
        color: #ffffff;
    }
    
    QTabBar::tab {
        background-color: #3c3f41;
        color: #ffffff;
        padding: 10px;
    }
    
    QTabBar::tab:selected {
        background-color: #555555;
    }
    
    QTabWidget::pane {
        border: 1px solid #555555;
    }
    
    QHeaderView::section {
        background-color: #3c3f41;
        color: #ffffff;
        padding: 4px;
        border: 1px solid #555555;
    }
    
    QTableWidget {
        background-color: #3c3f41;
        gridline-color: #555555;
    }
    
    QTableCornerButton::section {
        background-color: #3c3f41;
        border: 1px solid #555555;
    }
    
    QPushButton {
        background-color: #3c3f41;
        border: 1px solid #555555;
        color: white;
    }
    
    QPushButton:hover {
        background-color: #555555;
    }
"""