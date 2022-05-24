# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'searchTmXMVN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Search(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 300)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
" border-image: url(:/pic/background.png);\n"
"background-color: #ffede0;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 512, 61))
        font = QFont()
        font.setFamily(u"SVN-Georgia")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setFocusPolicy(Qt.WheelFocus)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 80, 301, 41))
        font1 = QFont()
        font1.setFamily(u"SVN-Georgia")
        font1.setPointSize(11)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 140, 381, 21))
        font2 = QFont()
        font2.setFamily(u"SVN-Georgia")
        font2.setPointSize(12)
        self.label_3.setFont(font2)
        self.txt_search = QLineEdit(self.centralwidget)
        self.txt_search.setObjectName(u"txt_search")
        self.txt_search.setEnabled(True)
        self.txt_search.setGeometry(QRect(80, 170, 441, 31))
        self.txt_search.setAutoFillBackground(False)
        self.txt_search.setStyleSheet(u"")
        self.txt_search.setReadOnly(False)
        self.txt_search.setClearButtonEnabled(False)
        self.btn_search = QPushButton(self.centralwidget)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setGeometry(QRect(230, 220, 121, 31))
        icon = QIcon()
        icon.addFile(u":/icon/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon)
        self.btn_search.setIconSize(QSize(15, 15))
        MainWindow.setCentralWidget(self.centralwidget)
        self.txt_search.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.btn_search.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#e67747;\">TRA C\u1ee8U</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#3a8ee6;\">Tra c\u1ee9u th\u00f4ng tin ti\u00eam v\u1eafc xin</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#3a8ee6;\">Vui l\u00f2ng nh\u1eadp s\u1ed1 CCCD/CMND \u0111\u1ec3 tra c\u1ee9u</span></p></body></html>", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u" Tra c\u1ee9u", None))
    # retranslateUi

