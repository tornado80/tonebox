from PySide2.QtMultimedia import QMediaPlaylist
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QIcon, QPixmap
from .media_player_widget_ui import Ui_MediaPlayerWidget
from PySide2.QtCore import Signal

class MediaPlayerWidget(QWidget, Ui_MediaPlayerWidget):
    speedChanged = Signal()
    volumeChanged = Signal()
    positionChanged = Signal()
    muteChanged = Signal()
    playbackModeChanged = Signal()
    playPauseChanged = Signal()
    stopTrackRequested = Signal()
    nextTrackRequested = Signal()
    previousTrackRequested = Signal()
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.volumeSlider.valueChanged.connect(self.handle_volume_slider)
        self.playbackModeBtn.clicked.connect(self.handle_playback_btn)
        #self.speedSpinBox.valueChanged.connect()
        #self.muteBtn.clicked.connect(self.handle_mute_btn)
        #self.playPauseBtn.clicked.connect()
        #self.stopBtn.clicked.connect()
        #self.nextBtn.clicked.connect()
        #self.previuosBtn.clicked.connect()
        #self.fasterBtn.clicked.connect()
        #self.slowerBtn.clicked.connect()
        self.play_back_mode = QMediaPlaylist.Sequential

    def handle_volume_slider(self):
        self.volumeSpinBox.setValue(self.volumeSlider.value())
        if self.volumeSlider.value() < 25:
            self.volumeIcon.setPixmap(QPixmap(u":/images/icons/icons8-no-audio-30.png"))
        elif self.volumeSlider.value() < 50:
            self.volumeIcon.setPixmap(QPixmap(u":/images/icons/icons8-low-volume-30.png"))
        elif self.volumeSlider.value() < 75:
            self.volumeIcon.setPixmap(QPixmap(u":/images/icons/icons8-voice-30.png"))
        else:
            self.volumeIcon.setPixmap(QPixmap(u":/images/icons/icons8-audio-30.png"))
        self.volumeChanged.emit()

    def handle_playback_btn(self):
        if self.play_back_mode == QMediaPlaylist.Sequential:
            self.play_back_mode = QMediaPlaylist.CurrentItemOnce
            self.playbackModeBtn.setIcon(QIcon(QPixmap(u":/images/icons/no-repeat-one-30.png")))
        elif self.play_back_mode == QMediaPlaylist.CurrentItemOnce:
            self.play_back_mode = QMediaPlaylist.CurrentItemInLoop
            self.playbackModeBtn.setIcon(QIcon(QPixmap(u":/images/icons/icons8-repeat-one-30.png")))            
        elif self.play_back_mode == QMediaPlaylist.CurrentItemInLoop:
            self.play_back_mode = QMediaPlaylist.Loop
            self.playbackModeBtn.setIcon(QIcon(QPixmap(u":/images/icons/icons8-repeat-30.png")))
        elif self.play_back_mode == QMediaPlaylist.Loop:
            self.play_back_mode = QMediaPlaylist.Random
            self.playbackModeBtn.setIcon(QIcon(QPixmap(u":/images/icons/icons8-shuffle-30.png")))
        elif self.play_back_mode == QMediaPlaylist.Random:
            self.play_back_mode = QMediaPlaylist.Sequential
            self.playbackModeBtn.setIcon(QIcon(QPixmap(u":/images/icons/no-repeat-all-30.png")))
        self.playbackModeChanged.emit()