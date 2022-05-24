import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.QtCore import QDate
from .ui_search import Ui_Search
from .ui_update import Ui_Update
import pymongo
import datetime
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["QuanLyTiemVaccine"]
mycol = mydb["ThongTinSinhVien"]


def show_message_box(title, message, type: str = 'info'):
    msg_box = QMessageBox()
    if type == 'critical':
        msg_box.setIcon(QMessageBox.Critical)
    else:
        msg_box.setIcon(QMessageBox.Information)
    msg_box.setText(message)
    msg_box.setWindowTitle(title)
    msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    return msg_box.exec_()


class UpdateWindow(QMainWindow):
    def __init__(self, row):
        QMainWindow.__init__(self)
        self.ui =  Ui_Update()
        self.ui.setupUi(self)
        self.row = row

        # Destructuring row data
        # ///////////////////////////////////////////////////////////////
        name, dateofbirth, sex, id, phone, mssv, inject1, inject2, inject3 = (
            row["name"], row['date of birth'], row["gender"], row["ID"], row["phone"],
            row["MSSV"], row['mui1'], row["mui2"], row["mui3"])

        # SET SIZE APP
        # ///////////////////////////////////////////////////////////////
        width = 1200
        height = 600
        self.setFixedSize(width, height)

        # SET APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Ứng Dụng Tra Cứu Thông Tin Covid-19"
        self.setWindowTitle(title)

        # ADD LIST INJECT TO COMBOBOX
        # ///////////////////////////////////////////////////////////////
        LIST_INJECT = ['Vero Cell', 'AstraZeneca', 'Pfizer']
        self.ui.cbb_inject1.addItems(LIST_INJECT)
        self.ui.cbb_inject2.addItems(LIST_INJECT)
        self.ui.cbb_inject3.addItems(LIST_INJECT)

        # SET VALUE FROM ROW TO APP
        # ///////////////////////////////////////////////////////////////
        self.ui.txt_name.setText(name)
        date = QDate(int(dateofbirth.split(
            '/')[2]), int(dateofbirth.split('/')[1]), int(dateofbirth.split('/')[0]))
        self.ui.txt_birthday.setDate(date)
        self.ui.txt_id.setText(str(id))
        self.ui.txt_phone.setText(str(phone))
        self.ui.txt_mssv.setText(str(mssv))
        if sex.lower() == 'nam':
            self.ui.rd_male.setChecked(True)
        else:
            self.ui.rd_female.setChecked(True)
        self.ui.cbb_inject1.setCurrentText(inject1)
        self.ui.cbb_inject2.setCurrentText(inject2)
        self.ui.cbb_inject3.setCurrentText(inject3)
        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////
        self.ui.btn_delete.clicked.connect(lambda: self.delete(id))
        self.ui.btn_save.clicked.connect(lambda: self.update(id))

        self.show()

    # BUTTONS CLICK
    # Functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def delete(self, id: int):
        x = mycol.delete_many({"ID": id})

        show_message_box('Thông báo', 'Xóa thành công !')
        # SHOW UI SEARCH
        # ///////////////////////////////////////////////////////////////
        self.search_window = SeacrhWindow()
        self.search_window.show()
        self.close()

    def update(self, id: int):
        day = self.ui.txt_birthday.date()
        format_day = '{0}/{1}/{2}'.format(day.day(), day.month(), day.year())
        if self.ui.rd_male.isChecked():
            sex = 'Nam'
        else:
            sex = 'Nữ'
        mycol.update_one(
            {"ID": id}, {"$set": {"name": self.ui.txt_name.text()}})
        mycol.update_one(
            {"ID": id}, {"$set": {"DOB": format_day}})
        mycol.update_one(
            {"ID": id}, {"$set": {"Sex": sex}})
        mycol.update_one(
            {"ID": id}, {"$set": {"ID":  int(self.ui.txt_id.text())}})
        mycol.update_one(
            {"ID": id}, {"$set": {"Phone": self.ui.txt_phone.text()}})
        mycol.update_one(
            {"ID": id}, {"$set": {"Student_ID": int(self.ui.txt_mssv.text())}})
        mycol.update_one(
            {"ID": id}, {"$set": {"1st_injection": self.ui.cbb_inject1.currentText()}})
        mycol.update_one(
            {"ID": id}, {"$set": {"2nd_injection": self.ui.cbb_inject2.currentText()}})
        mycol.update_one(
            {"ID": id}, {"$set": {"3rd_injection": self.ui.cbb_inject3.currentText()}})
        isContinue = show_message_box(
            'Thông báo', 'Lưu thành công, tiếp tục chỉnh sửa ?') == QMessageBox.Ok
        if not isContinue:
            # SHOW UI SEARCH
            # ///////////////////////////////////////////////////////////////
            self.search_window = SeacrhWindow()
            self.search_window.show()
            self.close()


class SeacrhWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Search()
        self.ui.setupUi(self)

        width = 600
        height = 300
        # SET SIZE APP
        # ///////////////////////////////////////////////////////////////
        self.setFixedSize(width, height)

        # SET APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Ứng Dụng Tra Cứu Thông Tin Covid-19"
        self.setWindowTitle(title)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////
        self.ui.btn_search.clicked.connect(self.search)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

    # BUTTONS CLICK
    # Functions for clicked buttons
    # ///////////////////////////////////////////////////////////////

    def search(self):
        count = 0
        value = self.ui.txt_search.text()
        print('SEARCH:', value)
        myquery = {"ID": value}
        mydoc = mycol.find(myquery)
        for x in mydoc:
            row = x
        # CHECK SEARCH VALUE
        # //////////////////////////////////////////////////////////////
        if not value:
            return show_message_box('Thông báo', 'Vui lòng nhập CMND hoặc CCCD để tìm !', 'critical')
        for x in mycol.find({}, {"_id": 0, "ID": 1}):
            if x['ID'] == value:
                count += 1
        if count == 0:
            return show_message_box('Thông báo', 'Không tìm thấy dữ liệu trong hệ thống !', 'critical')

        # SHOW UI UPDATE
        # ///////////////////////////////////////////////////////////////
        self.update_window = UpdateWindow(row)
        self.update_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SeacrhWindow()
    sys.exit(app.exec_())
