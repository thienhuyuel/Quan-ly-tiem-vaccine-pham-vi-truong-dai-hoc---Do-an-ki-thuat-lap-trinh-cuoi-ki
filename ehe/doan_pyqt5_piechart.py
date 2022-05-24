from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
#from matplotlib import pyplot as plt
from pymongo import *
#DB connection
mongo_client= MongoClient("mongodb://localhost:27017/")
db = mongo_client["Va"]
col = db["ThongTinSinhVien"]
cur=col.find({})
list=list(cur)

mui1=0
mui2=0
mui3=0
for i in list:
    if i["mui1"] != "Chưa tiêm" and i["mui2"] != "Chưa tiêm" and i["mui3"] != "Chưa tiêm":
        mui3 += 1
    if i["mui1"] != "Chưa tiêm" and i["mui2"] != "Chưa tiêm" and i["mui3"] == "Chưa tiêm":
        mui2 += 1
    if i["mui1"] != "Chưa tiêm" and i["mui2"] == "Chưa tiêm" and i["mui3"] == "Chưa tiêm":
        mui1 += 1
        
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bieu Do Mui Tiem")
        self.setGeometry(100,100,650,400)
        self.show()
        self.pie_chart()
    def pie_chart(self):
        mui_tiem = QtChart.QPieSeries()
        mui_tiem.append("đã tiêm 1 mũi", mui1)
        mui_tiem.append("đã tiêm 2 mũi", mui2)
        mui_tiem.append("đã tiêm 3 mũi", mui3)
        mui_tiem.setLabelsVisible(True)

        mui_tiem.setLabelsPosition(QtChart.QPieSlice.LabelOutside)
        for slice in mui_tiem.slices():
            slice.setLabel("{:1.2f}%".format(100 * slice.percentage()))

        slice = QPieSlice()
        #slice = mui_tiem.slices()[2]
        slice.setLabelVisible(True)
        mui_tiem.slices()[0].setColor(Qt.darkGreen)
        mui_tiem.slices()[1].setColor(Qt.darkGray)
        mui_tiem.slices()[2].setColor(Qt.darkCyan)

        chart = QChart()
        chart.legend()
        chart.addSeries(mui_tiem)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("BIỂU ĐỒ TIÊM VACCINE")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chart.legend().markers(mui_tiem)[0].setLabel("đã tiêm 1 mũi")
        chart.legend().markers(mui_tiem)[1].setLabel("đã tiêm 2 mũi")
        chart.legend().markers(mui_tiem)[2].setLabel("đã tiêm 3 mũi")

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chartview)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())




