import datetime
import sqlite3
import ntpath

class Playlist:
    def __init__(self, name, last_played=None):
        self.name = name
        self.id_ = id(self)
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
        self.conn = sqlite3.connect(self.db_path) 
        self.c = self.conn.cursor()

    def add_playlist(self, playlist):
        try:
            self.c.execute(f"INSERT INTO playlists VALUES ({playlist.id_}, {playlist.name})")    #assumes the table name is playlists if its not it should be changed
        except Exception as e:
            return repr(e)
        else:
            self.conn.commit()

    def remove_playlist(self, playlist):
        try:
            self.c.execute(f"DELETE FROM playlists WHERE id=?", (playlist.id_,))
        except Exception as e:                                                         #should also remove the playlists keys from the group table 
            return repr(e)
        else:
            self.conn.commit()

                


        