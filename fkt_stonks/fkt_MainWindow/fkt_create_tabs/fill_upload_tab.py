from PyQt5.QtWidgets import QVBoxLayout, QLabel, QTextEdit


def fill_upload_tab(tab):

    # Layout für den Upload-Reiter
    layout = QVBoxLayout()

    # Hinzufügen eines Labels mit anklickbarem Link
    link_label = QLabel('<a href="https://example.com">Hier können Sie die Kursdaten herunterladen.</a>')
    link_label.setOpenExternalLinks(True)  # Aktiviert den Link
    layout.addWidget(link_label)

    # Hinzufügen eines weiteren Beispiel-Labels
    another_link_label = QLabel('<a href="https://example2.com">Hier können Sie weitere Daten herunterladen.</a>')
    another_link_label.setOpenExternalLinks(True)
    layout.addWidget(another_link_label)

    # Drag-and-Drop-Feld
    drag_drop_area = QTextEdit("Dateien hier per Drag & Drop ablegen")
    drag_drop_area.setAcceptDrops(True)
    drag_drop_area.setReadOnly(True)
    layout.addWidget(drag_drop_area)

    # Funktion für das Drag-and-Drop-Verhalten
    drag_drop_area.dragEnterEvent = drag_enter_event
    drag_drop_area.dropEvent = drop_event

    tab.setLayout(layout)

def drag_enter_event(event):
    if event.mimeData().hasUrls():
        event.acceptProposedAction()

def drop_event(event):
    files = [url.toLocalFile() for url in event.mimeData().urls()]
    for file in files:
        print(f"Datei hinzugefügt: {file}")  # Hier könnte man die Datei weiterverarbeiten