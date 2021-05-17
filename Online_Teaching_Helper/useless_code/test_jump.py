# -*-coding:utf-8-*-
import inClass

from sys import argv
from PyQt5.QtWidgets import QApplication

app = QApplication(argv)
win= inClass.inClass()
win.show()
exit(app.exec_())