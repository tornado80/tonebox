from PySide2.QtWidgets import QAbstractItemView, QListWidget, QTableWidget, QTableWidgetItem

class FilterView(QListWidget):
    def __init__(self, parent):
        super().__init__(parent)

class SongsView(QTableWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.model = None
        self.filterViews = []
        self.rows_data = []
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.horizontalHeader().setStretchLastSection(True)
        #self.selectionModel().selectionChanged.connect(self.)
        self.doubleClicked.connect(self.play_item)

    def play_item(self, idx):
        print("Row double clicked. Row number:", idx.row())

    def setup_columns(self):
        """ This function will be connected to Settings signal for changing headers. """
        self.setColumnCount(13) # refer to Songs fileds in manager
        for i in range(5, 13):
            self.setColumnHidden(i, True)
        self.setHorizontalHeaderLabels(["Title", "Album", "Artist", "Genre", "Duration"])
        
    def connect_to_filter_view(self, fview):
        self.filterViews.append(fview)

    def update_view(self):
        self.clearContents()
        self.rows_data.clear()
        self.filter_view()
        self.setRowCount(len(self.rows_data))
        for i in range(len(self.rows_data)):
            song = self.model.songs[self.rows_data[i]]
            self.setItem(i, 0, QTableWidgetItem(song.title))
            self.setItem(i, 1, QTableWidgetItem(song.album))
            self.setItem(i, 2, QTableWidgetItem(song.artist))
            self.setItem(i, 3, QTableWidgetItem(song.genre))
            self.setItem(i, 4, QTableWidgetItem(song.duration))

    def filter_view(self):
        search = {}
        for view in self.filterViews:
            search.update(view.songs_filter_keywords())
        self.rows_data = self.model.songs_dict_filter(**search)
        