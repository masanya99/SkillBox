from PyQt5 import QtWidgets
import clienui

class MyWindow(QtWidgets.QMainWindow, clienui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.seetupUi(self)


app = QtWidgets.QApplication([])
window = MyWindow()
window.show()
app.exec_()