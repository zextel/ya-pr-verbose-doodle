# from config import BOT_TOKEN
from telebot import TeleBot

BOT_TOKEN = input("Введите токен для своего бота: ")
bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def bot_start(message):
    print('Получена команда /start')
    bot.send_message(message.chat.id, text="Я готов к работе!")


@bot.message_handler(commands=['help'])
def bot_start(message):
    print('Получена команда /help')
    bot.send_message(message.chat.id, text="Я буду повторять ваши сообщения ^-^")


@bot.message_handler(content_types=['text'])
def send_message(message):
    print(f'Полученo сообщение: {message.text}')
    bot.send_message(message.chat.id, text=f'Вы написали "{message.text}"')


bot.polling()
