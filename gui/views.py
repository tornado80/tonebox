from PySide2.QtWidgets import QAbstractItemView, QListWidget, QTableWidget, QTableWidgetItem, QMenu, QMessageBox

class FilterView(QListWidget):
    def __init__(self, parent):
        super().__init__(parent)

class SongsView(QTableWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.manager_model = None
        self.settings_model = None
        self.context_menu_selected_song_id = None
        self.filterViews = []
        self.rows_data = []
        self.setup_ui()

    def setup_ui(self):
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.horizontalHeader().setStretchLastSection(True)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setSectionsMovable(True)
        self.doubleClicked.connect(self.double_click_to_play_song)
        self.setup_context_menu()

    def connect_to_models(self, manager_model, settings_model):
        self.manager_model = manager_model
        self.settings_model = settings_model
        # signals

    def contextMenuEvent(self, event):
        row = self.rowAt(event.y())
        if row != -1:
            self.context_menu_selected_song_id = self.rows_data[row]
            print("Context menu event for row number:", row)
            self.contextMenu.exec_(event.globalPos())
            print("Done!")

    def double_click_to_play_song(self, idx):
        print("Playing song name:", self.manager_model.songs[self.rows_data[idx.row()]])
        print("Row double clicked. Row number:", idx.row(), "Column number:", idx.column())

    def setup_context_menu(self):
        self.contextMenu = QMenu(self)
        self.addToQueueAction = self.contextMenu.addAction("Add to Queue")
        self.addToPlaylistAction = self.contextMenu.addAction("Add to Playlist")
        self.removeSongAction = self.contextMenu.addAction("Remove song")
        self.informationAction = self.contextMenu.addAction("Information")
        self.removeSongAction.triggered.connect(self.handle_remove_song_action)
        self.addToQueueAction.triggered.connect(self.handle_add_to_queue)
        self.addToPlaylistAction.triggered.connect(self.handle_add_to_playlist)
        self.informationAction.triggered.connect(self.handle_information)

    def handle_information(self):
        pass

    def handle_add_to_playlist(self):
        pass

    def handle_add_to_queue(self):
        pass

    def handle_remove_song_action(self):
        if QMessageBox.question(self, "User Consent", "Do you really want to remove the file from Library?", QMessageBox.Yes, QMessageBox.No):
            self.manager_model.remove_song(song_id = self.context_menu_selected_song_id)
        
    def update_columns(self):
        headers = list(self.settings_model.DEFAULT_JSON_FIELDS["SongsViewHeaders"].keys())
        self.setColumnCount(len(headers))
        self.setHorizontalHeaderLabels(headers)
        for i in range(len(headers)):
            if not self.settings_model.json_dict["SongsViewHeaders"][headers[i]]:
                self.setColumnHidden(i, True)
        
    def connect_to_filter_view(self, fview):
        self.filterViews.append(fview)

    def update_view(self):
        self.update_columns()
        self.update_rows()

    def update_rows(self):
        self.clearContents()
        self.rows_data.clear()
        self.filter_view()
        self.setRowCount(len(self.rows_data))
        headers = list(self.settings_model.DEFAULT_JSON_FIELDS["SongsViewHeaders"].keys())
        for i in range(len(self.rows_data)):
            song = self.manager_model.songs[self.rows_data[i]]
            for j in range(len(headers)):
                self.setItem(i, j, QTableWidgetItem(
                    str(getattr(song, # duration as an integer should be an object and __str__ overloaded for it
                        self.settings_model.SONGS_VIEW_HEADERS_TRANSLATIONS[headers[j]]
                    ))
                ))

    def filter_view(self):
        search = {}
        for view in self.filterViews:
            search.update(view.songs_filter_keywords())
        self.rows_data = self.manager_model.songs_dict_filter(**search)
        