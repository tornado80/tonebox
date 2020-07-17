# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog_ui.ui'
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


class Ui_SettingsDialogUi(object):
    def setupUi(self, SettingsDialogUi):
        if not SettingsDialogUi.objectName():
            SettingsDialogUi.setObjectName(u"SettingsDialogUi")
        SettingsDialogUi.resize(603, 557)
        self.verticalLayout = QVBoxLayout(SettingsDialogUi)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(SettingsDialogUi)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_5 = QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_7)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)

        self.defaultPathLineEdit = QLineEdit(self.tab)
        self.defaultPathLineEdit.setObjectName(u"defaultPathLineEdit")
        self.defaultPathLineEdit.setReadOnly(True)

        self.gridLayout_4.addWidget(self.defaultPathLineEdit, 0, 1, 1, 1)

        self.defaultPathButton = QToolButton(self.tab)
        self.defaultPathButton.setObjectName(u"defaultPathButton")

        self.gridLayout_4.addWidget(self.defaultPathButton, 0, 2, 1, 1)

        self.rememberCheckBox = QCheckBox(self.tab)
        self.rememberCheckBox.setObjectName(u"rememberCheckBox")

        self.gridLayout_4.addWidget(self.rememberCheckBox, 1, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 2, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.resetDefaultPathButton = QPushButton(self.tab)
        self.resetDefaultPathButton.setObjectName(u"resetDefaultPathButton")

        self.horizontalLayout_2.addWidget(self.resetDefaultPathButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.verticalLayout_5.setStretch(1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_3)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.databasePathButton = QToolButton(self.tab_2)
        self.databasePathButton.setObjectName(u"databasePathButton")

        self.gridLayout_3.addWidget(self.databasePathButton, 0, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.databasePathLineEdit = QLineEdit(self.tab_2)
        self.databasePathLineEdit.setObjectName(u"databasePathLineEdit")
        self.databasePathLineEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.databasePathLineEdit, 0, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.resetDatabasePathButton = QPushButton(self.tab_2)
        self.resetDatabasePathButton.setObjectName(u"resetDatabasePathButton")

        self.horizontalLayout.addWidget(self.resetDatabasePathButton)

        self.reloadDatabaseButton = QPushButton(self.tab_2)
        self.reloadDatabaseButton.setObjectName(u"reloadDatabaseButton")

        self.horizontalLayout.addWidget(self.reloadDatabaseButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_2 = QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.resetHeadersButton = QPushButton(self.tab_3)
        self.resetHeadersButton.setObjectName(u"resetHeadersButton")

        self.gridLayout.addWidget(self.resetHeadersButton, 2, 4, 1, 1)

        self.composerCheckBox = QCheckBox(self.tab_3)
        self.composerCheckBox.setObjectName(u"composerCheckBox")

        self.gridLayout.addWidget(self.composerCheckBox, 1, 3, 1, 1)

        self.track_totalCheckBox = QCheckBox(self.tab_3)
        self.track_totalCheckBox.setObjectName(u"track_totalCheckBox")

        self.gridLayout.addWidget(self.track_totalCheckBox, 1, 1, 1, 1)

        self.genreCheckBox = QCheckBox(self.tab_3)
        self.genreCheckBox.setObjectName(u"genreCheckBox")
        self.genreCheckBox.setChecked(True)

        self.gridLayout.addWidget(self.genreCheckBox, 0, 3, 1, 1)

        self.commentCheckBox = QCheckBox(self.tab_3)
        self.commentCheckBox.setObjectName(u"commentCheckBox")

        self.gridLayout.addWidget(self.commentCheckBox, 2, 2, 1, 1)

        self.filesizeCheckBox = QCheckBox(self.tab_3)
        self.filesizeCheckBox.setObjectName(u"filesizeCheckBox")

        self.gridLayout.addWidget(self.filesizeCheckBox, 1, 4, 1, 1)

        self.titleCheckBox = QCheckBox(self.tab_3)
        self.titleCheckBox.setObjectName(u"titleCheckBox")
        self.titleCheckBox.setChecked(True)

        self.gridLayout.addWidget(self.titleCheckBox, 0, 0, 1, 1)

        self.albumCheckBox = QCheckBox(self.tab_3)
        self.albumCheckBox.setObjectName(u"albumCheckBox")
        self.albumCheckBox.setChecked(True)

        self.gridLayout.addWidget(self.albumCheckBox, 0, 1, 1, 1)

        self.imageCheckBox = QCheckBox(self.tab_3)
        self.imageCheckBox.setObjectName(u"imageCheckBox")

        self.gridLayout.addWidget(self.imageCheckBox, 2, 3, 1, 1)

        self.artistCheckBox = QCheckBox(self.tab_3)
        self.artistCheckBox.setObjectName(u"artistCheckBox")
        self.artistCheckBox.setChecked(True)

        self.gridLayout.addWidget(self.artistCheckBox, 0, 2, 1, 1)

        self.samplerateCheckBox = QCheckBox(self.tab_3)
        self.samplerateCheckBox.setObjectName(u"samplerateCheckBox")

        self.gridLayout.addWidget(self.samplerateCheckBox, 2, 1, 1, 1)

        self.pathCheckBox = QCheckBox(self.tab_3)
        self.pathCheckBox.setObjectName(u"pathCheckBox")
        self.pathCheckBox.setChecked(True)

        self.gridLayout.addWidget(self.pathCheckBox, 1, 0, 1, 1)

        self.durationCheckBox = QCheckBox(self.tab_3)
        self.durationCheckBox.setObjectName(u"durationCheckBox")
        self.durationCheckBox.setChecked(True)

        self.gridLayout.addWidget(self.durationCheckBox, 0, 4, 1, 1)

        self.bitrateCheckBox = QCheckBox(self.tab_3)
        self.bitrateCheckBox.setObjectName(u"bitrateCheckBox")

        self.gridLayout.addWidget(self.bitrateCheckBox, 2, 0, 1, 1)

        self.yearCheckBox = QCheckBox(self.tab_3)
        self.yearCheckBox.setObjectName(u"yearCheckBox")
        self.yearCheckBox.setChecked(True)

        self.gridLayout.addWidget(self.yearCheckBox, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout_2.setStretch(1, 1)
        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.reloadSettingsButton = QPushButton(SettingsDialogUi)
        self.reloadSettingsButton.setObjectName(u"reloadSettingsButton")

        self.verticalLayout.addWidget(self.reloadSettingsButton)

        self.buttonBox = QDialogButtonBox(SettingsDialogUi)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(SettingsDialogUi)
        self.buttonBox.accepted.connect(SettingsDialogUi.accept)
        self.buttonBox.rejected.connect(SettingsDialogUi.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SettingsDialogUi)
    # setupUi

    def retranslateUi(self, SettingsDialogUi):
        SettingsDialogUi.setWindowTitle(QCoreApplication.translate("SettingsDialogUi", u"Settings", None))
        self.label_7.setText(QCoreApplication.translate("SettingsDialogUi", u"You can choose the option that app remember last chosen path or to set a default path.", None))
        self.label_8.setText(QCoreApplication.translate("SettingsDialogUi", u"Default path:", None))
        self.defaultPathButton.setText(QCoreApplication.translate("SettingsDialogUi", u"...", None))
        self.rememberCheckBox.setText(QCoreApplication.translate("SettingsDialogUi", u"Remember last path", None))
        self.resetDefaultPathButton.setText(QCoreApplication.translate("SettingsDialogUi", u"Reset to defaults", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("SettingsDialogUi", u"Open File Path", None))
        self.label_3.setText(QCoreApplication.translate("SettingsDialogUi", u"Note that you must hit Reload Database in order that following action will affect data, otherwise it will be postponed till next session.", None))
        self.label_2.setText(QCoreApplication.translate("SettingsDialogUi", u"Database path:", None))
        self.databasePathButton.setText(QCoreApplication.translate("SettingsDialogUi", u"...", None))
        self.resetDatabasePathButton.setText(QCoreApplication.translate("SettingsDialogUi", u"Reset to default", None))
        self.reloadDatabaseButton.setText(QCoreApplication.translate("SettingsDialogUi", u"Reload database", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("SettingsDialogUi", u"Database Path", None))
        self.label.setText(QCoreApplication.translate("SettingsDialogUi", u"Here you can choose which headers to be seen in songs views.", None))
        self.resetHeadersButton.setText(QCoreApplication.translate("SettingsDialogUi", u"Reset to defaults", None))
        self.composerCheckBox.setText(QCoreApplication.translate("SettingsDialogUi", u"Composer", None))
        self.track_totalCheckBox.setText(QCoreApplication.translate("SettingsDialogUi", u"Total tracks", None))
        self.genreCheckBox.setText(QCoreApplication.translate("SettingsDialogUi", u"Genre", None))
        self.commentCheckBox.setText(QCoreApplication.translate("SettingsDialogUi", u"Comment", None))
        self.filesizeCheckBox.setText(QCoreApplication.translate("SettingsDialogUi", u"File size", None))
        self.titleCheckBox.setText(QCoreApplication.translate("SettingsDialogUi", u"Title", None))
        self.albumCheckBox.setText(QCoreApplication.translate("SettingsDialogUi", u"Album", None))
        self.imageCheckBox.setText(QCoreApplication.translate("SettingsDialogUi", u"Image", None))
        self.artistCheckBox.setText(QCoreApplication.translate("SettingsDialogUi", u"Artist", None))
        self.samplerateCheckBox.setText(QCoreApplication.translate("SettingsDialogUi", u"Sample rate", None))
        self.pathCheckBox.setText(QCoreApplication.translate("SettingsDialogUi", u"Location", None))
        self.durationCheckBox.setText(QCoreApplication.translate("SettingsDialogUi", u"Duration", None))
        self.bitrateCheckBox.setText(QCoreApplication.translate("SettingsDialogUi", u"Bitrate", None))
        self.yearCheckBox.setText(QCoreApplication.translate("SettingsDialogUi", u"Year", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("SettingsDialogUi", u"Songs View Headers", None))
        self.reloadSettingsButton.setText(QCoreApplication.translate("SettingsDialogUi", u"Reload Settings", None))
    # retranslateUi

