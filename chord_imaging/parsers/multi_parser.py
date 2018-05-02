import requests
from bs4 import BeautifulSoup

from res.riffspot import riff_cfg


def create_url_of_chord(instrument, chord):
    return riff_cfg.URL.format(instrument, chord)


def validation_soup(soup):
    empty_page = riff_cfg.EMPTY_PAGE
    title = soup.find('head').find('title').contents[0]
    if title == empty_page:
        return False
    return True


def get_images(instrument, url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    validate = validation_soup(soup)
    if not validate:
        return None

    pref = 'https:'
    if instrument == 'piano':
        return [pref + soup.find('div', {'class': 'col-md-12'}).find('img').get('src')]

    class_list = soup.find_all('img', {'class': 'margin-bottom-20'})
    image_list = []
    for img in class_list:
        image_list.append(pref + img.get('src'))
    return image_list
