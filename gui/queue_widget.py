from PySide2.QtGui import QIcon, QPixmap
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
        self.clearQueueAction = self.contextMenu.addAction("Clear queue")
        
        self.doubleClicked.connect(self.handle_double_click)
        self.row_numbers = 0
        self.current_playing_row = None  
    
    def handle_double_click(self, idx):
        self.queue_manager.setCurrentIndex(idx.row())

    def add_row(self, *args):
        self.insertRow(self.row_numbers)
        for i in range(1, 5):
            item = QTableWidgetItem(str(args[i-1]))
            self.setItem(self.row_numbers, i, item)
        self.row_numbers += 1
    
    def set_current_playing(self, row):
        print("set_current_playing", row)
        item = self.item(1, 1)
        print(item)
        item.setIcon(QIcon(QPixmap(u":/images/icons/icons8-play-30.png")))
        if self.current_playing_row is not None:
            item = self.item(self.current_playing_row, 0)
            item.setIcon(QIcon())
        self.current_playing_row = row

    def clear_rows(self):
        self.clearContents()
        self.setRowCount(0)
        self.row_numbers = 0

    def contextMenuEvent(self, event):
        self.contextMenu.exec_(event.globalPos())