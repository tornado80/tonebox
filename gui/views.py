from core.manager import Playlist
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QAbstractItemView, QListView, QListWidget, QListWidgetItem, QTableWidget, QTableWidgetItem, QMenu, QMessageBox
from PySide2.QtCore import Signal

class FilterView(QListWidget):
    childToBeUpdated = Signal()
    def __init__(self, parent):
        super().__init__(parent)
        self.manager_model = None
        self.settings_model = None
        self.parentFilterViews = []
        self.category = [] # should be list and could be [Album], [Album, Artist], [Genre], etc. it identifies filters to be shown
        self.setupUi()

    def setCategory(self, val):
        if not set(val) <= set(self.settings_model.SONGS_VIEW_HEADERS_TRANSLATIONS.values()):
            raise NotImplementedError("This category is not supported.")
        else:
            self.category = val

    def connect_to_models(self, manager_model, settings_model):
        self.manager_model = manager_model
        self.settings_model = settings_model
        self.connect_to_models_signals()
    
    def connect_to_models_signals(self):
        self.manager_model.songAdded.connect(self.update_view)
        self.manager_model.songRemoved.connect(self.update_view)

    def disconnect_from_models_signals(self):
        self.manager_model.songAdded.disconnect(self.update_view)
        self.manager_model.songRemoved.disconnect(self.update_view)

    def setupUi(self):
        self.setViewMode(QListWidget.ListMode)
        self.setMovement(QListView.Static)
        self.clicked.connect(self.single_click_to_filter_child)
        self.setup_context_menu()

    def contextMenuEvent(self, event):
        self.contextMenu.exec_(event.globalPos())

    def setup_context_menu(self):
        self.contextMenu = QMenu(self)
        self.viewModeAction = self.contextMenu.addAction("Icon Mode")
        self.viewModeAction.triggered.connect(self.handle_view_mode_action)

    def single_click_to_filter_child(self): # not sure to use idx
        self.childToBeUpdated.emit()

    def handle_view_mode_action(self):
        if self.viewMode() == QListWidget.ListMode:
            self.viewModeAction.setText("List Mode")
            self.setViewMode(QListWidget.IconMode)
        else:
            self.viewModeAction.setText("Icon Mode")
            self.setViewMode(QListWidget.ListMode)

    def connect_to_parent_filter_view(self, fview):
        fview.childToBeUpdated.connect(self.update_view)
        self.parentFilterViews.append(fview)

    def child_filter_keywords(self):
        result = self.accumulate_parent_keywords()
        if len(self.selectionModel().selectedRows()) > 0:
            selected_row = self.selectionModel().selectedRows()[0].row()
            for i in range(len(self.category)):
                result.update({
                    self.category[i] : self.rows_data[selected_row][i]
                    })
        return result
    
    def update_view(self):
        self.clear()
        self.rows_data = self.filter_view()
        for row_data in self.rows_data:
            shown_name = "({})" if len(row_data) > 1 else "{}"
            item = QListWidgetItem(shown_name.format(
                ", ".join(row_data)
            ))
            if ord("a") <= ord(str(row_data[0][0]).lower()) <= ord("z"):
                item.setIcon(QIcon(
                    QPixmap(u":/images/icons/ascii/{}.png".format(str(row_data[0][0]).lower()))
                    ))
            else:
                item.setIcon(QIcon(
                    QPixmap(u":/images/icons/ascii/question_mark.svg")
                    ))               
            self.addItem(item)
    
    def accumulate_parent_keywords(self):
        search = {}
        for pfv in self.parentFilterViews:
            search.update(pfv.child_filter_keywords())
        return search

    def filter_view(self):
        search = self.accumulate_parent_keywords()
        return list(self.manager_model.distinct_category_filter(self.category, **search))

class SongsView(QTableWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.manager_model = None
        self.settings_model = None
        self.filterViews = []
        self.setup_ui()

    def setup_ui(self):
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.horizontalHeader().setStretchLastSection(True)
        self.horizontalHeader().setSortIndicatorShown(True)
        self.setSortingEnabled(True)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setSectionsMovable(True)
        self.doubleClicked.connect(self.double_click_to_play_song)
        self.setup_context_menu()

    def connect_to_models(self, manager_model, settings_model):
        self.manager_model = manager_model
        self.settings_model = settings_model
        self.connect_to_models_signals()
    
    def connect_to_models_signals(self):
        self.manager_model.songAdded.connect(self.update_rows)
        self.manager_model.songRemoved.connect(self.update_rows)

    def disconnect_from_models_signals(self):
        self.manager_model.songAdded.disconnect(self.update_rows)
        self.manager_model.songRemoved.disconnect(self.update_rows)

    def contextMenuEvent(self, event):
        row = self.rowAt(event.y())
        if row != -1:
            if len(self.selectionModel().selectedRows()) > 1:
                self.informationAction.setVisible(False)
                self.playSongAction.setVisible(False)
            self.contextMenu.exec_(event.globalPos())
            self.informationAction.setVisible(True)
            self.playSongAction.setVisible(True)

    def double_click_to_play_song(self, idx):
        print("Playing song name:", self.manager_model.songs[self.rows_data[idx.row()]].title)
        print("Row double clicked. Row number:", idx.row(), "Column number:", idx.column())
        self.request_playing_song()

    def request_playing_song(self):
        pass

    def setup_context_menu(self):
        self.contextMenu = QMenu(self)
        self.playSongAction = self.contextMenu.addAction("Play")
        self.addToQueueAction = self.contextMenu.addAction("Add to Queue")
        self.addToPlaylistAction = self.contextMenu.addAction("Add to Playlist")
        self.removeSongAction = self.contextMenu.addAction("Remove song(s)")
        self.informationAction = self.contextMenu.addAction("Information")
        self.playSongAction.triggered.connect(self.request_playing_song)
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

    def handle_remove_song_action(self): # there is a bug here. we need a function to delete as many songs as we want and them emit signal
        if QMessageBox.question(self, "User Consent", "Do you really want to remove the file from Library?", QMessageBox.Yes, QMessageBox.No):
            songs_to_be_deleted = [self.rows_data[row_idx.row()] for row_idx in self.selectionModel().selectedRows()]
            self.manager_model.remove_songs(*songs_to_be_deleted)
        
    def update_columns(self):
        headers = list(self.settings_model.DEFAULT_JSON_FIELDS["SongsViewHeaders"].keys())
        self.setColumnCount(len(headers))
        self.setHorizontalHeaderLabels(headers)
        for i in range(len(headers)):
            if not self.settings_model.json_dict["SongsViewHeaders"][headers[i]]:
                self.setColumnHidden(i, True)
        
    def connect_to_filter_view(self, fview):
        fview.childToBeUpdated.connect(self.update_view)
        self.filterViews.append(fview)

    def update_view(self):
        self.update_columns()
        self.update_rows()

    def update_rows(self):
        self.clearContents()
        self.rows_data = self.filter_view()
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
            search.update(view.child_filter_keywords())
        return self.manager_model.songs_dict_filter(**search)

class PlaylistFilterView(FilterView):
    pass

class PlaylistSongsView(SongsView):
    pass