from telebot import TeleBot

bot = TeleBot("1627794202:AAE0gGxG93vgxbFwRETiUYQvXwmVphDvAOQ", threaded=False)


@bot.message_handler(content_types=["text"])
def handle(msg):
    bot.send_message(msg.from_user.id, msg.text)


bot.polling()
