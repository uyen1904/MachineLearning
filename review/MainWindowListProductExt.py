from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem

from review.MainWindowListProduct import Ui_MainWindow


class MainWindowListProductExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def showWindow(self):
        self.MainWindow.show()
    def load_products(self,lp):
        self.tableWidgetProduct.setRowCount(0) #xoá hết dữ liệu nhưng mà cột giữ nguyên không bị xoá
        for i in range(0, len(lp.products)):
            p=lp.products[i]
            number_row=self.tableWidgetProduct.rowCount() #lấy số dòng trên giao diện ra
            #insert new row (last row):
            self.tableWidgetProduct.insertRow(number_row)
            #fill attributes product into ListView:
            self.tableWidgetProduct.setItem(number_row,0, QTableWidgetItem(p.id)) #truyền row trước, sau đó đến column, QTableWidgetItem truyền vào dữ liệu phải là chuỗi, nếu là số thì phải đổi thành chuỗi tức là thêm str)
            self.tableWidgetProduct.setItem(number_row,1,QTableWidgetItem(p.name))
            self.tableWidgetProduct.setItem(number_row,2,QTableWidgetItem(str(p.quantity)))
            self.tableWidgetProduct.setItem(number_row,3,QTableWidgetItem(str(p.price)))
        pass