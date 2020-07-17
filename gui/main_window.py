from PySide2.QtWidgets import QMainWindow, QFileDialog
from .main_window_ui import Ui_MainWindowUi

class MainWindow(QMainWindow, Ui_MainWindowUi):
    def __init__(self, settings_model, manager_model, queue_model, player_object):
        super().__init__()
        self.setupUi(self)
        self.showMaximized()
        self.settings_model = settings_model
        self.manager_model = manager_model
        self.queue_model = queue_model
        self.player_object = player_object
        
        # views
        self.librarySongsView.connect_to_models(self.manager_model, self.settings_model)
        self.librarySongsView.update_view()

        self.albumSongsView.connect_to_models(self.manager_model, self.settings_model)
        self.albumSongsView.update_view()
        self.albumFilterView.connect_to_models(self.manager_model, self.settings_model)
        self.albumFilterView.setCategory(["album", "artist"])
        self.albumFilterView.update_view()
        self.albumSongsView.connect_to_filter_view(self.albumFilterView)

        self.artistSongsView.connect_to_models(self.manager_model, self.settings_model)
        self.artistSongsView.update_view()
        self.artistFilterView.connect_to_models(self.manager_model, self.settings_model)
        self.artistFilterView.setCategory(["artist"])
        self.artistFilterView.update_view()
        self.artistSongsView.connect_to_filter_view(self.artistFilterView)

        self.genreSongsView.connect_to_models(self.manager_model, self.settings_model)
        self.genreSongsView.update_view()
        self.genreFilterView.connect_to_models(self.manager_model, self.settings_model)
        self.genreFilterView.setCategory(["genre"])
        self.genreFilterView.update_view()
        self.genreSongsView.connect_to_filter_view(self.genreFilterView)

        # actions
        self.actionAddMusic.triggered.connect(self.handle_add_music_action)
        self.actionNewPlaylist.triggered.connect(self.handle_new_playlist_action)
        self.actionSettings.triggered.connect(self.handle_settings)

    def handle_add_music_action(self):
        new_songs, _ = QFileDialog.getOpenFileNames(self, 
            "Add Music(s) to Library", 
            self.settings_model.json_dict["OpenFilePath"],
            "Audio Files ({})".format(" ".join(self.settings_model.SUPPORTED_AUDIO_FILES))
            )
        self.manager_model.add_songs(*new_songs)
    
    def handle_new_playlist_action(self):
        pass

    def handle_settings(self):
        pass

    def closeEvent(self, event):
        self.manager_model.close_connection()