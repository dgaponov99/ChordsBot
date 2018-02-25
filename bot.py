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


def message_to_admin(about):
    pass
