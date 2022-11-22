# -*- coding: utf-8 -*-
import sys
import webbrowser
from json import load, dump
from os import getenv, mkdir
from os.path import exists

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow
from requests import get

from zoomplus_py.zoomplus_create_lessons import UiCreateLessonsWindow
from zoomplus_py.zoomplus_settings_names import UiEditNameWindow
from zoomplus_py.zoomplus_settings_urls import UiMainWindow
from zoomplus_py.zoomplusui import UiZoomPlus


class ZoomPlusTech:
    def __init__(self):
        self.assets_tmp: str = rf'{getenv("tmp")}\assets'
        self.data_tmp: str = rf'{getenv("tmp")}\assets\data.json'
        self.lessons_tmp: str = rf'{getenv("tmp")}\assets\lessons.json'
        self.data: list[dict[str: str, str: str]] = [
            {"name_conf": "Математика",
             "url": "https://us04web.zoom.us/j/9690474107?pwd=bUpuYXFydklnaFFlRTI2VnFIOE5sZz09"},
            {"name_conf": "Русский язык",
             "url": "https://us04web.zoom.us/j/73315543002?pwd=wlGKjsJHFWWDU2oPFeYqG4GOpKq5KK.1#success09"},
            {"name_conf": "Английский",
             "url": "https://us04web.zoom.us/j/9330067214?pwd=YkxxTnVEcUtidWVNUno5MEtPRmkyUT09"},
            {"name_conf": "История",
             "url": "https://us04web.zoom.us/j/2532973267?pwd=cFlNSmYxT3ZObzZBVTlHL0YzNFltdz09#success"},
            {"name_conf": "Информатика",
             "url": "https://us04web.zoom.us/j/76870763158?pwd=8qz8L6RZga4qFK2t2gY6ESUla93nYR.1"},
            {"name_conf": "Физика", "url": "https://us04web.zoom.us/j/2742436442?pwd=bG5OMmd1ZE4vcWRwVXFBcDEyQXl5UT09"},
            {"name_conf": "ИП", "url": "https://us04web.zoom.us/j/2491069797?pwd=cDYxRkl5ejlGSkxaSFczeXh6R3FKZz09"},
            {"name_conf": "Химия", "url": "https://us04web.zoom.us/j/7977029326?pwd=NWNYVEhmREh5VDN0TW40WnplVGQ3QT09"},
            {"name_conf": "Физ-ра",
             "url": "https://us04web.zoom.us/j/78560559321?pwd=vBa3Sfs13I3ldbcmC7ielSO30Y8jFa.1#success"},
            {"name_conf": "География",
             "url": "https://us05web.zoom.us/j/4544548111?pwd=VGhtcFl1OW14eTBreU9ULzByc2VYUT09"}
        ]

    def create_data(self, data_update=None):
        with open(self.assets_tmp + r'\data.json', 'w') as _file:
            if data_update is None:
                data_update = self.data
            return dump(data_update, _file, indent=4)

    def create_lesson_data(self, data_update=None):
        with open(rf'{self.assets_tmp}\lessons.json', 'a') as _file:
            return dump(data_update, _file, indent=4)

    @property
    def read_data_conf(self):
        with open(self.assets_tmp + r'\data.json', 'r') as _file:
            return load(_file)

    def open_url_conf(self, index_conf: int):
        return webbrowser.open(self.get_url_conf(index_conf=index_conf))

    def get_name_conf(self, index_conf: int):
        data_read = self.read_data_conf
        return data_read[index_conf]['name_conf']

    def get_url_conf(self, index_conf: int):
        return self.read_data_conf[index_conf]['url']

    for i in range(10):
        exec(f"""def set_name_conf_{i}(self, string: str):
    data_read = self.read_data_conf()
    data_read[{i}]['name_conf'] = string
    self.create_data(data_update=data_read)""")

    for i in range(10):
        exec(f"""def set_url_conf_{i}(self, url: str):
    data_read = self.read_data_conf
    data_read[{i}]['url'] = url
    self.create_data(data_update=data_read)""")

    @staticmethod
    def get_name_lesson(name: str) -> str:
        return name

    @staticmethod
    def get_url_lesson(url: str) -> str:
        return url

    def create_lesson(self, name: str, url: str):
        self.create_lesson_data(data_update={'conf': name, 'url': url})


if __name__ == "__main__":
    zoom_plus_tech = ZoomPlusTech()  # technical settings classes
    # Setting files app
    if not exists(zoom_plus_tech.assets_tmp):
        mkdir(zoom_plus_tech.assets_tmp)
        zoom_plus_tech.create_data()
    elif not exists(zoom_plus_tech.data_tmp):
        zoom_plus_tech.create_data()
    elif not exists(zoom_plus_tech.lessons_tmp):
        zoom_plus_tech.create_lesson_data()
    # Icon app:
    if not exists(rf'{zoom_plus_tech.assets_tmp}\favicon.png'):
        response = get(url='https://cdn.icon-icons.com/icons2/2428/PNG/512/zoom_black_logo_icon_147040.png',
                       allow_redirects=True)
        open(rf'{zoom_plus_tech.assets_tmp}\favicon.png', 'wb').write(response.content)

    # App
    app = QApplication(sys.argv)  # body app
    app.setWindowIcon(QIcon(rf'{zoom_plus_tech.assets_tmp}\favicon.png'))  # set icon

    # Main windows
    window = QMainWindow()  # 1 window
    window_settings_conf_name = QMainWindow()  # 2 window
    window_settings_conf_url = QMainWindow()  # 3 window
    window_create_lessons_conf = QMainWindow()  # 4 window

    ui_main = UiZoomPlus(window_settings_conf_name, window_settings_conf_url, window_create_lessons_conf)  # 1
    ui_setting_names_conf = UiEditNameWindow()  # 2
    ui_setting_urls_conf = UiMainWindow()  # 3, but set on UiEditUrlWindow()
    ui_create_lessons_conf = UiCreateLessonsWindow()  # 4
    ui_main.setup_ui(window, action=zoom_plus_tech)  # 1
    ui_setting_names_conf.setup_ui(window_settings_conf_name, action=zoom_plus_tech)  # 2
    ui_setting_urls_conf.setup_ui(window_settings_conf_url, action=zoom_plus_tech)  # 3
    ui_create_lessons_conf.setup_ui(window_create_lessons_conf, action=zoom_plus_tech)  # 4

    window.show()  # show body window
    sys.exit(app.exec())  # exit from program if person close this main window
