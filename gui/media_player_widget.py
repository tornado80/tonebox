from PySide2.QtWidgets import QWidget
from .media_player_widget_ui import Ui_MediaPlayerWidget

class MediaPlayerWidget(QWidget, Ui_MediaPlayerWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
