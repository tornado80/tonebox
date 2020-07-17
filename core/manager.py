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
        self.tag = TinyTag.get(path, image = True)
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
        path TEXT UNIQUE NOT NULL
    );
    CREATE TABLE IF NOT EXISTS Playlists (
        playlist_id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL
    );
    CREATE TABLE IF NOT EXISTS SongsPlaylistsGroups (
        record_id INTEGER PRIMARY KEY,
        song_id INTEGER NOT NULL,
        playlist_id INTEGER NOT NULL, 
        FOREIGN KEY (song_id) REFERENCES Songs (song_id),
        FOREIGN KEY (playlist_id) REFERENCES Playlists (playlist_id)
    );
    """

    def __init__(self, db_path):
        self.db_path = db_path
        self.songs = {}
        self.playlists = {}
        if self.open_connection():
            self.setup_database()
            self.get_all_data()

    def open_connection(self):
        try:
            self.db_connection = sqlite3.connect(self.db_path)
            self.db_cursor = self.db_connection.cursor()
            return 1
        except sqlite3.Error as err:
            self.show_errors_to_user(err)
            return 0

    def is_database_valid(self) -> bool:
        try:
            self.db_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            self.db_connection.commit()
            for tbl in self.db_cursor.fetchall():
                if tbl[0] not in ["Songs", "Playlists", "SongsPlaylistsGroups"]:
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
            self.db_connection.commit()
        except sqlite3.Error as err:
            self.show_errors_to_user(err, "setup_database")

    def get_all_data(self):
        try:
            self.db_cursor.execute("SELECT * FROM Songs")
            songs = self.db_cursor.fetchall()
            for data in songs:
                song = Song(data[1])
                self.songs[data[0]] = song
            self.db_cursor.execute("SELECT * FROM Playlists")
            playlists = self.db_cursor.fetchall()
            for data in playlists:
                playlist = Playlist(data[1])
                self.playlists[data[0]] = playlist        
            self.db_cursor.execute("SELECT * FROM SongsPlaylistsGroups")
            groups = self.db_cursor.fetchall()
            for group in groups:
                self.playlists[group[1]].songs = self.songs[group[2]]
        except sqlite3.Error as e:
            self.show_errors_to_user(e)        

    def add_playlist(self, playlist_name):
        try:
            new_playlist = Playlist(playlist_name)
            self.db_cursor.execute("INSERT INTO Playlists(name) VALUES (?)", (new_playlist.name,))
            self.db_cursor.execute("SELECT playlist_id FROM Playlists WHERE name=?", (playlist_name,))
            new_playlist.db_id = self.db_cursor.fetchone()[0]
            self.playlists[new_playlist.db_id] = new_playlist   
            self.db_connection.commit() 
        except sqlite3.Error as e:
            self.show_errors_to_user(e)
        else:
            return True
        return False

    def remove_playlist(self, playlist_name=None, playlist_id=None):
        if playlist_id:
            try:
                del self.playlists[playlist_id]
                self.db_cursor.execute("DELETE FROM Playlists WHERE playlist_id=?", (playlist_id,))
                self.db_cursor.execute("DELETE FROM SongsPlaylistsGroups WHERE playlist_id=?", (playlist_id,))
                self.db_connection.commit()    
            except sqlite3.Error as e:                                                     
                self.show_errors_to_user(e)
            else:
                return True
        elif playlist_name:
            try:
                for playlist_id in self.playlists.keys():
                    if playlist_name == self.playlists[playlist_id].name:
                        flag = playlist_id
                        break
                del self.playlists[flag]        
                self.db_cursor.execute("SELECT playlist_id FROM Playlists WHERE name=?", (playlist_name,))
                playlist_id = self.db_cursor.fetchone()[0]                                                                      
                self.db_cursor.execute("DELETE FROM Playlists WHERE name=?", (playlist_name,))
                self.db_cursor.execute("DELETE FROM SongsPlaylistsGroups WHERE playlist_id=?", (playlist_id,))
                self.db_connection.commit()
            except sqlite3.Error as e:                                                     
                self.show_errors_to_user(e)
            else:
                return True
        return False

    def add_song(self, song_path):
        try:
            new_song = Song(song_path)
            self.db_cursor.execute("INSERT INTO Songs(path) VALUES (?)", (new_song.path,))
            self.db_connection.commit()
            self.db_cursor.execute("SELECT song_id FROM Songs WHERE path=?", (song_path,))
            new_song.db_id = self.db_cursor.fetchone()[0]
            self.songs[new_song.db_id] = new_song
            self.db_connection.commit()
        except sqlite3.Error as e:
            self.show_errors_to_user(e)
        else:
            return True    
        return False

    def remove_song(self, song_path=None, song_id=None):
        if song_id:
            try:
                del self.songs[song_id]
                self.db_cursor.execute("DELETE FROM Songs WHERE song_id=?", (song_id,))
                self.db_cursor.execute("DELETE FROM SongsPlaylistsGroups WHERE song_id=?", (song_id,))
                self.db_connection.commit() 
            except sqlite3.Error as e:
                self.show_errors_to_user(e)
            else:
                return True
        elif song_path:
            try:
                for song_id in self.songs.keys():
                    if song_path == self.songs[song_id].path:
                        flag = song_id
                        break
                del self.songs[flag]        
                self.db_cursor.execute("SELECT song_id FROM Songs WHERE path=?", (song_path,))
                song_id = self.db_cursor.fetchone()[0]
                self.db_cursor.execute("DELETE FROM Songs WHERE path=?", (song_path,))
                self.db_cursor.execute("DELETE FROM SongsPlaylistsGroups WHERE song_id=?", (song_id,))
                self.db_connection.commit()
            except sqlite3.Error as e:
                self.show_errors_to_user(e)                
            else:
                return True
        return False                

    def songs_dict_filter(self, **keywords):
        result = []
        for song_id, song in self.songs.items():
            for kw_key, kw_val in keywords.items():
                if getattr(song, kw_key) != kw_val:
                    break
            else:
                result.append(song_id)
        return result                    

    def playlists_dict_filter(self, **keywords):
        result = []
        for playlist_id, playlist in self.playlists.items():
            for kw_key, kw_val in keywords.items():
                if getattr(playlist, kw_key) != kw_val:
                    break
            else:
                result.append(playlist_id)
        return result

    def add_song_to_playlist(self, playlist_id=None, song_id=None, playlist_name=None, song_path=None):  #tiny tag wont work so takes in song path instead of name
        if playlist_id and song_id:
            playlist = self.playlists[playlist_id]
            song = self.songs[song_id]
            playlist.songs.append(song)
            try:
                self.db_cursor.execute("INSERT INTO SongsPlaylistsGroups(song_id, playlist_id) VALUES (?, ?)", (song_id, playlist_id))
                self.db_connection.commit()
            except sqlite3.Error as e:
                self.show_errors_to_user(e)
            else:
                return True
        elif playlist_name and song_path:    
            for playlist_id in self.playlists.keys():
                if self.playlists[playlist_id].name == playlist_name:
                    playlist = self.playlists[playlist_id]
                    break
            for song_id in self.songs.keys():
                if self.songs[song_id].path == song_path:
                    song = self.songs[song_id] 
                    break
            playlist.songs.append(song)
            try:
                self.db_cursor.execute("INSERT INTO SongsPlaylistsGroups(song_id, playlist_id) VALUES (?, ?)", (song.db_id, playlist.db_id))
                self.db_connection.commit()
            except sqlite3.Error as e:
                self.show_errors_to_user(e)
            else:
                return True
        return False

    def remove_song_from_playlist(self, playlist_id=None, song_id=None, playlist_name=None, song_path=None):
        if playlist_id and song_id:
            playlist = self.playlists[playlist_id]
            song = self.songs[song_id]
            playlist.songs.remove(song)
            try:
                self.db_cursor.execute("DELETE FROM SongsPlaylistsGroups WHERE song_id=?", (song_id,))
                self.db_connection.commit()
            except sqlite3.Error as e:
                self.show_errors_to_user(e)
            else:
                return True
        elif playlist_name and song_path:    
            for playlist_id in self.playlists.keys():
                if self.playlists[playlist_id].name == playlist_name:
                    playlist = self.playlists[playlist_id]
                    break
            for song_id in self.songs.keys():
                if self.songs[song_id].path == song_path:
                    song = self.songs[song_id] 
                    break
            playlist.songs.remove(song)
            try:
                self.db_cursor.execute("DELETE FROM SongsPlaylistsGroups WHERE song_id=?", (song.db_id,))
                self.db_connection.commit() 
            except sqlite3.Error as e:
                self.show_errors_to_user(e)
            else:
                return True
        return False

    def filter(self, query):
        try:
            self.db_cursor.execute(query)
        except sqlite3.Error as e:
            self.show_errors_to_user(e)
        else:        
            self.db_connection.commit()

    def distinct_category_filter(self, category, **keywords) -> set: # this should be changed to alternative sql query for distinct on multi column
        result = set()
        for song in self.songs.values():
            for kw_key, kw_val in keywords.items():
                if getattr(song, kw_key) != kw_val:
                    break
            else:
                result.add(
                    tuple([
                        getattr(song, c) for c in category
                    ])
                )
        return result

    def close_connection(self):
        self.db_connection.close()

    def show_errors_to_user(self, err, place="[place not given]"):
        output = f"{err} at {place}"
        print(output)
        return output  

if __name__ == "__main__":
    m = Manager("tonebox.db")
    m.add_song("/home/amirhosein/Music/Seyed Jalaledin Mohammadian - Shirin Shirina.mp3")
