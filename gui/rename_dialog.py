from PySide2.QtWidgets import QDial, QDialog
from .rename_dialog_ui import Ui_RenameDialogUi

class RenameDialog(QDialog, Ui_RenameDialogUi):
    def __init__(self, parent, current_name):
        super().__init__(parent)
        self.setupUi(self)
        self.lineEdit.setText(current_name)