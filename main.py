import os

import telebot

# from flask import Flask, request

TOKEN = os.environ.get('TOKEN')

bot = telebot.TeleBot(TOKEN)


# server = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    pass


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
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
    bot.polling()
