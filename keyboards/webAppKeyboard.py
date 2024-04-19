from telebot import TeleBot, types

def webAppKeyboard(): #создание клавиатуры с webapp кнопкой
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) #создаем клавиатуру
   webAppAdd = types.WebAppInfo("https://b4mbolbi.github.io/StatCs.github.io/") #создаем webappinfo - формат хранения url
   webAppSelf = types.WebAppInfo("https://b4mbolbi.github.io/CheckInfoPerson.github.io./") #создаем webappinfo - формат хранения url
   one_butt = types.KeyboardButton(text="Добавить матч", web_app=webAppAdd) #создаем кнопку типа webapp
   two_butt = types.KeyboardButton(text="Добавить учетку", web_app=webAppSelf) #создаем кнопку типа webapp
   keyboard.add(one_butt,two_butt) #добавляем кнопки в клавиатуру
   return keyboard #возвращаем клавиатуру