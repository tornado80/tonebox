import sqlite3
import ntpath

class Song:
     def __init__(self, path, id_=None, artist=None, title=None, album=None, track_total=None, duration=None, genre=None, year=None, composer=None, filesize=None, bitrate=None, samplerate=None, comment=None, image=None):
        self.path = path
        self.id_ = id_
        self.artist = artist
        self.title = title
        self.album = album
        self.track_total = track_total
        self.duration = duration
        self.genre = genre
        self.year = year
        self.composer = composer
        self.filesize = filesize
        self.bitrate = bitrate
        self.samplerate = samplerate
        self.comment = comment
        self.image = image

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
            return repr(e)                         #this is be a problem
        else:
            songs = self.c.fetchall()             #fetchall returns a list of tuples and for some reason i cant convert them to a string  
            for i, song in enumerate(songs):
                self.songs[f'song{i+1}'] = song   #would be better to change the keys to song titles

    def add(self):
        pass
    def remove(self):
        pass
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