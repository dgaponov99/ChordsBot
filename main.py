import os
import telebot

import bot
import config

# from flask import Flask, request

TOKEN = os.environ.get('TOKEN')
server_bot = telebot.TeleBot(TOKEN)


# server = Flask(__name__)


@server_bot.message_handler(commands=['start'])
def start(message):
    bot.greeting(message.chat.id, message.from_user.first_name)
    bot.add_new_user(message.chat.id, message.from_user.first_name)


@server_bot.message_handler(commands=config.INSTRUMENTS)
def mode(message):
    bot.change_mode(message.chat.id, message.text)


@server_bot.message_handler(func=lambda message: True, content_types=['text'])
def text_message(message):
    pass


# @server.route('/' + TOKEN, methods=['POST'])
# def get_message():
#     bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
#     return "!", 200
#
#
# @server.route("/")
# def webhook():
#     bot.remove_webhook()
#     bot.set_webhook(url=os.environ.get('URL') + os.environ.get('TOKEN'))
#     return "!", 200
#
#
# if __name__ == "__main__":
#     server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

if __name__ == "__main__":
    server_bot.polling()
