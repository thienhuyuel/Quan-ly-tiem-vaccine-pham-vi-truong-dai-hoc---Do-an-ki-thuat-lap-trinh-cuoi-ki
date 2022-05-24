import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot, Qt
from GetCrawledData import Data

class Covid19_status(QWidget):

    def __init__(self):
        super().__init__()
        self.title = ''
        self.left = 0
        self.top = 0
        self.width = 1024
        self.height = 600
        self.initUI()

        
    def initUI(self):

        self.data = Data()
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #Label
        label = QLabel(self)
        label.setText("<font size>Tình hình dịch cả nước")
        label.setFont(QFont('Arial',18))
        label.setAlignment(Qt.AlignCenter)

        #Buttons
        update_button = QPushButton('Update',self)

        time = QLabel(self)
        time.setText(self.data.time)
        time.setFont(QFont('Arial',18))
        time.setAlignment(Qt.AlignCenter)

        self.createTable()

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.tableWidget)
        self.h_layout.addWidget(time)
        self.h_layout.addWidget(update_button)

        # Add box layout, add table to box layout and add box layout to widget
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(label)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout) 

        # Show widget
        #self.show()

    def createTable(self):
        

       # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(self.data.cities)-1)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels((f"{self.data.cities[0]};{self.data.total_cases[0]};{self.data.total_day[0]};{self.data.death[0]}").split(";"))

        for x in range(1,len(self.data.cities)):
            for y in range(0,4):
                if y == 0:
                    self.tableWidget.setItem(x-1,y, QTableWidgetItem(self.data.cities[x]))
                elif y == 1:
                    self.tableWidget.setItem(x-1,y, QTableWidgetItem(self.data.total_cases[x]))
                elif y == 2:
                    self.tableWidget.setItem(x-1,y, QTableWidgetItem(self.data.total_day[x]))
                elif y == 3:
                    self.tableWidget.setItem(x-1,y, QTableWidgetItem(self.data.death[x]))
        
        self.tableWidget.move(0,0)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
 

#app = QApplication(sys.argv)
#ex = App()
#sys.exit(app.exec_())  
