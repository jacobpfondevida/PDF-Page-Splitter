# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pdfProcessingWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(692, 555)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 0, 641, 521))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.graphicsView = QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout.addWidget(self.graphicsView)

        self.currentPageLabel = QLabel(self.verticalLayoutWidget)
        self.currentPageLabel.setObjectName(u"currentPageLabel")

        self.verticalLayout.addWidget(self.currentPageLabel)

        self.fileNameLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.fileNameLineEdit.setObjectName(u"fileNameLineEdit")

        self.verticalLayout.addWidget(self.fileNameLineEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.prevPageButton = QPushButton(self.verticalLayoutWidget)
        self.prevPageButton.setObjectName(u"prevPageButton")

        self.horizontalLayout.addWidget(self.prevPageButton)

        self.saveButton = QPushButton(self.verticalLayoutWidget)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout.addWidget(self.saveButton)

        self.nextPageButton = QPushButton(self.verticalLayoutWidget)
        self.nextPageButton.setObjectName(u"nextPageButton")

        self.horizontalLayout.addWidget(self.nextPageButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.currentPageLabel.setText("")
        self.fileNameLineEdit.setText(QCoreApplication.translate("Form", u"Enter file name", None))
        self.prevPageButton.setText(QCoreApplication.translate("Form", u"Previous Page", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"Save Page as PDF", None))
        self.nextPageButton.setText(QCoreApplication.translate("Form", u"Next Page", None))
    # retranslateUi
