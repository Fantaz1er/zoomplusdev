from PyQt6 import QtWidgets, QtGui, QtCore

from check_db import *
from zoomplus_py.zoomplusauthui import UiRegistration


class Interface(QtWidgets.QWidget):
    def __init__(self, main_window, parent=None):
        super(Interface, self).__init__(parent)
        self.ui = UiRegistration()
        self.ui.setup_ui(self)

        self.ui.pushButton.clicked.connect(self.auth)
        self.ui.pushButton_2.clicked.connect(self.reg)

        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

        self.main_window = main_window

    # Check correct input data
    @staticmethod
    def check_input(function):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            function(self)

        return wrapper

    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, "Оповещение", value)

    @check_input
    def auth(self):
        name = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        auth = self.check_db.thr_login(name, password)

        if auth:
            self.main_window.show()
            self.close()

    @check_input
    def reg(self):
        name = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        auth = self.check_db.thr_register(name, password)

        if auth:
            self.main_window.show()
            self.close()
