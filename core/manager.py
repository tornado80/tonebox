import datetime
import sqlite3
import ntpath
from tinytag import TinyTag

class Playlist:
    def __init__(self, name, db_id=None, last_played=None):
        self.db_id = db_id
        self.name = name
        self.songs = []
        self.c_date = datetime.datetime.now()
        self.last_played = last_played

    def update_last_played(self):
        self.last_played = datetime.datetime.now()

    def get_songs(self):
        pass

class Song:
    def __init__(self, path, db_id=None, artist=None, title=None, album=None, track_total=None, duration=None, genre=None, year=None, composer=None, filesize=None, bitrate=None, samplerate=None, comment=None, image=None):
        self.db_id = db_id
        self.path = path
        self.tag = TinyTag.get(path)
        self.artist = self.tag.artist
        self.title = self.tag.title
        self.album = self.tag.album
        self.track_total = self.tag.track_total
        self.duration = self.tag.duration
        self.genre = self.tag.genre
        self.year = self.tag.year
        self.composer = self.tag.composer
        self.filesize = self.tag.filesize
        self.bitrate = self.tag.bitrate
        self.samplerate = self.tag.samplerate
        self.comment = self.tag.comment
        self.image = self.tag.get_image()

class Manager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.db_conn = sqlite3.connect(self.db_path)   
        self.db_cursor = self.db_conn.cursor()
        self.songs = []
        self.playlists = {}

    def add_playlist(self, playlist_name):
        try:
            new_playlist = Playlist(playlist_name)
            self.playlists[new_playlist] = []
            self.db_cursor.execute(f"INSERT INTO playlists(name) VALUES (?)", (new_playlist.name,))    
        except Exception as e:
            self.show_errors_to_user(e)
        else:
            self.db_conn.commit()

    def remove_playlist(self, playlist_name):
        try:
            for playlist in self.playlists.keys():
                if playlist_name == playlist:
                    del self.playlists[playlist]
                    
            self.db_cursor.execute("SELECT playlist_id FROM  WHERE name=?", (playlist_name,))
            playlist_id = str(self.db_cursor.fetchone())
            self.db_cursor.execute("DELETE FROM playlists WHERE name=?", (playlist_name,))
            self.db_cursor.execute("DELETE FROM group WHERE playlist_id=?", (playlist_id,))
        except Exception as e:                                                     
            self.show_errors_to_user(e)
        else:
            self.db_conn.commit()

    def add_song(self, song_path):
        try:
            new_song = Song(song_path)
            self.songs.append(new_song)
            self.db_cursor.execute("INSERT INTO songs (path) VALUES (?)", (new_song.path,))
        except Exception as e:
            self.show_errors_to_user(e)
        else:
            self.db_conn.commit()    

    def remove_song(self, song_path):
        try:
            for song in self.songs:
            if song_path == song.path:
                del song

            self.db_cursor.execute("SELECT song_id FROM songs WHERE path=?", (song_path,))
            song_id = str(self.db_cursor.fetchone())
            self.db_cursor.execute("DELETE FROM songs WHERE path=?", (song_path,))
            self.db_cursor.execute("DELETE FROM group WHERE song_id=?", (song_id,))
        except Exception as e:
            self.show_errors_to_user(e)
        else:
            self.db_conn.commit()        

    def get_alldata(self):
        pass

    def filter(self, query):
        try:
            self.db_cursor.execute(query)
        except Exception as e:
            self.show_errors_to_user(e)
        else:        
            self.db_conn.commit()

    def close_connection(self):
        self.db_conn.close()

    def show_errors_to_user(self, err):
        print(err)    
