from PySide2.QtCore import QUrl, QByteArray
from PySide2.QtGui import QPixmap
from PySide2.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist

class SongContent(QMediaContent):
    def __init__(self, src, song, playlist_name):
        super().__init__(src)
        self.tonebox_song = song
        self.tonebox_playlist_name = playlist_name

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
        self.song_contents = []
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
        self.next()
    
    def previous_track(self):
        self.previous()

    def change_volume(self, vol):
        self.player_object.setVolume(vol)

    def change_position(self, pos):
        self.player_object.setPosition(pos)
    
    def change_mute(self, muted):
        self.player_object.setMuted(muted)
    
    def change_playback(self):
        self.setPlaybackMode(self.player_widget.play_back_mode)
        if self.player_widget.play_back_mode == QMediaPlaylist.Random:
            self.shuffle()

    def pause_queue(self):
        self.player_object.pause()
        self.player_widget.playPauseBtn.setChecked(False)

    def change_speed(self, spe):
        cur_pos = self.player_object.position()
        self.player_object.setPlaybackRate(spe)
        self.player_object.setPosition(cur_pos)

    def setup_player_signals(self):
        self.player_object.positionChanged.connect(self.update_time_seek_slider)
        self.player_object.setNotifyInterval(100)
        self.player_object.mediaStatusChanged.connect(self.media_status_changed)
        self.player_object.stateChanged.connect(self.media_state_changed)
        self.player_object.mediaChanged.connect(self.update_player_widget)

    def update_time_seek_slider(self, pos):
        if not self.player_widget.position_changing_state:
            self.player_widget.timeSeekSlider.setValue(pos)
            self.player_widget.elapsedTimeLineEdit.setText(self.showTimeProperly(int(pos/1000)))
    
    def update_player_widget(self, media):
        print(media.tonebox_song.name)

    def media_state_changed(self):
        print("Media sate changed", self.player_object.state())
        if self.player_object.state() == QMediaPlayer.PlayingState:
            song_id = self.songs_data_by_rows[self.currentIndex()][0]
            song = self.manager_model.songs[song_id]
            self.player_widget.timeSeekSlider.setMaximum(int(song.duration) * 1000)
            self.player_widget.totalTimeLineEdit.setText(self.showTimeProperly(int(song.duration)))
            qp = QPixmap()
            qp.loadFromData(QByteArray(song.image))
            self.player_widget.coverImageLabel.setPixmap(qp)                  
            self.player_widget.infoLabel.setText(f"""
                <html><head/><body>
                <p><span style="font-size:18pt; font-weight:600;">{song.title}</span></p>
                <p><span style=" font-size:14pt;">{song.album} - {song.artist}</span></p>
                </body></html>
            """)
            self.change_speed(self.player_widget.speedSpinBox.value())
        if self.player_object.state() == QMediaPlayer.StoppedState:
            self.player_widget.totalTimeLineEdit.setText("")
            self.player_widget.elapsedTimeLineEdit.setText("")
            self.player_widget.infoLabel.setText("No Song")
            self.player_widget.coverImageLabel.setPixmap(QPixmap(u":/images/icons/Blank_CD_icon.png"))  

    def showTimeProperly(self, t):
        hours = 0
        minutes = 0
        while t > 3600:
            hours += 1
            t -= 3600
        while t > 60:
            minutes += 1
            t -= 60
        seconds = t
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def media_status_changed(self):
        print("Media status changed", self.player_object.mediaStatus())

    def play_queue(self):
        self.player_object.play()
        self.player_widget.playPauseBtn.setChecked(True)

    def clear_queue(self):
        self.songs_by_rows.clear()
        self.songs_by_visuals.clear()
        self.songs_data_by_rows.clear()
        self.queue_widget.clear_rows()
        self.clear()

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
            sc = SongContent(QUrl.fromLocalFile(song.path), song, playlist_name)
            self.addMedia(sc)
            self.queue_widget.add_row(*[song.title, song.album, song.artist, playlist_name])
    