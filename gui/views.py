from PySide2.QtWidgets import QAbstractItemView, QListWidget, QTableWidget, QTableWidgetItem, QMenu

class FilterView(QListWidget):
    def __init__(self, parent):
        super().__init__(parent)

class SongsView(QTableWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.model = None
        self.settings_model = None
        self.filterViews = []
        self.rows_data = []
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.horizontalHeader().setStretchLastSection(True)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setSectionsMovable(True)
        self.doubleClicked.connect(self.play_item)

    def contextMenuEvent(self, event):
        row = self.rowAt(event.y())
        if row != -1:
            print("Context menu event for row number:", row)
            #menu = QMenu(self)
            #menu.addAction("Me Test")
            #menu.exec_(event.globalPos())

    def play_item(self, idx):
        print("Row double clicked. Row number:", idx.row(), "Column number:", idx.column())

    def setup_columns(self):
        self.setColumnCount(len(self.settings_model.json_dict["SongsViewHeaders"]))
        #default_headers = Settings.DEFAULT_JSON_FIELDS["SongsViewHeader"].keys()
        #self.setHorizontalHeaderLabels(default_headers)
        #for i in range(len(default_headers)):
        #    if not self.settings_model.json_dict["SongsViewHeader"][default_headers[i]][0]:
        #        self.setColumnHidden(i, True)
        for key, value in self.settings_model.json_dict["SongsViewHeaders"].items():
            self.setHorizontalHeaderItem(value[1], QTableWidgetItem(key))
            if not value[0]:
                self.setColumnHidden(value[1], True)
        
    def connect_to_filter_view(self, fview):
        self.filterViews.append(fview)

    def update_view(self):
        self.clearContents()
        self.rows_data.clear()
        self.filter_view()
        self.setRowCount(len(self.rows_data))
        for i in range(len(self.rows_data)):
            song = self.model.songs[self.rows_data[i]]
            for key, value in self.settings_model.json_dict["SongsViewHeaders"].items():
                self.setItem(i, value[1], QTableWidgetItem(
                    str(getattr(song, self.settings_model.SONGS_VIEW_HEADERS_TRANSLATIONS[key]))
                ))

    def filter_view(self):
        search = {}
        for view in self.filterViews:
            search.update(view.songs_filter_keywords())
        self.rows_data = self.model.songs_dict_filter(**search)
        