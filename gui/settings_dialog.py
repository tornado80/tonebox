from PySide2.QtWidgets import QDialog, QFileDialog
from .settings_dialog_ui import Ui_SettingsDialogUi

class SettingsDialog(QDialog, Ui_SettingsDialogUi):
    def __init__(self, parent, settings_model, manager_model):
        super().__init__(parent)
        self.setupUi(self)
        self.settings_model = settings_model
        self.manager_model = manager_model
        self.reloadDatabaseButton.clicked.connect(self.reload_database)
        self.resetDatabasePathButton.clicked.connect(self.reset_database_path)
        self.resetHeadersButton.clicked.connect(self.reset_headers)
        self.resetDefaultPathButton.clicked.connect(self.reset_default_path)
        self.reloadSettingsButton.clicked.connect(self.reload_settings)
        self.defaultPathButton.clicked.connect(self.get_default_path)
        self.databasePathButton.clicked.connect(self.get_database_path)

    def get_database_path(self):
        p, _ = QFileDialog.getOpenFileName(self, "Open Database File",
            self.databasePathLineEdit.text(),
            "ToneBox DB Files (*.db)")
        if p != "":
            self.databasePathLineEdit.setText(p)

    def get_default_path(self):
        p = QFileDialog.getExistingDirectory(self, "Open File Path",
                                       self.defaultPathLineEdit.text(),
                                       QFileDialog.ShowDirsOnly)
        if p != "":
            self.defaultPathLineEdit.setText(p)

    def reload_database(self):
        self.manager_model.close_connection()
        self.manager_model.db_path = self.settings_model.get("DatabasePath")
        self.manager_model.songs.clear()
        self.manager_model.playlists.clear()
        self.manager_model.setup_connection()
        self.manager_model.modelUpdated.emit()
    
    def reload_settings(self):
        self.settings_model.setup_settings()
        self.get_ready()

    def reset_headers(self):
        self.settings_model.update("SongsViewHeaders", self.settings_model.DEFAULT_JSON_FIELDS["SongsViewHeaders"].copy())
        self.get_ready()

    def reset_database_path(self):
        self.settings_model.update("DatabasePath", self.settings_model.DEFAULT_JSON_FIELDS["DatabasePath"])
        self.get_ready()

    def reset_default_path(self):
        self.settings_model.update("RememberLastPath", self.settings_model.DEFAULT_JSON_FIELDS["RememberLastPath"])
        self.settings_model.update("OpenFilePath", self.settings_model.DEFAULT_JSON_FIELDS["OpenFilePath"])
        self.get_ready()

    def get_ready(self):
        self.defaultPathLineEdit.setText(self.settings_model.get("OpenFilePath"))
        self.databasePathLineEdit.setText(self.settings_model.get("DatabasePath"))
        self.rememberCheckBox.setChecked(True if self.settings_model.get("RememberLastPath") else False)
        for key, value in self.settings_model.SONGS_VIEW_HEADERS_TRANSLATIONS.items():
            getattr(self, f"{value}CheckBox").setChecked(
                True if self.settings_model.get("SongsViewHeaders")[key] else False
                )

    def accept(self):
        self.settings_model.update("DatabasePath", self.databasePathLineEdit.text())
        self.settings_model.update("OpenFilePath", self.defaultPathLineEdit.text())
        self.settings_model.update("RememberLastPath", 1 if self.rememberCheckBox.isChecked() else 0)
        for key, value in self.settings_model.SONGS_VIEW_HEADERS_TRANSLATIONS.items():            
            self.settings_model.json_dict["SongsViewHeaders"][key] = 1 if getattr(self, f"{value}CheckBox").isChecked() else 0        
        self.settings_model.write_settings_file()
        self.reload_database()
        return super().accept()

    def exec_(self):
        self.get_ready()
        return super().exec_()