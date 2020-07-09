from PySide2.QtWidgets import QTableWidget

class QueueWidget(QTableWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        