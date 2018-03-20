# Заполнение базы данных url-адресами изображений
# с сайта gitaristu.ru
# Для обновления запустите этот скрипт
# Работает примерно 2.5 часа

from databases.db import Database
from databases import db_config
from databases.docs import chords_docs

import requests
from bs4 import BeautifulSoup

GUITAR_URL = 'http://www.gitaristu.ru'
GENERAL_URL = '/generator_akkordov/chords'

chords_db = Database(db_config.GUITAR_CHORDS_URL)


def to_database(chord_name, url_list):
    chords_db.add_doc(chords_docs.chords(chord_name,
                                         url_list, 'urls'))


def get_chords_list(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    chords_list = soup.find(id='chordslist').find_all('a')
    for i in range(0, len(chords_list)):
        chords_list[i] = chords_list[i].get('href')
    return chords_list if len(chords_list) > 0 else None


def get_image_urls(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    items = soup.find_all('a', {'class': 'fancybox'})
    if len(items) > 0:
        name = items[0].get('alt').split(' ')[1].lower()
        images = []
        for item in items:
            images.append(GUITAR_URL + item.get('href'))
        return name, images
    return None, None


general_list = get_chords_list(GUITAR_URL + GENERAL_URL)
for general_part in general_list:
    chords_list = get_chords_list(GUITAR_URL + general_part)
    for chord in chords_list:
        name, images = get_image_urls(GUITAR_URL + chord)
        if name is not None:
            to_database(name, images)
            print(name)
        bass_list = get_chords_list(GUITAR_URL + chord)
        if bass_list is not None:
            for bass_chord in bass_list:
                name, images = get_image_urls(GUITAR_URL + bass_chord)
                if name is not None:
                    to_database(name, images)
                    print(name)
