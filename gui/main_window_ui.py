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
from .views import PlaylistFilterView
from .views import PlaylistSongsView

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
        self.verticalLayout_7 = QVBoxLayout(self.artistsTab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.splitter_2 = QSplitter(self.artistsTab)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.artistFilterView = FilterView(self.splitter_2)
        self.artistFilterView.setObjectName(u"artistFilterView")
        self.splitter_2.addWidget(self.artistFilterView)
        self.artistSongsView = SongsView(self.splitter_2)
        self.artistSongsView.setObjectName(u"artistSongsView")
        self.splitter_2.addWidget(self.artistSongsView)

        self.verticalLayout_7.addWidget(self.splitter_2)

        self.categoryWidget.addTab(self.artistsTab, "")
        self.genresTab = QWidget()
        self.genresTab.setObjectName(u"genresTab")
        self.verticalLayout_8 = QVBoxLayout(self.genresTab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.splitter_3 = QSplitter(self.genresTab)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Vertical)
        self.genreFilterView = FilterView(self.splitter_3)
        self.genreFilterView.setObjectName(u"genreFilterView")
        self.splitter_3.addWidget(self.genreFilterView)
        self.genreSongsView = SongsView(self.splitter_3)
        self.genreSongsView.setObjectName(u"genreSongsView")
        self.splitter_3.addWidget(self.genreSongsView)

        self.verticalLayout_8.addWidget(self.splitter_3)

        self.categoryWidget.addTab(self.genresTab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_13 = QVBoxLayout(self.tab)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.splitter_6 = QSplitter(self.tab)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setOrientation(Qt.Vertical)
        self.splitter_5 = QSplitter(self.splitter_6)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter_5)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_10 = QVBoxLayout(self.widget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_10.addWidget(self.label_2)

        self.multiGenre = FilterView(self.widget)
        self.multiGenre.setObjectName(u"multiGenre")

        self.verticalLayout_10.addWidget(self.multiGenre)

        self.splitter_5.addWidget(self.widget)
        self.widget1 = QWidget(self.splitter_5)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout_11 = QVBoxLayout(self.widget1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_11.addWidget(self.label_3)

        self.multiArtist = FilterView(self.widget1)
        self.multiArtist.setObjectName(u"multiArtist")

        self.verticalLayout_11.addWidget(self.multiArtist)

        self.splitter_5.addWidget(self.widget1)
        self.widget2 = QWidget(self.splitter_5)
        self.widget2.setObjectName(u"widget2")
        self.verticalLayout_12 = QVBoxLayout(self.widget2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_12.addWidget(self.label_4)

        self.multiAlbum = FilterView(self.widget2)
        self.multiAlbum.setObjectName(u"multiAlbum")

        self.verticalLayout_12.addWidget(self.multiAlbum)

        self.splitter_5.addWidget(self.widget2)
        self.splitter_6.addWidget(self.splitter_5)
        self.multiSongs = SongsView(self.splitter_6)
        self.multiSongs.setObjectName(u"multiSongs")
        self.splitter_6.addWidget(self.multiSongs)

        self.verticalLayout_13.addWidget(self.splitter_6)

        self.categoryWidget.addTab(self.tab, "")
        self.playlistsTab = QWidget()
        self.playlistsTab.setObjectName(u"playlistsTab")
        self.verticalLayout_9 = QVBoxLayout(self.playlistsTab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.splitter_4 = QSplitter(self.playlistsTab)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Vertical)
        self.playlistFilterView = PlaylistFilterView(self.splitter_4)
        self.playlistFilterView.setObjectName(u"playlistFilterView")
        self.splitter_4.addWidget(self.playlistFilterView)
        self.playlistSongsView = PlaylistSongsView(self.splitter_4)
        self.playlistSongsView.setObjectName(u"playlistSongsView")
        self.splitter_4.addWidget(self.playlistSongsView)

        self.verticalLayout_9.addWidget(self.splitter_4)

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
        self.label_2.setText(QCoreApplication.translate("MainWindowUi", u"Genres:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindowUi", u"Artists:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindowUi", u"Albums:", None))
        self.categoryWidget.setTabText(self.categoryWidget.indexOf(self.tab), QCoreApplication.translate("MainWindowUi", u"Multi", None))
        self.categoryWidget.setTabText(self.categoryWidget.indexOf(self.playlistsTab), QCoreApplication.translate("MainWindowUi", u"Playlists", None))
        self.label.setText(QCoreApplication.translate("MainWindowUi", u"Playing Queue:", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindowUi", u"toolBar", None))
    # retranslateUi

