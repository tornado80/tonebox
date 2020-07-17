# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_ui.ui'
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

from .media_player_widget import MediaPlayerWidget
from .queue_widget import QueueWidget
from .views import SongsView
from .views import FilterView

from  . import icons_rc

class Ui_MainWindowUi(object):
    def setupUi(self, MainWindowUi):
        if not MainWindowUi.objectName():
            MainWindowUi.setObjectName(u"MainWindowUi")
        MainWindowUi.resize(920, 737)
        self.actionAddMusic = QAction(MainWindowUi)
        self.actionAddMusic.setObjectName(u"actionAddMusic")
        icon = QIcon()
        icon.addFile(u":/images/icons/music_add-512.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAddMusic.setIcon(icon)
        self.actionNewPlaylist = QAction(MainWindowUi)
        self.actionNewPlaylist.setObjectName(u"actionNewPlaylist")
        icon1 = QIcon()
        icon1.addFile(u":/images/icons/icons8-lounge-music-playlist-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNewPlaylist.setIcon(icon1)
        self.actionSettings = QAction(MainWindowUi)
        self.actionSettings.setObjectName(u"actionSettings")
        icon2 = QIcon()
        icon2.addFile(u":/images/icons/settings-512.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSettings.setIcon(icon2)
        self.actionAddDirectory = QAction(MainWindowUi)
        self.actionAddDirectory.setObjectName(u"actionAddDirectory")
        icon3 = QIcon()
        icon3.addFile(u":/images/icons/icons8-opened-folder-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAddDirectory.setIcon(icon3)
        self.centralwidget = QWidget(MainWindowUi)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.playerSplitter = QSplitter(self.centralwidget)
        self.playerSplitter.setObjectName(u"playerSplitter")
        self.playerSplitter.setOrientation(Qt.Vertical)
        self.queueSplitter = QSplitter(self.playerSplitter)
        self.queueSplitter.setObjectName(u"queueSplitter")
        self.queueSplitter.setOrientation(Qt.Horizontal)
        self.frame_3 = QFrame(self.queueSplitter)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.categoryWidget = QTabWidget(self.frame_3)
        self.categoryWidget.setObjectName(u"categoryWidget")
        self.categoryWidget.setTabPosition(QTabWidget.North)
        self.categoryWidget.setTabShape(QTabWidget.Triangular)
        self.libraryTab = QWidget()
        self.libraryTab.setObjectName(u"libraryTab")
        self.verticalLayout_5 = QVBoxLayout(self.libraryTab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.librarySongsView = SongsView(self.libraryTab)
        self.librarySongsView.setObjectName(u"librarySongsView")

        self.verticalLayout_5.addWidget(self.librarySongsView)

        self.categoryWidget.addTab(self.libraryTab, "")
        self.albumsTab = QWidget()
        self.albumsTab.setObjectName(u"albumsTab")
        self.verticalLayout_6 = QVBoxLayout(self.albumsTab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.splitter = QSplitter(self.albumsTab)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.albumFilterView = FilterView(self.splitter)
        self.albumFilterView.setObjectName(u"albumFilterView")
        self.splitter.addWidget(self.albumFilterView)
        self.albumSongsView = SongsView(self.splitter)
        self.albumSongsView.setObjectName(u"albumSongsView")
        self.splitter.addWidget(self.albumSongsView)

        self.verticalLayout_6.addWidget(self.splitter)

        self.categoryWidget.addTab(self.albumsTab, "")
        self.artistsTab = QWidget()
        self.artistsTab.setObjectName(u"artistsTab")
        self.categoryWidget.addTab(self.artistsTab, "")
        self.genresTab = QWidget()
        self.genresTab.setObjectName(u"genresTab")
        self.categoryWidget.addTab(self.genresTab, "")
        self.playlistsTab = QWidget()
        self.playlistsTab.setObjectName(u"playlistsTab")
        self.categoryWidget.addTab(self.playlistsTab, "")

        self.verticalLayout.addWidget(self.categoryWidget)

        self.queueSplitter.addWidget(self.frame_3)
        self.frame = QFrame(self.queueSplitter)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.queueWidget = QueueWidget(self.frame)
        self.queueWidget.setObjectName(u"queueWidget")

        self.verticalLayout_4.addWidget(self.queueWidget)

        self.verticalLayout_4.setStretch(1, 1)
        self.queueSplitter.addWidget(self.frame)
        self.playerSplitter.addWidget(self.queueSplitter)
        self.frame_2 = QFrame(self.playerSplitter)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.playerWidget = MediaPlayerWidget(self.frame_2)
        self.playerWidget.setObjectName(u"playerWidget")

        self.verticalLayout_3.addWidget(self.playerWidget)

        self.playerSplitter.addWidget(self.frame_2)

        self.verticalLayout_2.addWidget(self.playerSplitter)

        MainWindowUi.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindowUi)
        self.statusbar.setObjectName(u"statusbar")
        MainWindowUi.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindowUi)
        self.toolBar.setObjectName(u"toolBar")
        MainWindowUi.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionAddMusic)
        self.toolBar.addAction(self.actionNewPlaylist)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSettings)

        self.retranslateUi(MainWindowUi)

        self.categoryWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindowUi)
    # setupUi

    def retranslateUi(self, MainWindowUi):
        MainWindowUi.setWindowTitle(QCoreApplication.translate("MainWindowUi", u"Tone Box", None))
        self.actionAddMusic.setText(QCoreApplication.translate("MainWindowUi", u"Add Music(s)", None))
        self.actionNewPlaylist.setText(QCoreApplication.translate("MainWindowUi", u"New Playlist", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindowUi", u"Settings", None))
        self.actionAddDirectory.setText(QCoreApplication.translate("MainWindowUi", u"Add Directory", None))
        self.categoryWidget.setTabText(self.categoryWidget.indexOf(self.libraryTab), QCoreApplication.translate("MainWindowUi", u"Library", None))
        self.categoryWidget.setTabText(self.categoryWidget.indexOf(self.albumsTab), QCoreApplication.translate("MainWindowUi", u"Albums", None))
        self.categoryWidget.setTabText(self.categoryWidget.indexOf(self.artistsTab), QCoreApplication.translate("MainWindowUi", u"Artists", None))
        self.categoryWidget.setTabText(self.categoryWidget.indexOf(self.genresTab), QCoreApplication.translate("MainWindowUi", u"Genres", None))
        self.categoryWidget.setTabText(self.categoryWidget.indexOf(self.playlistsTab), QCoreApplication.translate("MainWindowUi", u"Playlists", None))
        self.label.setText(QCoreApplication.translate("MainWindowUi", u"Playing Queue:", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindowUi", u"toolBar", None))
    # retranslateUi

