from PySide2.QtCore import QObject
from PySide2.QtWidgets import QMessageBox
from .manager import Manager
from PySide2.QtCore import Signal

class Model(QObject, Manager):

    songAdded = Signal()
    songRemoved = Signal()
    playlistAdded = Signal()
    playlistRemoved = Signal()
    songAddedToPlaylist = Signal()
    songRemovedFromPlaylist = Signal()

    def __init__(self, db_path):
        QObject.__init__(self)
        Manager.__init__(self, db_path)

    def show_errors_to_user(self, err, place="[place not given]"):
        output = Manager.show_errors_to_user(self, err, place)
        QMessageBox.critical(None, "Error", output)

    def add_song(self, song_path):
        if Manager.add_song(self, song_path):
            self.songAdded.emit()
    
    def remove_song(self, song_path=None, song_id=None):
        if Manager.remove_song(self, song_path, song_id):
            self.songRemoved.emit()

    def add_playlist(self, playlist_name):
        if Manager.add_playlist(self, playlist_name):
            self.playlistAdded.emit()

    def remove_playlist(self, playlist_name=None, playlist_id=None):
        if Manager.remove_playlist(self, playlist_name, playlist_id):
            self.playlistRemoved.emit()
    
    def add_song_to_playlist(self, playlist_name, song_path):
        if Manager.add_song_to_playlist(self, playlist_name, song_path):
            self.songAddedToPlaylist.emit()
    
    def remove_song_from_playlist(self, playlist_name, song_path):
        if Manager.remove_song_from_playlist(self, playlist_name, song_path):
            self.songRemovedFromPlaylist.emit()
