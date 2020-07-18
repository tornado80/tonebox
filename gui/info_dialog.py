from PySide2.QtCore import QByteArray
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QDialog
from .info_dialog_ui import Ui_InfoDialogUi

class InfoDialog(QDialog, Ui_InfoDialogUi):
    def __init__(self, parent, song, settings_model):
        super().__init__(parent)
        self.setupUi(self)
        self.song = song
        for val in settings_model.SONGS_VIEW_HEADERS_TRANSLATIONS.values():
            if val != "image":
                if hasattr(self, f"{val}LineEdit"):
                    getattr(self, f"{val}LineEdit").setText(str(
                        getattr(song, val)
                        ))
            else:
                qp = QPixmap()
                qp.loadFromData(QByteArray(song.image))
                self.imageLabel.setPixmap(qp)        

    def exec_(self):

        return super().exec_()

    def closeEvent(self, event):
        self.song = None
