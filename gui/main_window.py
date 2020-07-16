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
        self.librarySongsView.connect_to_models_signals()
        self.librarySongsView.update_view()

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
        for new_song in new_songs:
            self.manager_model.add_song(new_song)
    
    def handle_new_playlist_action(self):
        pass

    def handle_settings(self):
        pass