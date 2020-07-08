from PySide2.QtWidgets import QApplication
import sys
from gui.main_window import ToneBoxMainWindow
from tools.setup import SettingsModel
from core import songs_model, playlists_model, queue_model

class ToneBoxApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settings_model = SettingsModel()
        self.songs_manager_model = songs_model.SongsManagerModel()
        self.playlists_manager_model = playlists_model.PlyalistsManagerModel()
        self.queue_model = queue_model.QueueModel()
        self.main_window = ToneBoxMainWindow()

tone_box_app = ToneBoxApp(sys.argv)
tone_box_app.exec_()
