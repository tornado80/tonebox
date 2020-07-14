import datetime
import sqlite3
import ntpath

class Playlist:
    def __init__(self, name, last_played=None):
        self.name = name
        self.songs = []
        self.c_date = datetime.datetime.now()
        self.last_played = last_played

    def update_last_played(self):
        self.last_played = datetime.datetime.now()

    def get_songs(self):
        pass

class PlaylistManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.db_name = ntpath.basename(db_path)

        self.conn = sqlite3.connect(self.db_path) 
        self.c = self.conn.cursor()
        