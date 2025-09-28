from PyQt6.QtWidgets import QApplication, QMainWindow

from review.MainWindowListProductExt import MainWindowListProductExt
from review.products import ListProduct
from review.review_list import Product

app=QApplication([])
qmain=QMainWindow()
myWindow=MainWindowListProductExt()
myWindow.setupUi(qmain)

#load data:
lp=ListProduct()
lp.add_product(Product("p1","Juice",19,20.000))
lp.add_product(Product("p2","Water",4,10.000))
lp.add_product(Product("p3","Detox",20,12.000))
lp.add_product(Product("p4","Coca",9,12.000))

myWindow.load_products(lp)

myWindow.showWindow()
app.exec()
