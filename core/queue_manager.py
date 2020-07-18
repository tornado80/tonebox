from PySide2.QtCore import QUrl
from PySide2.QtMultimedia import QMediaPlaylist

class QueueManager(QMediaPlaylist):
    def __init__(self, manager_model):
        super().__init__()
        self.manager_model = manager_model
        self.queue_widget = None
        self.player_widget = None
        self.player_object = None
        self.songs_by_rows = []
        self.songs_by_visuals = []
        self.songs_data_by_rows = []

    def setup_player_signals(self):
        pass

    def add_songs_to_queue(self, *songs_data):
        idx = len(self.songs_by_rows)
        for song_data in songs_data:
            song = self.manager_model.songs[song_data[0]]
            playlist_name = self.manager_model.playlists[song_data[1]].name
            self.songs_by_visuals.append(idx)
            self.songs_by_rows.append(idx)
            self.songs_data_by_rows.append(song_data)
            self.addMedia(QUrl.fromLocalFile(song.path))
            self.queue_widget.add_row(*[song.title, song.album, song.artist, playlist_name])
    