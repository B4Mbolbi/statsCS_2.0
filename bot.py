from telebot import types, TeleBot
from token import TOKEN

bot = TeleBot(TOKEN)


@bot.message_handler(commands='start')
def start_admin(message):
    bot.send_message(message.chat.id, 'Выбери что ты хочешь сделать', reply_markup=webAppKeyboard())


@bot.message_handler(content_types="web_app_data")  # получаем отправленные данные
def answer(webAppMes):
    get_funck_webbapp(bot, webAppMes.chat.id, webAppMes.web_app_data.data)


@bot.message_handler(content_types="text")  # получаем отправленные данные
def move(message):
    pass


bot.polling()
