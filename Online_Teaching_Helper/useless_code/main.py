from useless_code.at_class_students import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

if __name__ =='__main__':
    app = QApplication(sys.argv)
    window=QMainWindow()
    ui = Ui_MainWindow(window)
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())