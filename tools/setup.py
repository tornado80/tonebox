from PySide2.QtCore import QObject
import json
import os

def validate_songs_view_headers(s):
    if s.keys() != SettingsModel.SONGS_VIEW_HEADERS_TRANSLATIONS.keys():
        return False
    else:
        return True

class Settings(object):

    DEFAULT_SETTINGS_PATH = "settings.json"
    DEFAULT_JSON_FIELDS = {
        "DatabasePath" : "tonebox.db",
        "AppName" : "ToneBox Copyright 2020 Mo-Rajab-Team",
        "OpenFilePath" : "/",
        "SongsViewHeaders" : {
            "Title" : 1, 
            "Album" : 1, 
            "Artist" : 1, 
            "Genre" : 1, 
            "Duration" : 1, 
            "Location" : 1, 
            "Total tracks" : 0, 
            "Year" : 1, 
            "Composer" : 0, 
            "File size" : 0, 
            "Bitrate" : 0, 
            "Sample rate" : 0,
            "Comment" : 1, 
            "Image" : 0, 
        }
    }
    DEFAULT_JSON_FIELDS_VALIDATORS = {
        "DatabasePath" : lambda s : False if s == "" else True,
        "AppName" : lambda s : True,
        "OpenFilePath" : lambda s : True,
        "SongsViewHeaders" : validate_songs_view_headers
    }
    SUPPORTED_AUDIO_FILES = ["*.wav", "*.mp3"]

    def __init__(self):
        self.json_dict = {}
        if not self.settings_file_exists():
            self.create_settings_file()
        else:
            self.read_settings_file()
            if not self.is_settings_file_valid():
                self.show_messages_to_user("Settings file not recognized. Making new one!")
                self.create_settings_file()

    def is_settings_file_valid(self):
        if self.json_dict.keys() != Settings.DEFAULT_JSON_FIELDS.keys():
            return False
        else:
            for k in self.json_dict.keys():
                if not Settings.DEFAULT_JSON_FIELDS_VALIDATORS[k](self.json_dict[k]):
                    return False
        return True

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
    SONGS_VIEW_HEADERS_TRANSLATIONS = {
        "Title" : "title",
        "Album" : "album",
        "Artist" : "artist",
        "Genre" : "genre",
        "Duration" : "duration",
        "Location" : "path",
        "Total tracks" : "track_total",
        "Year" : "year",
        "Composer" : "composer",
        "File size" : "filesize",
        "Bitrate" : "bitrate",
        "Sample rate" : "samplerate",
        "Comment" : "comment",
        "Image" : "image"
    }
    def __init__(self):
        QObject.__init__(self)
        Settings.__init__(self)

if __name__ == "__main__":
    s = SettingsModel()
    print(s.json_dict)