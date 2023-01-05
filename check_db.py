from PyQt6 import QtCore

from handler.db_handler import login, register


class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def thr_login(self, name, password) -> bool:
        return login(name, password, self.mysignal)

    def thr_register(self, name, password) -> bool:
        return register(name, password, self.mysignal)
