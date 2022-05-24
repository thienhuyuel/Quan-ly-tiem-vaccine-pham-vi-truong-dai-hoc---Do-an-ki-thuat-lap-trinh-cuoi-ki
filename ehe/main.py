from PyQt5 import QtCore, QtGui, QtWidgets

import sys


from capnhattinhhinh import Covid19_status
from Form import ControlMainWindow
from uu import LoadData
from doan_pyqt5_piechart import Window
from update import update_Init

class Ui_Main(object):
    def setupUi(self, Mainwindow):
        Mainwindow.setObjectName("Mainwindow")
        Mainwindow.resize(1024, 600)
        self.widget = QtWidgets.QWidget(Mainwindow)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background: url(ggg.png)\n"
"}")
        self.widget.setObjectName("widget")
        #toolbar = QtWidgets.QToolBar("Exit")
        #toolbar.addAction()
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(330, 10, 355, 43))
        self.label.setStyleSheet("color: rgb(230, 119, 71); font: 18pt \"UTM Facebook\"; ")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(360, 60, 301, 28))
        font = QtGui.QFont()
        font.setFamily("UTM AVo")
        font.setPointSize(13)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("font: 13pt \"UTM AVo\"; color: rgb(230, 103, 71)")
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(450, 230, 161, 201))
        font = QtGui.QFont()
        font.setFamily("UTM Avo")
        font.setPointSize(9)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"image: url(p.png); border: none; text-align:top; color: rgb(230, 116, 71); font: 9pt \"UTM Avo\";\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"image: url(p.png); border: none; text-align:top; font: 9pt \"UTM Avo\"; color: rgb(85, 255, 0);\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"image: url(p.png); border: none; text-align:top; color: rgb(230, 116, 71); font: 9pt \"UTM Avo\";\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.switch_to_form)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 110, 161, 191))
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
"image: url(m2.png); border: none; text-align:top; color: rgb(230, 116, 71); font: 9pt \"UTM Avo\";\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"image: url(m2.png); border: none; text-align:top; font: 9pt \"UTM Avo\"; color: rgb(85, 255, 0);\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"image: url(m2.png); border: none; text-align:top; color: rgb(230, 116, 71); font: 9pt \"UTM Avo\";\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.switch_to_table)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 350, 161, 191))
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_3{\n"
"image: url(m3.png); border: none; text-align:top; color: rgb(230, 116, 71); font: 9pt \"UTM Avo\";\n"
"}\n"
"QPushButton#pushButton_3:hover{\n"
"image: url(m3.png); border: none; text-align:top; font: 9pt \"UTM Avo\"; color: rgb(85, 255, 0);\n"
"}\n"
"QPushButton#pushButton_3:pressed{\n"
"image: url(m3.png); border: none; text-align:top; color: rgb(230, 116, 71); font: 9pt \"UTM Avo\";\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.switch_to_update)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(810, 120, 161, 191))
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4{\n"
"image: url(m4.png); border: none; text-align:top; color: rgb(230, 116, 71); font: 9pt \"UTM Avo\";\n"
"}\n"
"QPushButton#pushButton_4:hover{\n"
"image: url(m4.png); border: none; text-align:top; font: 9pt \"UTM Avo\"; color: rgb(85, 255, 0);\n"
"}\n"
"QPushButton#pushButton_4:pressed{\n"
"image: url(m4.png); border: none; text-align:top; color: rgb(230, 116, 71); font: 9pt \"UTM Avo\";\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.switch_to_chart)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(820, 350, 161, 191))
        self.pushButton_5.setStyleSheet("QPushButton#pushButton_5{\n"
"image: url(m5.png); border: none; text-align:top; color: rgb(230, 116, 71); font: 9pt \"UTM Avo\";\n"
"}\n"
"QPushButton#pushButton_5:hover{\n"
"image: url(m5.png); border: none; text-align:top; font: 9pt \"UTM Avo\"; color: rgb(85, 255, 0);\n"
"}\n"
"QPushButton#pushButton_5:pressed{\n"
"image: url(m5.png); border: none; text-align:top; color: rgb(230, 116, 71); font: 9pt \"UTM Avo\";\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.switch_to_status_covid19)

        self.retranslateUi(Mainwindow)
        QtCore.QMetaObject.connectSlotsByName(Mainwindow)

    def retranslateUi(self, Mainwindow):
        _translate = QtCore.QCoreApplication.translate
        Mainwindow.setWindowTitle(_translate("Mainwindow", "Mainwindow"))
        self.label.setText(_translate("Mainwindow", "THÔNG TIN TIÊM CHỦNG"))
        self.label_2.setText(_translate("Mainwindow", "SINH VIÊN ĐH KINH TẾ - LUẬT"))
        self.pushButton.setText(_translate("Mainwindow", "THÊM HỒ SƠ"))
        self.pushButton_2.setText(_translate("Mainwindow", "DANH SÁCH"))
        self.pushButton_3.setText(_translate("Mainwindow", "TRA CỨU/ CẬP NHẬP"))
        self.pushButton_4.setText(_translate("Mainwindow", "BIỂU ĐỒ"))
        self.pushButton_5.setText(_translate("Mainwindow", "TÌNH HÌNH COVID-19"))
    def switch_to_status_covid19(self):
        screen = Covid19_status()
        widget.addWidget(screen)
        widget.setCurrentWidget(screen)
    def switch_to_table(self):
        screen = LoadData()
        widget.addWidget(screen)
        widget.setCurrentWidget(screen)
    def switch_to_chart(self):
        screen = Window()
        widget.addWidget(screen)
        widget.setCurrentWidget(screen)
    def switch_to_update(self):
        screen = update_Init.SeacrhWindow()
        widget.addWidget(screen)
        widget.setCurrentWidget(screen)
    def switch_to_form(self):
        screen = ControlMainWindow()
        widget.addWidget(screen)
        widget.setCurrentWidget(screen)
    #def setMainMenu(self):
        #widget.setCurrentWidget(mainwindow)

app = QtWidgets.QApplication(sys.argv)

mainMenu = QtWidgets.QMainWindow()
ui = Ui_Main()
ui.setupUi(mainMenu)

#form = QtWidgets.QMainWindow()
#ui = Ui_inputInfo()
#ui.setupUi(form)

widget = QtWidgets.QStackedWidget()

mainwindow = mainMenu


widget.addWidget(mainwindow)

#widget.addWidget(input_form)
widget.setFixedHeight(600)
widget.setFixedWidth(1024)

widget.show()

sys.exit(app.exec_())
