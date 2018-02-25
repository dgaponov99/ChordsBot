import telebot
import os

import config

from res import string_values
from databases import users_docs
from databases.db import Database

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

users_database = Database(config.USERS)


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


def message_to_admin(about):
    pass
