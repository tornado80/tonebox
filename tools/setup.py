from PySide2.QtCore import QObject
import json
import os

class Settings(object):

    DEFAULT_SETTINGS_PATH = "settings.json"
    DEFAULT_JSON_FIELDS = {
        "DatabasePath" : "tonebox.db",
        "AppName" : "ToneBox Copyright 2020 Mo-Rajab-Team"
    }

    def __init__(self):
        self.json_dict = {}
        if not self.settings_file_exists():
            self.create_settings_file()
        else:
            self.read_settings_file()

    def settings_file_exists(self):
        if os.path.exists(Settings.DEFAULT_SETTINGS_PATH):
            try:                    
                with open(Settings.DEFAULT_SETTINGS_PATH, "r") as file:
                    json.load(file)
            except json.JSONDecodeError as error:
                self.show_errors_to_user(error.msg)
                return False
            else:
                return True
        else:
            return False

    def create_settings_file(self):
        self.json_dict = Settings.DEFAULT_JSON_FIELDS.copy()
        self.write_settings_file()

    def write_settings_file(self):
        with open(Settings.DEFAULT_SETTINGS_PATH, "w") as file:
            json.dump(self.json_dict, file)

    def read_settings_file(self):
        with open(Settings.DEFAULT_SETTINGS_PATH, "r") as file:
            self.json_dict = json.load(file)

    def show_messages_to_user(self, msg):
        print(msg)

    def show_errors_to_user(self, err):
        print(err)

class SettingsModel(QObject, Settings):
    def __init__(self):
        QObject.__init__(self)
        Settings.__init__(self)