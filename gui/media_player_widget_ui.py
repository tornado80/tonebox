# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'media_player_widget_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from  . import icons_rc

class Ui_MediaPlayerWidget(object):
    def setupUi(self, MediaPlayerWidget):
        if not MediaPlayerWidget.objectName():
            MediaPlayerWidget.setObjectName(u"MediaPlayerWidget")
        MediaPlayerWidget.resize(846, 315)
        self.verticalLayout_3 = QVBoxLayout(MediaPlayerWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.coverImageLabel = QLabel(MediaPlayerWidget)
        self.coverImageLabel.setObjectName(u"coverImageLabel")
        self.coverImageLabel.setMaximumSize(QSize(100, 100))
        self.coverImageLabel.setPixmap(QPixmap(u":/images/icons/Blank_CD_icon.png"))
        self.coverImageLabel.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.coverImageLabel)

        self.infoLabel = QLabel(MediaPlayerWidget)
        self.infoLabel.setObjectName(u"infoLabel")
        self.infoLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.infoLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(MediaPlayerWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/images/icons/icons8-speed-30.png"))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.label = QLabel(MediaPlayerWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.speedSpinBox = QDoubleSpinBox(MediaPlayerWidget)
        self.speedSpinBox.setObjectName(u"speedSpinBox")
        self.speedSpinBox.setFrame(False)
        self.speedSpinBox.setAlignment(Qt.AlignCenter)
        self.speedSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.speedSpinBox.setMinimum(-10.000000000000000)
        self.speedSpinBox.setMaximum(10.000000000000000)
        self.speedSpinBox.setSingleStep(0.500000000000000)
        self.speedSpinBox.setValue(1.000000000000000)

        self.verticalLayout.addWidget(self.speedSpinBox)

        self.verticalLayout.setStretch(0, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.volumeIcon = QLabel(MediaPlayerWidget)
        self.volumeIcon.setObjectName(u"volumeIcon")
        self.volumeIcon.setPixmap(QPixmap(u":/images/icons/icons8-voice-30.png"))
        self.volumeIcon.setScaledContents(False)
        self.volumeIcon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.volumeIcon)

        self.label_2 = QLabel(MediaPlayerWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.volumeSpinBox = QSpinBox(MediaPlayerWidget)
        self.volumeSpinBox.setObjectName(u"volumeSpinBox")
        self.volumeSpinBox.setFrame(False)
        self.volumeSpinBox.setAlignment(Qt.AlignCenter)
        self.volumeSpinBox.setReadOnly(True)
        self.volumeSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.volumeSpinBox.setMaximum(100)
        self.volumeSpinBox.setValue(70)

        self.verticalLayout_2.addWidget(self.volumeSpinBox)

        self.verticalLayout_2.setStretch(0, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.volumeSlider = QSlider(MediaPlayerWidget)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setValue(70)
        self.volumeSlider.setOrientation(Qt.Vertical)
        self.volumeSlider.setTickPosition(QSlider.TicksBothSides)

        self.horizontalLayout_2.addWidget(self.volumeSlider)

        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.elapsedTimeLineEdit = QLineEdit(MediaPlayerWidget)
        self.elapsedTimeLineEdit.setObjectName(u"elapsedTimeLineEdit")
        self.elapsedTimeLineEdit.setFrame(False)
        self.elapsedTimeLineEdit.setAlignment(Qt.AlignCenter)
        self.elapsedTimeLineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.elapsedTimeLineEdit)

        self.timeSeekSlider = QSlider(MediaPlayerWidget)
        self.timeSeekSlider.setObjectName(u"timeSeekSlider")
        self.timeSeekSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.timeSeekSlider)

        self.totalTimeLineEdit = QLineEdit(MediaPlayerWidget)
        self.totalTimeLineEdit.setObjectName(u"totalTimeLineEdit")
        self.totalTimeLineEdit.setFrame(False)
        self.totalTimeLineEdit.setAlignment(Qt.AlignCenter)
        self.totalTimeLineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.totalTimeLineEdit)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.playPauseBtn = QToolButton(MediaPlayerWidget)
        self.playPauseBtn.setObjectName(u"playPauseBtn")
        icon = QIcon()
        icon.addFile(u":/images/icons/icons8-play-30.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/icons/icons8-pause-30.png", QSize(), QIcon.Normal, QIcon.On)
        self.playPauseBtn.setIcon(icon)
        self.playPauseBtn.setIconSize(QSize(30, 30))
        self.playPauseBtn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.playPauseBtn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.previousBtn = QToolButton(MediaPlayerWidget)
        self.previousBtn.setObjectName(u"previousBtn")
        icon1 = QIcon()
        icon1.addFile(u":/images/icons/icons8-skip-to-start-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.previousBtn.setIcon(icon1)
        self.previousBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.previousBtn)

        self.slowerBtn = QToolButton(MediaPlayerWidget)
        self.slowerBtn.setObjectName(u"slowerBtn")
        icon2 = QIcon()
        icon2.addFile(u":/images/icons/icons8-rewind-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.slowerBtn.setIcon(icon2)
        self.slowerBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.slowerBtn)

        self.stopBtn = QToolButton(MediaPlayerWidget)
        self.stopBtn.setObjectName(u"stopBtn")
        icon3 = QIcon()
        icon3.addFile(u":/images/icons/icons8-stop-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stopBtn.setIcon(icon3)
        self.stopBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.stopBtn)

        self.fasterBtn = QToolButton(MediaPlayerWidget)
        self.fasterBtn.setObjectName(u"fasterBtn")
        icon4 = QIcon()
        icon4.addFile(u":/images/icons/icons8-fast-forward-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fasterBtn.setIcon(icon4)
        self.fasterBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.fasterBtn)

        self.nextBtn = QToolButton(MediaPlayerWidget)
        self.nextBtn.setObjectName(u"nextBtn")
        icon5 = QIcon()
        icon5.addFile(u":/images/icons/icons8-end-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nextBtn.setIcon(icon5)
        self.nextBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.nextBtn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.back30SecBtn = QToolButton(MediaPlayerWidget)
        self.back30SecBtn.setObjectName(u"back30SecBtn")
        icon6 = QIcon()
        icon6.addFile(u":/images/icons/icons8-replay-30-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back30SecBtn.setIcon(icon6)
        self.back30SecBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.back30SecBtn)

        self.back10SecBtn = QToolButton(MediaPlayerWidget)
        self.back10SecBtn.setObjectName(u"back10SecBtn")
        icon7 = QIcon()
        icon7.addFile(u":/images/icons/icons8-replay-10-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back10SecBtn.setIcon(icon7)
        self.back10SecBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.back10SecBtn)

        self.back5SecBtn = QToolButton(MediaPlayerWidget)
        self.back5SecBtn.setObjectName(u"back5SecBtn")
        icon8 = QIcon()
        icon8.addFile(u":/images/icons/icons8-replay-5-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back5SecBtn.setIcon(icon8)
        self.back5SecBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.back5SecBtn)

        self.skip5SecBtn = QToolButton(MediaPlayerWidget)
        self.skip5SecBtn.setObjectName(u"skip5SecBtn")
        icon9 = QIcon()
        icon9.addFile(u":/images/icons/icons8-forward-5-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.skip5SecBtn.setIcon(icon9)
        self.skip5SecBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.skip5SecBtn)

        self.skip10SecBtn = QToolButton(MediaPlayerWidget)
        self.skip10SecBtn.setObjectName(u"skip10SecBtn")
        icon10 = QIcon()
        icon10.addFile(u":/images/icons/icons8-forward-10-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.skip10SecBtn.setIcon(icon10)
        self.skip10SecBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.skip10SecBtn)

        self.skip30SecBtn = QToolButton(MediaPlayerWidget)
        self.skip30SecBtn.setObjectName(u"skip30SecBtn")
        icon11 = QIcon()
        icon11.addFile(u":/images/icons/icons8-forward-30-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.skip30SecBtn.setIcon(icon11)
        self.skip30SecBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.skip30SecBtn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.playbackModeBtn = QToolButton(MediaPlayerWidget)
        self.playbackModeBtn.setObjectName(u"playbackModeBtn")
        icon12 = QIcon()
        icon12.addFile(u":/images/icons/no-repeat-all-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playbackModeBtn.setIcon(icon12)
        self.playbackModeBtn.setIconSize(QSize(30, 30))
        self.playbackModeBtn.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.playbackModeBtn)

        self.muteBtn = QToolButton(MediaPlayerWidget)
        self.muteBtn.setObjectName(u"muteBtn")
        icon13 = QIcon()
        icon13.addFile(u":/images/icons/icons8-mute-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.muteBtn.setIcon(icon13)
        self.muteBtn.setIconSize(QSize(30, 30))
        self.muteBtn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.muteBtn)

        self.horizontalLayout_3.setStretch(14, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.retranslateUi(MediaPlayerWidget)

        QMetaObject.connectSlotsByName(MediaPlayerWidget)
    # setupUi

    def retranslateUi(self, MediaPlayerWidget):
        MediaPlayerWidget.setWindowTitle(QCoreApplication.translate("MediaPlayerWidget", u"Form", None))
        self.coverImageLabel.setText("")
        self.infoLabel.setText(QCoreApplication.translate("MediaPlayerWidget", u"infoLabel", None))
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("MediaPlayerWidget", u"Speed:", None))
        self.speedSpinBox.setSuffix(QCoreApplication.translate("MediaPlayerWidget", u"x", None))
        self.volumeIcon.setText("")
        self.label_2.setText(QCoreApplication.translate("MediaPlayerWidget", u"Volume:", None))
        self.volumeSpinBox.setSuffix(QCoreApplication.translate("MediaPlayerWidget", u"%", None))
        self.playPauseBtn.setText("")
        self.previousBtn.setText(QCoreApplication.translate("MediaPlayerWidget", u"...", None))
        self.slowerBtn.setText(QCoreApplication.translate("MediaPlayerWidget", u"...", None))
        self.stopBtn.setText(QCoreApplication.translate("MediaPlayerWidget", u"...", None))
        self.fasterBtn.setText(QCoreApplication.translate("MediaPlayerWidget", u"...", None))
        self.nextBtn.setText(QCoreApplication.translate("MediaPlayerWidget", u"...", None))
        self.back30SecBtn.setText(QCoreApplication.translate("MediaPlayerWidget", u"...", None))
        self.back10SecBtn.setText(QCoreApplication.translate("MediaPlayerWidget", u"...", None))
        self.back5SecBtn.setText(QCoreApplication.translate("MediaPlayerWidget", u"...", None))
        self.skip5SecBtn.setText(QCoreApplication.translate("MediaPlayerWidget", u"...", None))
        self.skip10SecBtn.setText(QCoreApplication.translate("MediaPlayerWidget", u"...", None))
        self.skip30SecBtn.setText(QCoreApplication.translate("MediaPlayerWidget", u"...", None))
        self.playbackModeBtn.setText(QCoreApplication.translate("MediaPlayerWidget", u"...", None))
        self.muteBtn.setText(QCoreApplication.translate("MediaPlayerWidget", u"...", None))
    # retranslateUi

