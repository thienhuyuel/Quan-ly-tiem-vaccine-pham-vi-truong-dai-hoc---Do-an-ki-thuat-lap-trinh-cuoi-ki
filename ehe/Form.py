from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
import sys
import datetime
import pandas as pd
import openpyxl
from pymongo import  *
data = []

class Ui_inputInfo(object):

    def setupUi(self, inputInfo):

        mongoClient = MongoClient("mongodb://localhost:27017")
        db = mongoClient["QuanLyTiemVaccine"]
        self.column = db["ThongTinSinhVien"]

        inputInfo.setObjectName("inputInfo")
        inputInfo.resize(1024, 600)
        inputInfo.setStyleSheet("* {\n"
"background-color: #ffede0\n"
"}")
        self.window = QtWidgets.QWidget(inputInfo)
        self.window.setObjectName("window")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lable_frame = QtWidgets.QWidget(self.window)
        self.lable_frame.setObjectName("lable_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.lable_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Title_lable = QtWidgets.QLabel(self.lable_frame)
        font = QtGui.QFont()
        font.setFamily("#9Slide03 Montserrat Black")
        font.setPointSize(20)
        font.setBold(True)
        self.Title_lable.setFont(font)
        self.Title_lable.setObjectName("Title_lable")
        self.verticalLayout_2.addWidget(self.Title_lable)
        self.verticalLayout.addWidget(self.lable_frame, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.mainFrame = QtWidgets.QWidget(self.window)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.mainFrame)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 30, 0, 15)
        self.verticalLayout_3.setSpacing(35)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.titleFrame = QtWidgets.QFrame(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleFrame.sizePolicy().hasHeightForWidth())
        self.titleFrame.setSizePolicy(sizePolicy)
        self.titleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titleFrame.setObjectName("titleFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.titleFrame)
        self.verticalLayout_4.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Left_lable = QtWidgets.QLabel(self.titleFrame)
        font = QtGui.QFont()
        font.setFamily("#9Slide03 Montserrat Medium")
        font.setPointSize(12)
        self.Left_lable.setFont(font)
        self.Left_lable.setObjectName("Left_lable")
        self.verticalLayout_4.addWidget(self.Left_lable)
        self.verticalLayout_3.addWidget(self.titleFrame)
        self.btnFrame = QtWidgets.QFrame(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnFrame.sizePolicy().hasHeightForWidth())
        self.btnFrame.setSizePolicy(sizePolicy)
        self.btnFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.btnFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btnFrame.setLineWidth(1)
        self.btnFrame.setMidLineWidth(1)
        self.btnFrame.setObjectName("btnFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.btnFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.card1 = QtWidgets.QFrame(self.btnFrame)
        self.card1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card1.setObjectName("card1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.card1)
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn1 = QtWidgets.QWidget(self.card1)
        self.btn1.setObjectName("btn1")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.btn1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lb1 = QtWidgets.QLabel(self.btn1)
        self.lb1.setObjectName("lb1")
        self.verticalLayout_8.addWidget(self.lb1)
        self.input1 = QtWidgets.QLineEdit(self.btn1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input1.sizePolicy().hasHeightForWidth())
        self.input1.setSizePolicy(sizePolicy)
        self.input1.setObjectName("input1")
        self.verticalLayout_8.addWidget(self.input1)
        self.verticalLayout_5.addWidget(self.btn1)
        self.btn2 = QtWidgets.QWidget(self.card1)
        self.btn2.setObjectName("btn2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.btn2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lb2 = QtWidgets.QLabel(self.btn2)
        self.lb2.setObjectName("lb2")
        self.verticalLayout_9.addWidget(self.lb2)
        self.input2 = QtWidgets.QLineEdit(self.btn2)
        self.input2.setObjectName("input2")
        self.verticalLayout_9.addWidget(self.input2)
        self.verticalLayout_5.addWidget(self.btn2)
        self.btn3 = QtWidgets.QWidget(self.card1)
        self.btn3.setObjectName("btn3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.btn3)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.lb3 = QtWidgets.QLabel(self.btn3)
        self.lb3.setObjectName("lb3")
        self.verticalLayout_10.addWidget(self.lb3)
        self.box1 = QtWidgets.QComboBox(self.btn3)
        self.box1.setObjectName("box1")
        #self.box1.setCurrentText(None)
        self.verticalLayout_10.addWidget(self.box1)
        self.verticalLayout_5.addWidget(self.btn3)
        self.horizontalLayout_2.addWidget(self.card1)
        self.card2 = QtWidgets.QFrame(self.btnFrame)
        self.card2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card2.setObjectName("card2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.card2)
        self.verticalLayout_6.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btn4 = QtWidgets.QWidget(self.card2)
        self.btn4.setObjectName("btn4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.btn4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.lb4 = QtWidgets.QLabel(self.btn4)
        self.lb4.setObjectName("lb4")
        self.verticalLayout_11.addWidget(self.lb4)
        self.dateInput = QtWidgets.QDateEdit(self.btn4)
        self.dateInput.setObjectName("dateInput")
        self.verticalLayout_11.addWidget(self.dateInput)
        self.verticalLayout_6.addWidget(self.btn4)
        self.btn5 = QtWidgets.QWidget(self.card2)
        self.btn5.setObjectName("btn5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.btn5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.lb5 = QtWidgets.QLabel(self.btn5)
        self.lb5.setObjectName("lb5")
        self.verticalLayout_12.addWidget(self.lb5)
        self.input3 = QtWidgets.QLineEdit(self.btn5)
        self.input3.setObjectName("input3")
        self.verticalLayout_12.addWidget(self.input3)
        self.verticalLayout_6.addWidget(self.btn5)
        self.btn6 = QtWidgets.QWidget(self.card2)
        self.btn6.setObjectName("btn6")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.btn6)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.lb6 = QtWidgets.QLabel(self.btn6)
        self.lb6.setObjectName("lb6")
        self.verticalLayout_13.addWidget(self.lb6)
        self.box2 = QtWidgets.QComboBox(self.btn6)
        self.box2.setObjectName("box2")
        self.verticalLayout_13.addWidget(self.box2)
        self.verticalLayout_6.addWidget(self.btn6)
        self.horizontalLayout_2.addWidget(self.card2)
        self.card3 = QtWidgets.QFrame(self.btnFrame)
        self.card3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card3.setObjectName("card3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.card3)
        self.verticalLayout_7.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.btn7 = QtWidgets.QWidget(self.card3)
        self.btn7.setObjectName("btn7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.btn7)
        self.horizontalLayout_3.setContentsMargins(9, 0, -1, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lb7 = QtWidgets.QLabel(self.btn7)
        self.lb7.setObjectName("lb7")
        self.horizontalLayout_3.addWidget(self.lb7)
        self.radioButton1 = QtWidgets.QRadioButton(self.btn7)
        self.radioButton1.setObjectName("radioButton_2")
        self.horizontalLayout_3.addWidget(self.radioButton1)
        self.radioButton2 = QtWidgets.QRadioButton(self.btn7)
        self.radioButton2.setObjectName("radioButton2")
        self.horizontalLayout_3.addWidget(self.radioButton2)
        self.verticalLayout_7.addWidget(self.btn7)
        self.btn8 = QtWidgets.QWidget(self.card3)
        self.btn8.setObjectName("btn8")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.btn8)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.lb8 = QtWidgets.QLabel(self.btn8)
        self.lb8.setObjectName("lb8")
        self.verticalLayout_15.addWidget(self.lb8)
        self.input4 = QtWidgets.QLineEdit(self.btn8)
        self.input4.setObjectName("input4")
        self.verticalLayout_15.addWidget(self.input4)
        self.verticalLayout_7.addWidget(self.btn8)
        self.btn9 = QtWidgets.QWidget(self.card3)
        self.btn9.setObjectName("btn9")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.btn9)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.lb9 = QtWidgets.QLabel(self.btn9)
        self.lb9.setObjectName("lb9")
        self.verticalLayout_16.addWidget(self.lb9)
        self.box3 = QtWidgets.QComboBox(self.btn9)
        self.box3.setObjectName("box3")
        self.verticalLayout_16.addWidget(self.box3)
        self.verticalLayout_7.addWidget(self.btn9)
        self.horizontalLayout_2.addWidget(self.card3)
        self.verticalLayout_3.addWidget(self.btnFrame)
        self.verticalLayout.addWidget(self.mainFrame)
        self.Button_frame = QtWidgets.QWidget(self.window)
        self.Button_frame.setObjectName("Button_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Button_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 22)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.Button_frame)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Button_lable = QtWidgets.QLabel(self.widget)
        self.Button_lable.setObjectName("Button_lable")
        self.horizontalLayout_4.addWidget(self.Button_lable)
        self.horizontalLayout.addWidget(self.widget, 0, QtCore.Qt.AlignRight)
        self.widget_2 = QtWidgets.QWidget(self.Button_frame)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.confirmButton = QtWidgets.QPushButton(self.widget_2)
        self.confirmButton.setObjectName("confirmButton")
        self.horizontalLayout_5.addWidget(self.confirmButton)
        self.horizontalLayout.addWidget(self.widget_2, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout.addWidget(self.Button_frame, 0, QtCore.Qt.AlignBottom)
        inputInfo.setCentralWidget(self.window)

        self.retranslateUi(inputInfo)
        QtCore.QMetaObject.connectSlotsByName(inputInfo)


        '''LineEdit'''
        self.dateInput.setDate(datetime.datetime.now())

        '''RadioButton'''
        self.radioButton1.setChecked(True)

        '''ComboBox'''
        vacxinList = ["Chưa tiêm", "AstraZeneca", "Vero Cell", "Abdala (Cuba)", "Pfizer", "Moderna"]
        for i in vacxinList:
            self.box1.addItem(i)
            self.box2.addItem(i)
            self.box3.addItem(i)


        # '''ConfirmButton'''
        # if self.input1. == "":
        #    self.confirmButton.hide()
        # else:
        self.confirmButton.clicked.connect(self.confirmPopup)
        # self.input1.textEdited.connect()
        # self.cofirmButton.clicked.connect(self.saveData)

        if self.box1.currentText() == "Chưa tiêm":
            self.box3.setEnabled(False)
            self.box2.setEnabled(False)
        self.box1.currentIndexChanged.connect(self.get1)

        if self.box2.currentText() == "Chưa tiêm":
            self.box3.setEnabled(False)

        self.box2.currentIndexChanged.connect(self.get2)

    def get1(self):
        self.box2.setEnabled(True)

    def get2(self):
        self.box3.setEnabled(True)
    # def on_combobox_changed(self, value):
    #     print("combobox changed", value)
    #     self.box1.



    def gender(self):
        if self.radioButton1.isChecked():
            return "Nam"
        if self.radioButton2.isChecked():
            return "Nữ"

    def errorWindow(self):
        erWindow = QMessageBox()
        erWindow.setWindowTitle("Thông báo")
        erWindow.setText("Vui lòng nhập đúng định dạng")
        erWindow.setIcon(QMessageBox.Critical)
        y = erWindow.exec()

    def notiWindow(self):
        notiWd = QMessageBox()
        notiWd.setWindowTitle("Thông báo")
        notiWd.setText("Vui lòng nhập đầy đủ thông tin yêu cầu")
        notiWd.setIcon(QMessageBox.Critical)
        z = notiWd.exec()
    def confirmWindow(self):
        msgWindow = QMessageBox()
        msgWindow.setWindowTitle("Xác nhận thông tin")
        msgWindow.setText("""
Thông tin bạn đã nhập

Họ và tên: {}
Ngày tháng năm sinh: {}
Giới tính: {}
CMND/CCCD/Passport: {}
Số điện thoại: {}
MSSV: {}
Mũi 1: {}
Mũi 2: {}
Mũi 3: {}        
""".format(self.input1.text().title(), self.dateInput.text(), self.gender(), self.input2.text(), self.input3.text(), self.input4.text(), self.box1.currentText(), self.box2.currentText(), self.box3.currentText()))

        msgWindow.setStandardButtons(QMessageBox.Cancel | QMessageBox.Save)
        msgWindow.setDefaultButton(QMessageBox.Cancel)
        msgWindow.buttonClicked.connect(self.popupButton)

        x = msgWindow.exec()

    def confirmPopup(self):
        if self.input1.text()[0].isdigit() or self.input1.text().startswith(""):
            self.errorWindow()
        elif self.input1.text()[0].isalpha():
            self.confirmWindow()
        else:
            self.notiWindow()

    def popupButton(self,i):
        if i.text() == "Save":
            self.saveData()

    def retranslateUi(self, inputInfo):
        _translate = QtCore.QCoreApplication.translate
        inputInfo.setWindowTitle(_translate("inputInfo", "MainWindow"))
        self.Title_lable.setText(_translate("inputInfo", "THÊM HỒ SƠ"))
        self.Left_lable.setText(_translate("inputInfo", "Thông tin cá nhân"))
        self.lb1.setText(_translate("inputInfo", "Họ và tên(*)"))
        self.lb2.setText(_translate("inputInfo", "Số CMND/CCCD/HC(*)"))
        self.lb3.setText(_translate("inputInfo", "Mũi 1"))
        self.lb4.setText(_translate("inputInfo", "Ngày tháng năm sinh(*)"))
        self.lb5.setText(_translate("inputInfo", "Số điện thoại"))
        self.lb6.setText(_translate("inputInfo", "Mũi 2"))
        self.lb7.setText(_translate("inputInfo", "Giới tính(*)"))
        self.radioButton1.setText(_translate("inputInfo", "Nam"))
        self.radioButton2.setText(_translate("inputInfo", "Nữ"))
        self.lb8.setText(_translate("inputInfo", "MSSV"))
        self.lb9.setText(_translate("inputInfo", "Mũi 3"))
        self.Button_lable.setText(_translate("inputInfo", "(*) Thông tin bắt buộc"))
        self.confirmButton.setText(_translate("inputInfo", "Lưu thông tin"))
    def saveData(self):
        dataImport = {"name":self.input1.text(), "date of birth": self.dateInput.text(), "gender": self.gender(), "ID":self.input2.text(), "phone":self.input3.text(), "MSSV": self.input4.text(), "mui1":self.box1.currentText(), "mui2": self.box2.currentText(), "mui3": self.box3.currentText()}
        doc = self.column.insert_one(dataImport)


# class ControlMainWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super(ControlMainWindow, self).__init__(parent)
#         self.ui = Ui_inputInfo()
#         self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_inputInfo()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
