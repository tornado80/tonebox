import sqlite3
import ntpath
from tinytag import TinyTag

class Song:
     def __init__(self, path, id_=None, artist=None, title=None, album=None, track_total=None, duration=None, genre=None, year=None, composer=None, filesize=None, bitrate=None, samplerate=None, comment=None, image=None):
        self.path = path
        self.tag = TinyTag.get(path)
        self.id_ = id_
        self.artist = tag.artist
        self.title = tag.title
        self.album = tag.album
        self.track_total = tag.track_total
        self.duration = tag.duration
        self.genre = tag.genre
        self.year = tag.year
        self.composer = tag.composer
        self.filesize = tag.filesize
        self.bitrate = tag.bitrate
        self.samplerate = tag.samplerate
        self.comment = tag.comment
        self.image = tag.get_image()

class SongsManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.db_name = ntpath.basename(db_path) #assumes the file name is the dbs name
        self.songs = {}

        self.conn = sqlite3.connect(":memory:")    #change to :memory: if u want to test
        self.c = self.conn.cursor()

        #self.c.execute("""CREATE TABLE songs(
        #                path text
        #)""")                                                     #for testing
        #self.c.execute("INSERT INTO songs VALUES ('testing')")
        #self.conn.commit()
        
        try:
            self.c.execute("SELECT * FROM songs")
        except Exception as e:
            return repr(e)                         #this is a problem
        else:
            songs = self.c.fetchall()             #fetchall returns a list of tuples and for some reason i cant convert them to a string  
            for i, song in enumerate(songs):
                self.songs[f'song{i+1}'] = song   #would be better to change the keys to song titles

    def add(self, song_path):
        try:
            self.c.execute(f"INSERT INTO {self.db_name} VALUES ({song_path})")
        except Exception as e:
            return repr(e)

    def remove(self, song_path):
        try:
            self.c.execute(f"DELETE FROM {self.db_name} WHERE path=?", (song_path,))
        except Exception as e:
            return repr(e)    

    def get_alldata(self):
        pass

    def filter(self, query):
        try:
            self.c.execute(query)
        except Exception as e:
            return repr(e)
        else:        
            self.conn.commit()

    def close_connection(self):
        self.conn.close()

if __name__ == "__main__":
    testing = SongsManager('doesnt matter')
    print(testing.songs)