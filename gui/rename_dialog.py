from PySide2.QtWidgets import QDial, QDialog, QMessageBox
from .rename_dialog_ui import Ui_RenameDialogUi

class RenameDialog(QDialog, Ui_RenameDialogUi):
    def __init__(self, parent, current_name):
        super().__init__(parent)
        self.setupUi(self)
        self.lineEdit.setText(current_name)
        self.lineEdit.selectAll()

    def accept(self):
        if self.lineEdit.text() != "":
            return super().accept()
        else:
            QMessageBox.critical(self, "Error", "Playlist name can not be empty.", QMessageBox.Ok)