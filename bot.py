import os

import telebot
from telebot import types
import requests

from res import string_values
from databases.db import Database
from databases import db_config
from databases.docs import users_docs

from chord_imaging import chords

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

users_database = Database(db_config.USERS)


def greeting(chat_id, first_name):
    bot.send_message(chat_id, string_values.greeting.format(first_name), parse_mode='HTML')


def add_new_user(chat_id, first_name):
    success = users_database.add_doc(users_docs.new_user(chat_id, first_name))
    if success:
        message_to_admin('new_user')
        print('пользователь добавлен')


def change_mode(chat_id, mode):
    mode = mode_validate(mode)
    users_database.change_doc(users_docs.user(chat_id),
                              users_docs.user_mode(mode))
    bot.send_message(chat_id, string_values.change_mode.format(mode.title()))


def mode_validate(mode):
    space_index = mode.find(' ')
    if space_index != -1:
        return mode[1:space_index]
    return mode[1:]


def message_to_admin(about):  # доделать
    pass


def get_mode(user_id):
    user = users_database.get_one_doc(user_id)
    return user['mode']


def chord_validation(chord):
    if len(chord) > 15:
        return None
    return chord.lower()


def send_fail(user_id):
    bot.send_message(user_id, 'Аккорд не найден')  # Исправить


def send_processing(user_id):
    return bot.send_message(user_id, 'Обновление базы...')  # Исправить


def chord_processing(message):
    user_id = message.chat.id
    chord = chord_validation(message.text)
    mode = get_mode(user_id)

    if chord is None:
        send_fail(user_id)
        return False

    image_list = chords.get_chord_files_id(mode, chord)
    if image_list is not None:
        send_images(user_id, image_list)
        return True

    msg_pr = send_processing(user_id)

    urls_list = chords.get_chord_urls(mode, chord)
    if urls_list is not None:
        files_id = send_images(user_id, urls_list)
        chords.add_chord(mode, chord, files_id)
        del_message(msg_pr)
        return True
    del_message(msg_pr)
    send_fail(user_id)
    return False


def del_message(msg):
    bot.delete_message(msg.chat.id, msg.message_id)


def split_of_list(l):
    length = len(l)
    new_l = []
    num = int(length / 10)

    for i in range(num):
        new_l.append(l[:10])
        l = l[10:]
    new_l.append(l)

    return new_l


def send_error(user_id):  # исправить
    pass


def send_images(user_id, images_list):
    images_box = split_of_list(images_list)
    converting_to_media(images_box)
    print(images_box)

    files_id = []

    for images in images_box:
        if len(images) > 1:
            try:
                messages_file = bot.send_media_group(user_id, images)
                for message_file in messages_file:
                    files_id.append(message_file.photo[0].file_id)
            except Exception:
                send_error(user_id)
        else:
            if images[0].startswith('http'):
                img = requests.get(images[0])
                try:
                    file = bot.send_photo(user_id, img.content)
                    files_id.append(file.photo[0].file_id)
                except Exception:
                    send_error(user_id)
            else:
                try:
                    bot.send_photo(user_id, images[0])
                except Exception:
                    send_error(user_id)

    if len(files_id) == 0:
        return None
    return files_id


def converting_to_media(box):
    length = len(box)
    for i in range(length):
        if type(box[i]) == list:
            converting_to_media(box[i])
        elif length > 1:
            box[i] = types.InputMediaPhoto(box[i])
