from PySide2.QtWidgets import QMainWindow
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
        self.actionAddMusic.triggered.connect(self.addMusicActionTriggered)
        self.librarySongsView.model = self.manager_model
        self.librarySongsView.settings_model = self.settings_model
        self.librarySongsView.setup_columns()
        self.librarySongsView.update_view()

    def addMusicActionTriggered(self):
        print("hello")