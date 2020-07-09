import sqlite3
import ntpath
from tinytag import TinyTag

class Song:
     def __init__(self, path, id_=None, artist=None, title=None, album=None, track_total=None, duration=None, genre=None, year=None, composer=None, filesize=None, bitrate=None, samplerate=None, comment=None, image=None):
        self.path = path
        self.tag = TinyTag.get(path)
        self.id_ = id_
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

class SongsManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.db_name = ntpath.basename(db_path) #assumes the file name is the dbs name
        self.songs = {}

        self.conn = sqlite3.connect(self.db_path)    #change to :memory: if u want to test
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
            songs = self.c.fetchall()           
            for song in songs:
                self.songs[TinyTag.get(song[0]).title] = song[0]

    def add(self, song_path):
        try:
            self.c.execute(f"INSERT INTO {self.db_name} VALUES ({song_path})")
        except Exception as e:
            return repr(e)
        else:
            self.conn.commit()    

    def remove(self, song_path):
        try:
            self.c.execute(f"DELETE FROM {self.db_name} WHERE path=?", (song_path,))
            self.conn.commit()
        except Exception as e:
            return repr(e)
        else:
            self.conn.commit()        

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