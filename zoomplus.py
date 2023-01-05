# -*- coding: utf-8 -*-
from sys import argv, exit

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow
from requests import get

from config import *
from zoomplus_auth import Interface
from zoomplus_py.zoomplus_create_lessons import UiCreateLessonsWindow
from zoomplus_py.zoomplus_settings_names import UiEditNameWindow
from zoomplus_py.zoomplus_settings_urls import UiEditUrlWindow
from zoomplus_py.zoomplusui import UiZoomPlus

if __name__ == "__main__":
    cfg = ZoomPlusConfig()  # technical settings classes
    # Setting files app
    if not os.path.exists(assets_tmp):
        os.mkdir(assets_tmp)
        cfg.create_data()
    elif not os.path.exists(data_tmp):
        cfg.create_data()
    elif not os.path.exists(lessons_tmp):
        cfg.create_lesson_data()
    # Icon app:
    if not os.path.exists(rf'{assets_tmp}\\favicon.png'):
        response = get(url='https://cdn.icon-icons.com/icons2/2428/PNG/512/zoom_black_logo_icon_147040.png',
                       allow_redirects=True)
        open(rf'{assets_tmp}\\favicon.png', 'wb').write(response.content)

    # App
    app = QApplication(argv)  # body app
    app.setWindowIcon(QIcon(rf'{assets_tmp}\\favicon.png'))  # set icon

    # Main windows
    window = QMainWindow()  # 1 window
    window_auth = Interface(window)  # Auth window
    window_settings_conf_name = QMainWindow()  # 2 window
    window_settings_conf_url = QMainWindow()  # 3 window
    window_create_lessons_conf = QMainWindow()  # 4 window

    ui_main = UiZoomPlus(window_settings_conf_name, window_settings_conf_url, window_create_lessons_conf)  # 1
    ui_setting_names_conf = UiEditNameWindow()  # 2
    ui_setting_urls_conf = UiEditUrlWindow()  # 3, but set on UiEditUrlWindow()
    ui_create_lessons_conf = UiCreateLessonsWindow()  # 4
    ui_main.setup_ui(window)  # 1
    ui_setting_names_conf.setup_ui(window_settings_conf_name)  # 2
    ui_setting_urls_conf.setup_ui(window_settings_conf_url)  # 3
    ui_create_lessons_conf.setup_ui(window_create_lessons_conf)  # 4

    window_auth.show()  # show body window
    exit(app.exec())  # exit from program if person close this main window
