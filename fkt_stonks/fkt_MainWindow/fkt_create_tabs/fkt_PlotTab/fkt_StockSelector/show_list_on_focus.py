

from PyQt5.QtWidgets import QLineEdit

def show_list_on_focus(instance, event):
    # Liste anzeigen, wenn das Entry-Feld den Fokus erhält
    instance.list_widget.show()
    QLineEdit.focusInEvent(instance.entry, event)  # Standardfokusverhalten beibehalten