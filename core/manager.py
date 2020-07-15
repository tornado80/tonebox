import sqlite3
from tinytag import TinyTag

class Playlist:
    def __init__(self, name, db_id=None):
        self.db_id = db_id
        self.name = name
        self.songs = []

class Song:
    def __init__(self, path, db_id=None):
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

    SQLITE_SCHEMA = """
    CREATE TABLE IF NOT EXISTS Songs (
        song_id INTEGER PRIMARY KEY,
        path TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS Playlists (
        playlist_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS SongsPlaylistsGroup (
        record_id INTEGER PRIMARY KEY,
        song_id INTEGER NOT NULL,
        playlist_id INTEGER NOT NULL, 
        FOREIGN KEY (song_id) REFERENCES Songs (song_id),
        FOREIGN KEY (playlist_id) REFERENCES Playlists (playlist_id)
    );
    """

    def __init__(self, db_path):
        self.db_path = db_path
        if self.open_connection():
            self.setup_database()

    def open_connection(self):
        try:
            self.db_conn = sqlite3.connect(self.db_path)
            self.db_cursor = self.db_conn.cursor()
            return 1
        except sqlite3.Error as err:
            self.show_errors_to_user(err)
            return 0

    def is_database_valid(self) -> bool:
        try:
            self.db_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            self.db_conn.commit()
            for tbl in self.db_cursor.fetchall():
                if tbl[0] not in ["Songs", "Playlists", "SongsPlaylistsGroup"]:
                    return False
            return True
        except sqlite3.Error as err:
            self.show_errors_to_user(err)
            return False

    def setup_database(self):
        try:
            if not self.is_database_valid():
                self.close_connection()
                raise sqlite3.NotSupportedError("This database is not created by ToneBox App. Please change the path and try again.")
            self.db_cursor.executescript(Manager.SQLITE_SCHEMA)
            self.db_conn.commit()
        except sqlite3.Error as err:
            self.show_errors_to_user(err, "setup_database")

    def add_playlist(self, playlist_name):
        try:
            new_playlist = Playlist(playlist_name)
            self.db_cursor.execute(f"INSERT INTO playlists(name) VALUES (?)", (new_playlist.name,))    
        except Exception as e:
            self.show_errors_to_user(e)
        else:
            self.db_conn.commit()

    def remove_playlist(self, playlist_name):
        try:
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
            self.db_cursor.execute("INSERT INTO songs (path) VALUES (?)", (new_song.path,))
        except Exception as e:
            self.show_errors_to_user(e)
        else:
            self.db_conn.commit()    

    def remove_song(self, song_path):
        try:
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

    def show_errors_to_user(self, err, place=None):
        print(err, f"at {place}" if place is not None else "[place not given]")  

if __name__ == "__main__":
    m = Manager("test.db")
