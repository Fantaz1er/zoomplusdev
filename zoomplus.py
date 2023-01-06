# -*- coding: utf-8 -*-
from sys import argv, exit

from PyQt6 import QtGui, QtWidgets

from config import favicon_tmp
from zoomplus_auth import Interface
from zoomplus_py.zoomplus_create_lessons import UiCreateLessonsWindow
from zoomplus_py.zoomplus_settings_names import UiEditNameWindow
from zoomplus_py.zoomplus_settings_urls import UiEditUrlWindow
from zoomplus_py.zoomplusui import UiZoomPlus


class ZoomPlus:
    def __init__(self):
        # MAIN APP:
        application = QtWidgets.QApplication(argv)
        application.setWindowIcon(QtGui.QIcon(favicon_tmp))  # set favicon on app

        # MAIN WINDOWS:
        window_main = QtWidgets.QMainWindow()  # 1
        window_auth = Interface(window_main)  # Start show
        window_settings_conf_name = QtWidgets.QMainWindow()  # 2
        window_settings_conf_url = QtWidgets.QMainWindow()  # 3
        window_create_lessons_conf = QtWidgets.QMainWindow()  # 4

        # Ui interfaces
        ui_main = UiZoomPlus(window_settings_conf_name, window_settings_conf_url, window_create_lessons_conf)  # 1
        ui_setting_names_conf = UiEditNameWindow()  # 2
        ui_setting_urls_conf = UiEditUrlWindow()  # 3
        ui_create_lessons_conf = UiCreateLessonsWindow()  # 4

        # Initializing methods
        ui_main.setup_ui(window_main)  # 1
        ui_setting_names_conf.setup_ui(window_settings_conf_name)  # 2
        ui_setting_urls_conf.setup_ui(window_settings_conf_url)  # 3
        ui_create_lessons_conf.setup_ui(window_create_lessons_conf)  # 4

        # Start interface
        window_auth.show()
        exit(application.exec())  # exit from program


if __name__ == "__main__":
    ZoomPlus()
