# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rename_dialog_ui.ui'
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


class Ui_RenameDialogUi(object):
    def setupUi(self, RenameDialogUi):
        if not RenameDialogUi.objectName():
            RenameDialogUi.setObjectName(u"RenameDialogUi")
        RenameDialogUi.resize(453, 76)
        RenameDialogUi.setMaximumSize(QSize(16777215, 76))
        self.verticalLayout = QVBoxLayout(RenameDialogUi)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(RenameDialogUi)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(RenameDialogUi)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(RenameDialogUi)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(RenameDialogUi)
        self.buttonBox.accepted.connect(RenameDialogUi.accept)
        self.buttonBox.rejected.connect(RenameDialogUi.reject)

        QMetaObject.connectSlotsByName(RenameDialogUi)
    # setupUi

    def retranslateUi(self, RenameDialogUi):
        RenameDialogUi.setWindowTitle(QCoreApplication.translate("RenameDialogUi", u"Rename playlist", None))
        self.label.setText(QCoreApplication.translate("RenameDialogUi", u"New name:", None))
    # retranslateUi

