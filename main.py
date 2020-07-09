from core.media_player import MediaPlayer
from PySide2.QtWidgets import QApplication
import sys
from gui.main_window import MainWindow
from tools.setup import SettingsModel
from core import songs_model, playlists_model, queue_model, media_player

class ToneBoxApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settings_model = SettingsModel()
        self.songs_manager_model = songs_model.SongsManagerModel()
        self.playlists_manager_model = playlists_model.PlyalistsManagerModel()
        self.queue_model = queue_model.QueueModel()
        self.player_object = media_player.MediaPlayer()
        self.player_object.setPlaylist(self.queue_model)
        self.main_window = MainWindow()

tone_box_app = ToneBoxApp(sys.argv)
tone_box_app.exec_()
