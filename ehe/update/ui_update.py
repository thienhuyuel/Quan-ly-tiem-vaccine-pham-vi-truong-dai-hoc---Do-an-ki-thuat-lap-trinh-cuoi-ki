# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'updateDFLbPi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Update(object):
    def setupUi(self, Ui_Update):
        if not Ui_Update.objectName():
            Ui_Update.setObjectName(u"Ui_Update")
        Ui_Update.resize(1202, 591)
        Ui_Update.setStyleSheet(u"* {\n"
"background-color: #ffede0\n"
"}")
        self.window = QWidget(Ui_Update)
        self.window.setObjectName(u"window")
        self.verticalLayout = QVBoxLayout(self.window)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lable_frame = QWidget(self.window)
        self.lable_frame.setObjectName(u"lable_frame")
        self.verticalLayout_2 = QVBoxLayout(self.lable_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Title_lable = QLabel(self.lable_frame)
        self.Title_lable.setObjectName(u"Title_lable")
        font = QFont()
        font.setFamily(u"#9Slide03 Montserrat Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Title_lable.setFont(font)

        self.verticalLayout_2.addWidget(self.Title_lable)


        self.verticalLayout.addWidget(self.lable_frame, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.mainFrame = QWidget(self.window)
        self.mainFrame.setObjectName(u"mainFrame")
        self.verticalLayout_3 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_3.setSpacing(35)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 30, 0, 15)
        self.titleFrame = QFrame(self.mainFrame)
        self.titleFrame.setObjectName(u"titleFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleFrame.sizePolicy().hasHeightForWidth())
        self.titleFrame.setSizePolicy(sizePolicy)
        self.titleFrame.setFrameShape(QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.titleFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 5, 0, 0)
        self.Left_lable = QLabel(self.titleFrame)
        self.Left_lable.setObjectName(u"Left_lable")
        font1 = QFont()
        font1.setFamily(u"#9Slide03 Montserrat Medium")
        font1.setPointSize(12)
        self.Left_lable.setFont(font1)

        self.verticalLayout_4.addWidget(self.Left_lable)


        self.verticalLayout_3.addWidget(self.titleFrame)

        self.btnFrame = QFrame(self.mainFrame)
        self.btnFrame.setObjectName(u"btnFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnFrame.sizePolicy().hasHeightForWidth())
        self.btnFrame.setSizePolicy(sizePolicy1)
        self.btnFrame.setFrameShape(QFrame.NoFrame)
        self.btnFrame.setFrameShadow(QFrame.Raised)
        self.btnFrame.setLineWidth(1)
        self.btnFrame.setMidLineWidth(1)
        self.horizontalLayout_2 = QHBoxLayout(self.btnFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.card1 = QFrame(self.btnFrame)
        self.card1.setObjectName(u"card1")
        self.card1.setFrameShape(QFrame.StyledPanel)
        self.card1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.card1)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 10)
        self.btn1 = QWidget(self.card1)
        self.btn1.setObjectName(u"btn1")
        self.verticalLayout_8 = QVBoxLayout(self.btn1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lb1 = QLabel(self.btn1)
        self.lb1.setObjectName(u"lb1")

        self.verticalLayout_8.addWidget(self.lb1)

        self.txt_name = QLineEdit(self.btn1)
        self.txt_name.setObjectName(u"txt_name")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.txt_name.sizePolicy().hasHeightForWidth())
        self.txt_name.setSizePolicy(sizePolicy2)

        self.verticalLayout_8.addWidget(self.txt_name)


        self.verticalLayout_5.addWidget(self.btn1)

        self.btn2 = QWidget(self.card1)
        self.btn2.setObjectName(u"btn2")
        self.verticalLayout_9 = QVBoxLayout(self.btn2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lb2 = QLabel(self.btn2)
        self.lb2.setObjectName(u"lb2")

        self.verticalLayout_9.addWidget(self.lb2)

        self.txt_id = QLineEdit(self.btn2)
        self.txt_id.setObjectName(u"txt_id")

        self.verticalLayout_9.addWidget(self.txt_id)


        self.verticalLayout_5.addWidget(self.btn2)

        self.btn3 = QWidget(self.card1)
        self.btn3.setObjectName(u"btn3")
        self.verticalLayout_10 = QVBoxLayout(self.btn3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lb3 = QLabel(self.btn3)
        self.lb3.setObjectName(u"lb3")

        self.verticalLayout_10.addWidget(self.lb3)

        self.cbb_inject1 = QComboBox(self.btn3)
        self.cbb_inject1.setObjectName(u"cbb_inject1")

        self.verticalLayout_10.addWidget(self.cbb_inject1)


        self.verticalLayout_5.addWidget(self.btn3)


        self.horizontalLayout_2.addWidget(self.card1)

        self.card2 = QFrame(self.btnFrame)
        self.card2.setObjectName(u"card2")
        self.card2.setFrameShape(QFrame.StyledPanel)
        self.card2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.card2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 10, 0, 10)
        self.btn4 = QWidget(self.card2)
        self.btn4.setObjectName(u"btn4")
        self.verticalLayout_11 = QVBoxLayout(self.btn4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.lb4 = QLabel(self.btn4)
        self.lb4.setObjectName(u"lb4")

        self.verticalLayout_11.addWidget(self.lb4)

        self.txt_birthday = QDateEdit(self.btn4)
        self.txt_birthday.setObjectName(u"txt_birthday")

        self.verticalLayout_11.addWidget(self.txt_birthday)


        self.verticalLayout_6.addWidget(self.btn4)

        self.btn5 = QWidget(self.card2)
        self.btn5.setObjectName(u"btn5")
        self.verticalLayout_12 = QVBoxLayout(self.btn5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lb5 = QLabel(self.btn5)
        self.lb5.setObjectName(u"lb5")

        self.verticalLayout_12.addWidget(self.lb5)

        self.txt_phone = QLineEdit(self.btn5)
        self.txt_phone.setObjectName(u"txt_phone")

        self.verticalLayout_12.addWidget(self.txt_phone)


        self.verticalLayout_6.addWidget(self.btn5)

        self.btn6 = QWidget(self.card2)
        self.btn6.setObjectName(u"btn6")
        self.verticalLayout_13 = QVBoxLayout(self.btn6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.lb6 = QLabel(self.btn6)
        self.lb6.setObjectName(u"lb6")

        self.verticalLayout_13.addWidget(self.lb6)

        self.cbb_inject2 = QComboBox(self.btn6)
        self.cbb_inject2.setObjectName(u"cbb_inject2")

        self.verticalLayout_13.addWidget(self.cbb_inject2)


        self.verticalLayout_6.addWidget(self.btn6)


        self.horizontalLayout_2.addWidget(self.card2)

        self.card3 = QFrame(self.btnFrame)
        self.card3.setObjectName(u"card3")
        self.card3.setFrameShape(QFrame.StyledPanel)
        self.card3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.card3)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 10, 0, 10)
        self.btn7 = QWidget(self.card3)
        self.btn7.setObjectName(u"btn7")
        self.horizontalLayout_3 = QHBoxLayout(self.btn7)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 0, -1, 0)
        self.lb7 = QLabel(self.btn7)
        self.lb7.setObjectName(u"lb7")

        self.horizontalLayout_3.addWidget(self.lb7)

        self.rd_male = QRadioButton(self.btn7)
        self.rd_male.setObjectName(u"rd_male")

        self.horizontalLayout_3.addWidget(self.rd_male)

        self.rd_female = QRadioButton(self.btn7)
        self.rd_female.setObjectName(u"rd_female")

        self.horizontalLayout_3.addWidget(self.rd_female)


        self.verticalLayout_7.addWidget(self.btn7)

        self.btn8 = QWidget(self.card3)
        self.btn8.setObjectName(u"btn8")
        self.verticalLayout_15 = QVBoxLayout(self.btn8)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.lb8 = QLabel(self.btn8)
        self.lb8.setObjectName(u"lb8")

        self.verticalLayout_15.addWidget(self.lb8)

        self.txt_mssv = QLineEdit(self.btn8)
        self.txt_mssv.setObjectName(u"txt_mssv")

        self.verticalLayout_15.addWidget(self.txt_mssv)


        self.verticalLayout_7.addWidget(self.btn8)

        self.btn9 = QWidget(self.card3)
        self.btn9.setObjectName(u"btn9")
        self.verticalLayout_16 = QVBoxLayout(self.btn9)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.lb9 = QLabel(self.btn9)
        self.lb9.setObjectName(u"lb9")

        self.verticalLayout_16.addWidget(self.lb9)

        self.cbb_inject3 = QComboBox(self.btn9)
        self.cbb_inject3.setObjectName(u"cbb_inject3")

        self.verticalLayout_16.addWidget(self.cbb_inject3)


        self.verticalLayout_7.addWidget(self.btn9)


        self.horizontalLayout_2.addWidget(self.card3)


        self.verticalLayout_3.addWidget(self.btnFrame)


        self.verticalLayout.addWidget(self.mainFrame)

        self.Button_frame = QWidget(self.window)
        self.Button_frame.setObjectName(u"Button_frame")
        self.horizontalLayout = QHBoxLayout(self.Button_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 22)
        self.widget = QWidget(self.Button_frame)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Button_lable = QLabel(self.widget)
        self.Button_lable.setObjectName(u"Button_lable")

        self.horizontalLayout_4.addWidget(self.Button_lable)


        self.horizontalLayout.addWidget(self.widget, 0, Qt.AlignRight)

        self.widget_2 = QWidget(self.Button_frame)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_save = QPushButton(self.widget_2)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout_5.addWidget(self.btn_save)

        self.btn_delete = QPushButton(self.widget_2)
        self.btn_delete.setObjectName(u"btn_delete")

        self.horizontalLayout_5.addWidget(self.btn_delete)


        self.horizontalLayout.addWidget(self.widget_2, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.Button_frame, 0, Qt.AlignBottom)

        Ui_Update.setCentralWidget(self.window)

        self.retranslateUi(Ui_Update)

        QMetaObject.connectSlotsByName(Ui_Update)
    # setupUi

    def retranslateUi(self, Ui_Update):
        Ui_Update.setWindowTitle(QCoreApplication.translate("Ui_Update", u"MainWindow", None))
        self.Title_lable.setText(QCoreApplication.translate("Ui_Update", u"TH\u00caM H\u1ed2 S\u01a0", None))
        self.Left_lable.setText(QCoreApplication.translate("Ui_Update", u"Th\u00f4ng tin c\u00e1 nh\u00e2n", None))
        self.lb1.setText(QCoreApplication.translate("Ui_Update", u"H\u1ecd v\u00e0 t\u00ean(*)", None))
        self.lb2.setText(QCoreApplication.translate("Ui_Update", u"S\u1ed1 CMND/CCCD/HC(*)", None))
        self.lb3.setText(QCoreApplication.translate("Ui_Update", u"M\u0169i 1(*)", None))
        self.lb4.setText(QCoreApplication.translate("Ui_Update", u"Ng\u00e0y th\u00e1ng n\u0103m sinh(*)", None))
        self.lb5.setText(QCoreApplication.translate("Ui_Update", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None))
        self.lb6.setText(QCoreApplication.translate("Ui_Update", u"M\u0169i 2", None))
        self.lb7.setText(QCoreApplication.translate("Ui_Update", u"Gi\u1edbi t\u00ednh(*)", None))
        self.rd_male.setText(QCoreApplication.translate("Ui_Update", u"Nam", None))
        self.rd_female.setText(QCoreApplication.translate("Ui_Update", u"N\u1eef", None))
        self.lb8.setText(QCoreApplication.translate("Ui_Update", u"MSSV", None))
        self.lb9.setText(QCoreApplication.translate("Ui_Update", u"M\u0169i 3", None))
        self.Button_lable.setText(QCoreApplication.translate("Ui_Update", u"(*) Th\u00f4ng tin b\u1eaft bu\u1ed9c", None))
        self.btn_save.setText(QCoreApplication.translate("Ui_Update", u"L\u01b0u th\u00f4ng tin", None))
        self.btn_delete.setText(QCoreApplication.translate("Ui_Update", u"X\u00f3a", None))
    # retranslateUi

