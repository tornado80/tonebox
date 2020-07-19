from PySide2.QtWidgets import QApplication
import sys
from gui.main_window import MainWindow
from tools.setup import SettingsModel
from core import manager_model, queue_manager, media_player

class ToneBoxApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settings_model = SettingsModel()
        self.manager_model = manager_model.Model(self.settings_model.get("DatabasePath"))
        self.queue_manager = queue_manager.QueueManager(self.manager_model)
        self.player_object = media_player.MediaPlayer()
        self.player_object.setPlaylist(self.queue_manager)
        self.queue_manager.player_object = self.player_object
        self.main_window = MainWindow(self.settings_model, self.manager_model, self.queue_manager)
        self.queue_manager.player_widget = self.main_window.playerWidget
        self.main_window.playerWidget.queue_manager = self.queue_manager
        self.queue_manager.queue_widget = self.main_window.queueWidget
        self.main_window.queueWidget.queue_manager = self.queue_manager
        self.queue_manager.setup_signals()
        self.main_window.show()

tone_box_app = ToneBoxApp(sys.argv)
tone_box_app.exec_()
