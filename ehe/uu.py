from ast import List
import sys
import pandas as pd
from r import *
from PyQt5.QtWidgets import QTableWidget, QTableView, QWidget,QTableWidgetItem 

class LoadData(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.read_excel)
    
    def read_excel(self):
        df=pd.read_excel('QuanLyTiemVC.xlsx')
        column= list(df.columns)
        row= df.to_numpy().tolist()
        x=len(column)
        y=len(row)

        self.ui.tableWidget.setRowCount(y)
        self.ui.tableWidget.setColumnCount(x)
        
        for i in range (x):
            hd=QtWidgets.QTableWidgetItem(column[i])
            self.ui.tableWidget.setHorizontalHeaderItem(i, hd)
            for j in range (y):
                dt=str(row[j][i])
                self.ui.tableWidget.setItem(j,i, QTableWidgetItem(dt))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ld=LoadData()
    ld.show()
    sys.exit(app.exec_())

 