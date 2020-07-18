# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_dialog_ui.ui'
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


class Ui_InfoDialogUi(object):
    def setupUi(self, InfoDialogUi):
        if not InfoDialogUi.objectName():
            InfoDialogUi.setObjectName(u"InfoDialogUi")
        InfoDialogUi.resize(569, 617)
        self.verticalLayout = QVBoxLayout(InfoDialogUi)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_7 = QLabel(InfoDialogUi)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.bitrateLineEdit = QLineEdit(InfoDialogUi)
        self.bitrateLineEdit.setObjectName(u"bitrateLineEdit")
        self.bitrateLineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.bitrateLineEdit, 10, 1, 1, 1)

        self.track_totalLineEdit = QLineEdit(InfoDialogUi)
        self.track_totalLineEdit.setObjectName(u"track_totalLineEdit")
        self.track_totalLineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.track_totalLineEdit, 6, 1, 1, 1)

        self.label = QLabel(InfoDialogUi)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_13 = QLabel(InfoDialogUi)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 12, 0, 1, 1)

        self.label_10 = QLabel(InfoDialogUi)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)

        self.label_2 = QLabel(InfoDialogUi)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_8 = QLabel(InfoDialogUi)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.label_9 = QLabel(InfoDialogUi)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)

        self.filesizeLineEdit = QLineEdit(InfoDialogUi)
        self.filesizeLineEdit.setObjectName(u"filesizeLineEdit")
        self.filesizeLineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.filesizeLineEdit, 9, 1, 1, 1)

        self.pathLineEdit = QLineEdit(InfoDialogUi)
        self.pathLineEdit.setObjectName(u"pathLineEdit")
        self.pathLineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.pathLineEdit, 5, 1, 1, 1)

        self.yearLineEdit = QLineEdit(InfoDialogUi)
        self.yearLineEdit.setObjectName(u"yearLineEdit")
        self.yearLineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.yearLineEdit, 7, 1, 1, 1)

        self.label_3 = QLabel(InfoDialogUi)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.composerLineEdit = QLineEdit(InfoDialogUi)
        self.composerLineEdit.setObjectName(u"composerLineEdit")
        self.composerLineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.composerLineEdit, 8, 1, 1, 1)

        self.durationLineEdit = QLineEdit(InfoDialogUi)
        self.durationLineEdit.setObjectName(u"durationLineEdit")
        self.durationLineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.durationLineEdit, 4, 1, 1, 1)

        self.label_11 = QLabel(InfoDialogUi)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 10, 0, 1, 1)

        self.albumLineEdit = QLineEdit(InfoDialogUi)
        self.albumLineEdit.setObjectName(u"albumLineEdit")
        self.albumLineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.albumLineEdit, 1, 1, 1, 1)

        self.titleLineEdit = QLineEdit(InfoDialogUi)
        self.titleLineEdit.setObjectName(u"titleLineEdit")
        self.titleLineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.titleLineEdit, 0, 1, 1, 1)

        self.label_5 = QLabel(InfoDialogUi)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.artistLineEdit = QLineEdit(InfoDialogUi)
        self.artistLineEdit.setObjectName(u"artistLineEdit")
        self.artistLineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.artistLineEdit, 2, 1, 1, 1)

        self.label_4 = QLabel(InfoDialogUi)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_6 = QLabel(InfoDialogUi)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.genreLineEdit = QLineEdit(InfoDialogUi)
        self.genreLineEdit.setObjectName(u"genreLineEdit")
        self.genreLineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.genreLineEdit, 3, 1, 1, 1)

        self.label_12 = QLabel(InfoDialogUi)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 11, 0, 1, 1)

        self.label_14 = QLabel(InfoDialogUi)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 13, 0, 1, 1)

        self.imageLabel = QLabel(InfoDialogUi)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setScaledContents(False)
        self.imageLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.imageLabel, 13, 1, 1, 1)

        self.samplerateLineEdit = QLineEdit(InfoDialogUi)
        self.samplerateLineEdit.setObjectName(u"samplerateLineEdit")
        self.samplerateLineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.samplerateLineEdit, 11, 1, 1, 1)

        self.commentLineEdit = QLineEdit(InfoDialogUi)
        self.commentLineEdit.setObjectName(u"commentLineEdit")
        self.commentLineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.commentLineEdit, 12, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(InfoDialogUi)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(InfoDialogUi)
        self.buttonBox.accepted.connect(InfoDialogUi.accept)
        self.buttonBox.rejected.connect(InfoDialogUi.reject)

        QMetaObject.connectSlotsByName(InfoDialogUi)
    # setupUi

    def retranslateUi(self, InfoDialogUi):
        InfoDialogUi.setWindowTitle(QCoreApplication.translate("InfoDialogUi", u"Details", None))
        self.label_7.setText(QCoreApplication.translate("InfoDialogUi", u"Total tracks:", None))
        self.label.setText(QCoreApplication.translate("InfoDialogUi", u"Title:", None))
        self.label_13.setText(QCoreApplication.translate("InfoDialogUi", u"Comment:", None))
        self.label_10.setText(QCoreApplication.translate("InfoDialogUi", u"File size:", None))
        self.label_2.setText(QCoreApplication.translate("InfoDialogUi", u"Album:", None))
        self.label_8.setText(QCoreApplication.translate("InfoDialogUi", u"Year:", None))
        self.label_9.setText(QCoreApplication.translate("InfoDialogUi", u"Composer:", None))
        self.label_3.setText(QCoreApplication.translate("InfoDialogUi", u"Artist:", None))
        self.label_11.setText(QCoreApplication.translate("InfoDialogUi", u"Bitrate:", None))
        self.label_5.setText(QCoreApplication.translate("InfoDialogUi", u"Duration:", None))
        self.label_4.setText(QCoreApplication.translate("InfoDialogUi", u"Genre:", None))
        self.label_6.setText(QCoreApplication.translate("InfoDialogUi", u"Location:", None))
        self.label_12.setText(QCoreApplication.translate("InfoDialogUi", u"Sample rate:", None))
        self.label_14.setText(QCoreApplication.translate("InfoDialogUi", u"Image:", None))
        self.imageLabel.setText(QCoreApplication.translate("InfoDialogUi", u"TextLabel", None))
    # retranslateUi

