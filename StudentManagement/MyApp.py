from PyQt6.QtWidgets import QApplication, QMainWindow

from StudentManagement.MainWindowEX import MainWindowEx

# MyApp.py (đầu file)
import faulthandler
faulthandler.enable()   # in stack trace nếu có crash native

app=QApplication([])
myWindow=MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.connectMySQL()
myWindow.selectAllStudent()
myWindow.show()
app.exec()