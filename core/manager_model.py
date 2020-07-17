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
    modelUpdated = Signal()
    def __init__(self, db_path):
        QObject.__init__(self)
        Manager.__init__(self, db_path)

    def show_errors_to_user(self, err, place="[place not given]"):
        output = Manager.show_errors_to_user(self, err, place)
        QMessageBox.critical(None, "Error", output)

    def add_songs(self, *song_paths):
        added_songs_count = 0
        for song_path in song_paths:
            if not Manager.add_song(self, song_path):
                self.show_errors_to_user(f"Failed to add song with path \"{song_path}\"", "add_songs")
            else:
                added_songs_count += 1
        if added_songs_count != 0:
            self.songAdded.emit()
            self.modelUpdated.emit()
    
    def remove_songs(self, *song_ids):
        removed_songs_count = 0
        for song_id in song_ids:
            song_path = self.songs[song_id].path
            if not Manager.remove_song(self, song_id = song_id):
                self.show_errors_to_user(f"Failed to remove song with path \"{song_path}\"", "remove_songs")
            else:
                removed_songs_count += 1
        if removed_songs_count != 0:
            self.songRemoved.emit()
            self.modelUpdated.emit()
        
    def add_playlists(self, *playlist_names):
        added_playlists_count = 0
        for playlist_name in playlist_names:
            if not Manager.add_playlist(self, playlist_name):
                self.show_errors_to_user(f"Failed to add playlist with name \"{playlist_name}\"", "add_playlists")
            else:
                added_playlists_count += 1
        if added_playlists_count != 0:
            self.playlistAdded.emit()
            self.modelUpdated.emit()

    def remove_playlists(self, *playlist_ids):
        removed_playlists_count = 0
        for playlist_id in playlist_ids:
            playlist_name = self.playlists[playlist_id]
            if not Manager.remove_playlist(self, playlist_id = playlist_id):
                self.show_errors_to_user(f"Failed to remove playlist with name \"{playlist_name}\"", "remove_playlists")
            else:
                removed_playlists_count += 1
        if removed_playlists_count != 0:    
            self.playlistRemoved.emit()
            self.modelUpdated.emit()
    
    def add_songs_to_playlist(self, playlist_id, *song_ids):
        added_songs_count = 0
        playlist_name = self.playlists[playlist_id]
        for song_id in song_ids:
            song_name = self.songs[song_id]
            if not Manager.add_song_to_playlist(self, playlist_id = playlist_id, song_id = song_id):
                self.show_errors_to_user(f"Failed to add song \"{song_name}\" to playlist \"{playlist_name}\"", "add_songs_to_playlist")
            else:
                added_songs_count += 1
        if added_songs_count != 0:
            self.songAddedToPlaylist.emit()
            self.modelUpdated.emit()
    
    def remove_songs_from_playlist(self, playlist_id, *song_ids):
        removed_songs_count = 0
        playlist_name = self.playlists[playlist_id]
        for song_id in song_ids:
            song_name = self.songs[song_id]
            if not Manager.remove_song_from_playlist(self, playlist_id = playlist_id, song_id = song_id):
                self.show_errors_to_user(f"Failed to remove song \"{song_name}\" from playlist \"{playlist_name}\"", "remove_songs_from_playlist")
            else:
                removed_songs_count += 1
        if removed_songs_count != 0:
            self.songRemovedFromPlaylist.emit()
            self.modelUpdated.emit()