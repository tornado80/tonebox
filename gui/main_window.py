from PySide2.QtWidgets import QMainWindow
from .main_window_ui import Ui_MainWindowUi

class MainWindow(QMainWindow, Ui_MainWindowUi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
