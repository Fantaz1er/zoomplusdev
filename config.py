# -*- coding: utf-8 -*-
import os
import webbrowser
from json import load, dump

assets_tmp: str = rf'{os.getenv("tmp")}\assets'
data_tmp: str = rf'{os.getenv("tmp")}\assets\data.json'
lessons_tmp: str = rf'{os.getenv("tmp")}\assets\lessons.json'


class ZoomPlusConfig:
    def __init__(self):
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
        if data_update is None:
            data_update = self.data
        with open(rf'{assets_tmp}\\data.json', 'w', encoding='utf-8') as file:
            return dump(data_update, file, indent=4, ensure_ascii=False)

    @staticmethod
    def create_lesson_data(data_update=None):
        with open(rf'{assets_tmp}\\lessons.json', 'a') as file:
            return dump(data_update, file, indent=4, ensure_ascii=False)

    @staticmethod
    def read_data_conf():
        with open(rf'{assets_tmp}\\data.json', encoding='utf-8') as file:
            return load(file)

    def open_url_conf(self, index: int):
        return webbrowser.open(self.get_url_conf(index))

    def get_name_conf(self, index: int):
        data_read = self.read_data_conf()
        return data_read[index]['name_conf']

    def get_url_conf(self, index: int):
        return self.read_data_conf()[index]['url']

    def set_name_conf(self, value: str, index: int):
        data_read = self.read_data_conf()
        data_read[index]['name_conf'] = value
        self.create_data(data_read)

    def set_url_conf(self, value: str, index: int):
        data_read = self.read_data_conf()
        data_read[index]['url'] = value
        self.create_data(data_read)

    def create_lesson(self, name: str, url: str):
        self.create_lesson_data({'conf': name, 'url': url})
