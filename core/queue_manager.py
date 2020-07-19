from PySide2.QtCore import QUrl
from PySide2.QtMultimedia import QMediaPlayer, QMediaPlaylist

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
        self.last_player_state = QMediaPlayer.StoppedState
        self.setPlaybackMode(QMediaPlaylist.Sequential)

    def setup_signals(self):
        self.setup_player_signals()
        self.setup_queue_widget_signals()

    def setup_queue_widget_signals(self):
        self.player_widget.speedChanged.connect(self.change_speed)
        self.player_widget.volumeChanged.connect(self.change_volume)
        self.player_widget.positionChanged.connect(self.change_position)
        self.player_widget.muteChanged.connect(self.change_mute)
        self.player_widget.playbackModeChanged.connect(self.change_playback)
        self.player_widget.trackPlayed.connect(self.play_queue)
        self.player_widget.trackPaused.connect(self.pause_queue)
        self.player_widget.stopTrackRequested.connect(self.stop_queue)
        self.player_widget.nextTrackRequested.connect(self.next_track)
        self.player_widget.previousTrackRequested.connect(self.previous_track)     

    def stop_queue(self):
        self.player_object.stop()

    def next_track(self):
        self.player_object.next()
    
    def previous_track(self):
        self.player_object.previous()

    def change_volume(self, spe):
        self.player_object.setPlaybackRate(spe)

    def change_position(self, pos):
        self.player_object.setPosition(pos)
    
    def change_mute(self, muted):
        self.player_object.setMuted(muted)
    
    def change_playback(self, mode):
        self.setPlaybackMode(mode)
        if mode == QMediaPlaylist.Random:
            self.shuffle()

    def pause_queue(self):
        self.player_object.pause()

    def change_speed(self, spe):
        self.player_object.setPlaybackRate(spe)

    def setup_player_signals(self):
        self.player_object.positionChanged.connect(self.update_time_seek_slider)
        self.player_object.setNotifyInterval(100)
        self.player_object.mediaStatusChanged.connect(self.media_status_changed)
        self.player_object.stateChanged.connect(self.media_state_changed)

    def update_time_seek_slider(self, pos):
        if not self.player_widget.position_changing_state:
            self.player_widget.timeSeekSlider.setValue(pos)
            self.player_widget.elapsedTimeLineEdit.setText(str(pos))
    
    def media_state_changed(self):
        print("Media sate changed", self.player_object.state())
        if self.player_object.state() == QMediaPlayer.PlayingState:
            #song = 
            self.player_widget.timeSeekSlider.setMaximum()

    def media_status_changed(self):
        print("Media status changed", self.player_object.mediaStatus())

    def play_queue(self):
        self.player_object.play()

    def clear_queue(self):
        self.songs_by_rows.clear()
        self.songs_by_visuals.clear()
        self.songs_data_by_rows.clear()
        self.queue_widget.clear_rows()

    def add_songs_to_queue(self, *songs_data):
        idx = len(self.songs_by_rows)
        for song_data in songs_data:
            song = self.manager_model.songs[song_data[0]]
            if song_data[1]:
                playlist_name = self.manager_model.playlists[song_data[1]].name
            else:
                playlist_name = None
            self.songs_by_visuals.append(idx)
            self.songs_by_rows.append(idx)
            self.songs_data_by_rows.append(song_data)
            self.addMedia(QUrl.fromLocalFile(song.path))
            self.queue_widget.add_row(*[song.title, song.album, song.artist, playlist_name])
    