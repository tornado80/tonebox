from PySide2.QtWidgets import QAbstractItemView, QTableWidgetItem, QMenu, QTableWidget

class QueueWidget(QTableWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.horizontalHeader().setStretchLastSection(True)
        self.verticalHeader().setVisible(True)
        self.horizontalHeader().setVisible(True)
        self.horizontalHeader().setSectionsMovable(True)      
        self.verticalHeader().setSectionsMovable(True)
        self.setColumnCount(5)
        self.setHorizontalHeaderLabels(["Status", "Title", "Album", "Artist", "Playlist"])      
        self.contextMenu = QMenu(self)
        self.removeFromQueueAction = self.contextMenu.addAction("Remove song(s) from queue")
        self.doubleClicked.connect(self.handle_double_click)
        self.row_numbers = 0  
    
    def handle_double_click(self):
        pass

    def add_row(self, *args):
        self.insertRow(self.row_numbers)
        for i in range(1, 5):
            item = QTableWidgetItem(str(args[i-1]))
            self.setItem(self.row_numbers, i, item)
        self.row_numbers += 1
    
    def clear_rows(self):
        self.clearContents()
        self.row_numbers = 0

    def contextMenuEvent(self, event):
        pass