class Song:
     def __init__(self, path, id_=None, artist=None, title=None, album=None, track_total=None, duration=None, genre=None, year=None, composer=None, filesize=None, bitrate=None, samplerate=None, comment=None, image=None):
        self.path = path
        self.id = id_
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
    pass