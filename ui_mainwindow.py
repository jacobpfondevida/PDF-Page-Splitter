# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(713, 164)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 0, 671, 141))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_2.addWidget(self.textBrowser)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.outputFolderButton = QPushButton(self.verticalLayoutWidget)
        self.outputFolderButton.setObjectName(u"outputFolderButton")

        self.gridLayout.addWidget(self.outputFolderButton, 2, 1, 1, 1)

        self.inputFileLabel = QLabel(self.verticalLayoutWidget)
        self.inputFileLabel.setObjectName(u"inputFileLabel")

        self.gridLayout.addWidget(self.inputFileLabel, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.clearAllButton = QPushButton(self.verticalLayoutWidget)
        self.clearAllButton.setObjectName(u"clearAllButton")

        self.verticalLayout.addWidget(self.clearAllButton)


        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)

        self.outputFolderLabel = QLabel(self.verticalLayoutWidget)
        self.outputFolderLabel.setObjectName(u"outputFolderLabel")

        self.gridLayout.addWidget(self.outputFolderLabel, 1, 1, 1, 1)

        self.inputFileButton = QPushButton(self.verticalLayoutWidget)
        self.inputFileButton.setObjectName(u"inputFileButton")

        self.gridLayout.addWidget(self.inputFileButton, 2, 0, 1, 1)

        self.proceedToProcessButton = QPushButton(self.verticalLayoutWidget)
        self.proceedToProcessButton.setObjectName(u"proceedToProcessButton")

        self.gridLayout.addWidget(self.proceedToProcessButton, 3, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PDF Page Splitter", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select the file you want to split by pages.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This program will save each individual page as its own PDF.</p></body></html>", None))
        self.outputFolderButton.setText(QCoreApplication.translate("MainWindow", u"Choose Output Destination", None))
        self.inputFileLabel.setText(QCoreApplication.translate("MainWindow", u"No file selected.", None))
        self.clearAllButton.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
        self.outputFolderLabel.setText(QCoreApplication.translate("MainWindow", u"No output destination folder selected.", None))
        self.inputFileButton.setText(QCoreApplication.translate("MainWindow", u"Choose Input File", None))
        self.proceedToProcessButton.setText(QCoreApplication.translate("MainWindow", u"Proceed to Labelling", None))
    # retranslateUi

