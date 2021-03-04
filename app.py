from telebot import TeleBot
from flask import Flask, request
from telebot.types import Update

app = Flask(__name__)


@app.route("/tg/", methods=['GET', 'POST'])
def tg():
    update = Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200


bot = TeleBot("1627794202:AAE0gGxG93vgxbFwRETiUYQvXwmVphDvAOQ", threaded=False)


@bot.message_handler(content_types=["text"])
def handle(msg):
    bot.send_message(msg.from_user.id, msg.text)
