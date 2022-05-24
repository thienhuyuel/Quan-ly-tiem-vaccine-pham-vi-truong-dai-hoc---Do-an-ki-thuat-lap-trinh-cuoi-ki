import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 1024, 600))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-image: url(h.png);\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(200, 30, 611, 61))
        self.label.setStyleSheet("color: rgb(181, 39, 46); font: 15pt \"UTM Facebook\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(20, 90, 141, 41))
        self.pushButton.setStyleSheet("font: 10pt \"UTM Avo\"; \n"
"color: rgb(230, 116, 71);")
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 170, 901, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setStyleSheet("color:rgb(230, 116, 71); font: 9pt \"UTM Avo\"; border-color:rgb(230, 116, 71) ")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.tableWidget.reset)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "DANH SÁCH SINH VIÊN THỰC HIỆN TIÊM VACCINE"))
        self.pushButton.setText(_translate("MainWindow", "Tải bảng"))

"""
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
"""
