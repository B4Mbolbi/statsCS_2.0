from telebot import TeleBot, types

def wedAppKeyboard_stats():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создаем клавиатуру
    webAppSelf = types.WebAppInfo("https://b4mbolbi.github.io/get_info_user/")  # создаем webappinfo - формат хранения url
    one_butt = types.KeyboardButton(text="получить стату", web_app=webAppSelf)  # создаем кнопку типа webapp
    keyboard.add(one_butt)  # добавляем кнопки в клавиатуру
    return keyboard  # возвращаем клавиатуру