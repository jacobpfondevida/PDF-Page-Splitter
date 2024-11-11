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
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(685, 663)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 0, 641, 641))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.graphicsView = QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout.addWidget(self.graphicsView)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.currentPageLabel = QLabel(self.verticalLayoutWidget)
        self.currentPageLabel.setObjectName(u"currentPageLabel")
        self.currentPageLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.currentPageLabel)

        self.currentPageLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.currentPageLineEdit.setObjectName(u"currentPageLineEdit")
        self.currentPageLineEdit.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_5.addWidget(self.currentPageLineEdit)

        self.totalPagesLabel = QLabel(self.verticalLayoutWidget)
        self.totalPagesLabel.setObjectName(u"totalPagesLabel")

        self.horizontalLayout_5.addWidget(self.totalPagesLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.fileNameLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.fileNameLineEdit.setObjectName(u"fileNameLineEdit")

        self.horizontalLayout_2.addWidget(self.fileNameLineEdit)

        self.docTypeDropdownBox = QComboBox(self.verticalLayoutWidget)
        self.docTypeDropdownBox.addItem("")
        self.docTypeDropdownBox.addItem("")
        self.docTypeDropdownBox.addItem("")
        self.docTypeDropdownBox.addItem("")
        self.docTypeDropdownBox.addItem("")
        self.docTypeDropdownBox.addItem("")
        self.docTypeDropdownBox.addItem("")
        self.docTypeDropdownBox.addItem("")
        self.docTypeDropdownBox.addItem("")
        self.docTypeDropdownBox.setObjectName(u"docTypeDropdownBox")
        self.docTypeDropdownBox.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.docTypeDropdownBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

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

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.clearAllButton = QPushButton(self.verticalLayoutWidget)
        self.clearAllButton.setObjectName(u"clearAllButton")

        self.horizontalLayout_3.addWidget(self.clearAllButton)

        self.saveAllPagesButton = QPushButton(self.verticalLayoutWidget)
        self.saveAllPagesButton.setObjectName(u"saveAllPagesButton")

        self.horizontalLayout_3.addWidget(self.saveAllPagesButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.currentPageLabel.setText(QCoreApplication.translate("Form", u"Current Page: ", None))
        self.currentPageLineEdit.setInputMask("")
        self.totalPagesLabel.setText("")
        self.fileNameLineEdit.setText(QCoreApplication.translate("Form", u"Enter file name", None))
        self.docTypeDropdownBox.setItemText(0, QCoreApplication.translate("Form", u"Choose file type", None))
        self.docTypeDropdownBox.setItemText(1, QCoreApplication.translate("Form", u"Insurance Auth", None))
        self.docTypeDropdownBox.setItemText(2, QCoreApplication.translate("Form", u"ID", None))
        self.docTypeDropdownBox.setItemText(3, QCoreApplication.translate("Form", u"OrthoK", None))
        self.docTypeDropdownBox.setItemText(4, QCoreApplication.translate("Form", u"Outside Rx", None))
        self.docTypeDropdownBox.setItemText(5, QCoreApplication.translate("Form", u"POF Waiver", None))
        self.docTypeDropdownBox.setItemText(6, QCoreApplication.translate("Form", u"Rx Request", None))
        self.docTypeDropdownBox.setItemText(7, QCoreApplication.translate("Form", u"Referrals", None))
        self.docTypeDropdownBox.setItemText(8, QCoreApplication.translate("Form", u"Summaries", None))

        self.prevPageButton.setText(QCoreApplication.translate("Form", u"Previous Page", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"Save Page as PDF", None))
        self.nextPageButton.setText(QCoreApplication.translate("Form", u"Next Page", None))
        self.clearAllButton.setText(QCoreApplication.translate("Form", u"Clear All", None))
        self.saveAllPagesButton.setText(QCoreApplication.translate("Form", u"Save All Pages", None))
    # retranslateUi

