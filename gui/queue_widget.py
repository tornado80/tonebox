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
        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(["Title", "Album", "Artist", "Playlist"])      
        self.contextMenu = QMenu(self)
        self.removeFromQueueAction = self.contextMenu.addAction("Remove song from queue")
        self.clearQueueAction = self.contextMenu.addAction("Clear queue")
        self.removeFromQueueAction.triggered.connect(self.handle_remove_from_queue)
        self.doubleClicked.connect(self.handle_double_click)
        self.current_playing_row = None  
    
    def handle_remove_from_queue(self):
        row = self.currentRow()
        self.removeRow(row)
        self.queue_manager.remove_song_from_queue(row)

    def handle_double_click(self, idx):
        self.queue_manager.setCurrentIndex(idx.row())
        self.queue_manager.play_queue()

    def add_row(self, *args):
        self.insertRow(self.rowCount())
        for i in range(4):
            if i == 3 and args[i] is None:
                item = QTableWidgetItem("")
            else:
                item = QTableWidgetItem(str(args[i]))
            self.setItem(self.rowCount() - 1, i, item)

    def set_current_paused(self, row):
        if self.current_playing_row is not None:
            item = self.item(self.current_playing_row, 0)
            if item is not None:
                item.setIcon(QIcon())
        if row is not None:
            item = self.item(row, 0)  
            if item is not None:      
                item.setIcon(QIcon(QPixmap(u":/images/icons/icons8-pause-30.png")))
        self.current_playing_row = row

    def set_current_playing(self, row):
        if self.current_playing_row is not None:
            item = self.item(self.current_playing_row, 0)
            if item is not None:
                item.setIcon(QIcon())
        if row is not None:
            item = self.item(row, 0)
            if item is not None:        
                item.setIcon(QIcon(QPixmap(u":/images/icons/icons8-play-30.png")))
        self.current_playing_row = row

    def clear_rows(self):
        self.clearContents()
        self.setRowCount(0)

    def contextMenuEvent(self, event):
        self.contextMenu.exec_(event.globalPos())