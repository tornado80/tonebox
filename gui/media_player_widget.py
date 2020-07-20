from PySide2.QtMultimedia import QMediaPlaylist
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QIcon, QPixmap
from .media_player_widget_ui import Ui_MediaPlayerWidget
from PySide2.QtCore import Signal

class MediaPlayerWidget(QWidget, Ui_MediaPlayerWidget):
    speedChanged = Signal(float)
    volumeChanged = Signal(int)
    positionChanged = Signal(int)
    muteChanged = Signal(bool)
    playbackModeChanged = Signal()
    trackPlayed = Signal()
    trackPaused = Signal()
    stopTrackRequested = Signal()
    nextTrackRequested = Signal()
    previousTrackRequested = Signal()
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.volumeSlider.valueChanged.connect(self.handle_volume_slider)
        self.playbackModeBtn.clicked.connect(self.handle_playback_btn)
        self.speedSpinBox.valueChanged.connect(self.handle_speed_spinbox)
        self.muteBtn.clicked.connect(self.handle_mute_btn)
        self.playPauseBtn.clicked.connect(self.handle_play_pause_btn)
        self.stopBtn.clicked.connect(self.handle_stop_btn)
        self.nextBtn.clicked.connect(self.handle_next_btn)
        self.fasterBtn.clicked.connect(self.handle_faster_btn)
        self.slowerBtn.clicked.connect(self.handle_slower_btn)
        self.previousBtn.clicked.connect(self.handle_previous_btn)
        self.timeSeekSlider.sliderPressed.connect(self.started_to_change_position)
        self.timeSeekSlider.sliderReleased.connect(self.finished_changing_position)
        self.play_back_mode = QMediaPlaylist.Sequential
        self.playbackModeChanged.emit()
        self.position_changing_state = False

    def handle_faster_btn(self):
        self.speedSpinBox.setValue(self.speedSpinBox.value() + 0.5)

    def handle_slower_btn(self):
        self.speedSpinBox.setValue(self.speedSpinBox.value() - 0.5)

    def handle_speed_spinbox(self):
        self.speedChanged.emit(self.speedSpinBox.value())

    def handle_mute_btn(self):
        self.muteChanged.emit(self.muteBtn.isChecked())

    def handle_next_btn(self):
        self.nextTrackRequested.emit()

    def handle_previous_btn(self):
        self.previousTrackRequested.emit()
    
    def handle_stop_btn(self):
        self.stopTrackRequested.emit()

    def started_to_change_position(self):
        self.position_changing_state = True
    
    def finished_changing_position(self):
        self.position_changing_state = False
        self.positionChanged.emit(self.timeSeekSlider.value())

    def handle_play_pause_btn(self):
        if self.playPauseBtn.isChecked():
            self.trackPlayed.emit()
        else:
            self.trackPaused.emit()

    def handle_volume_slider(self):
        self.volumeSpinBox.setValue(self.volumeSlider.value())
        if self.volumeSlider.value() == 0:
            self.volumeIcon.setPixmap(QPixmap(u":/images/icons/icons8-no-audio-30.png"))
        elif self.volumeSlider.value() < 40:
            self.volumeIcon.setPixmap(QPixmap(u":/images/icons/icons8-low-volume-30.png"))
        elif self.volumeSlider.value() < 80:
            self.volumeIcon.setPixmap(QPixmap(u":/images/icons/icons8-voice-30.png"))
        else:
            self.volumeIcon.setPixmap(QPixmap(u":/images/icons/icons8-audio-30.png"))
        self.volumeChanged.emit(self.volumeSpinBox.value())

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
            self.play_back_mode = QMediaPlaylist.Sequential
            self.playbackModeBtn.setIcon(QIcon(QPixmap(u":/images/icons/no-repeat-all-30.png")))
        self.playbackModeChanged.emit()