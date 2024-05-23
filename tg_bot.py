Telebot
from telebot import TeleBot, types
import random

bot = TeleBot(token='', parse_mode='html') # создание бота

#библиотека машин:
Audi_Q = "Audi Q7 3.0 TDI 286 hp quattro \nhttps://www.auto-data.net/en/audi-q7-typ-4m-50-tdi-v6-286hp-quattro-mild-hybrid-tiptronic-35842"
Volkswagen = "Volkswagen Touareg \nhttps://vw-cars.ru/touareg/"
Toyota = "Toyota Highlander \nhttps://toyota-nevsky.ru/toyota/highlander/about"
Audi_A = "Audi A8 \nhttps://new-audi.ru/brands/audi/a8"
BMW = "BMW 7 серии \nhttps://www.bmw.ru/ru/all-models/7-series/sedan/2019/bmw-7-series-sedan-inspire.html#tab-0"
Mercedes = "Mercedes-Benz S600 \nhttps://www.mercedes-benz.com/en/vehicles/mercedes-benz/s-class/"
Ferrari = "Ferrari LaFerrari \nhttps://www.ferrari.com/en-EN/auto/laferrari"
Porsche = "Porsche 911 Turbo S \nhttps://porsche.ru/models/911/911-turbo-models/911-turbo-s/index.html"
Lamborghini = "Lamborghini Huracán \nhttps://www.drive.ru/brands/lamborghini/models/2014/huracan"
VW = "Volkswagen Golf \nhttps://www.volkswagen.co.uk/en/new/golf.html"
Audi__A = "Audi A3 \nhttps://www.drive.ru/brands/audi/models/2020/a3_sedan"
Audi__Q = "Audi Q5 \nhttps://www.drive2.ru/cars/audi/q5/g61/"
VW_ = "Volkswagen Tiguan \nhttps://www.drive.ru/brands/volkswagen/models/2020/tiguan"
Porsche_ = "Porsche Macan \nhttps://porsche.ru/models/macan/macan-models/macan/index.html"


# обработчик команды '/start'
@bot.message_handler(commands=['start'])
@bot.message_handler(func=lambda x: x.text == 'Назад')

def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Проходимость🚗")
    btn2 = types.KeyboardButton("Премиальность🚨")
    btn3 = types.KeyboardButton("Скорость🏎")
    btn4 = types.KeyboardButton("Семейный комфорт👨‍👩‍👧‍👦")
    btn5 = types.KeyboardButton("Маленький городской🚘")
   
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, text="Добрый день, {0.first_name}! Выберите характеристику машины, которая Вам важна.".format(message.from_user), reply_markup=markup)
    
# обработчик всех остальных сообщений    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Проходимость🚗"):
     bot.send_message(message.chat.id,"Выберите марку автомобиля.\n\n")
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Volkswagen")
     btn2 = types.KeyboardButton("Audi_Q")
     btn3 = types.KeyboardButton("Toyota") 
     btn4 = types.KeyboardButton("Назад")   
     btn5 = types.KeyboardButton("Подходит!")  
     markup.add(btn1, btn2, btn3, btn4, btn5)
     bot.send_message(message.chat.id,text="Хорошенько подумайте!", reply_markup=markup)
  
    elif(message.text == "Audi_Q"):
     bot.send_message(message.chat.id,"Вам подходит:\n\n{0}".format(Audi_Q))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     
    elif(message.text == "Volkswagen"):
     bot.send_message(message.chat.id,"Вам подходит:\n\n{0}".format(Volkswagen))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    elif(message.text == "Toyota"):
     bot.send_message(message.chat.id,"Вам подходит:\n\n{0}".format(Toyota))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    elif(message.text == "Подходит!"):
     bot.send_message(message.chat.id,text="Удачных поездок!😇")
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)


    if(message.text == "Премиальность🚨"):
     bot.send_message(message.chat.id,"Выберите марку автомобиля.\n\n")
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("BMW")
     btn2 = types.KeyboardButton("Audi_A")
     btn3 = types.KeyboardButton("Mercedes") 
     btn4 = types.KeyboardButton("Назад")   
     btn5 = types.KeyboardButton("Беру!")  
     markup.add(btn1, btn2, btn3, btn4, btn5)
     bot.send_message(message.chat.id,text="Хорошенько подумайте!", reply_markup=markup)
  
    elif(message.text == "Audi_A"):
     bot.send_message(message.chat.id,"Вам подходит:\n\n{0}".format(Audi_A))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     
    elif(message.text == "BMW"):
     bot.send_message(message.chat.id,"Вам подходит:\n\n{0}".format(BMW))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    elif(message.text == "Mercedes"):
     bot.send_message(message.chat.id,"Вам подходит:\n\n{0}".format(Mercedes))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    elif(message.text == "Беру!"):
     bot.send_message(message.chat.id,text="Удачных поездок!😇")
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)


    if(message.text == "Скорость🏎"):
     bot.send_message(message.chat.id,"Выберите марку автомобиля.\n\n")
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Ferrari")
     btn2 = types.KeyboardButton("Porsche")
     btn3 = types.KeyboardButton("Lamborghini") 
     btn4 = types.KeyboardButton("Назад")   
     btn5 = types.KeyboardButton("Отлично!")  
     markup.add(btn1, btn2, btn3, btn4, btn5)
     bot.send_message(message.chat.id,text="Хорошенько подумайте!", reply_markup=markup)
  
    elif(message.text == "Ferrari"):
     bot.send_message(message.chat.id,"Вам подходит:\n\n{0}".format(Ferrari))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     
    elif(message.text == "Porsche"):
     bot.send_message(message.chat.id,"Вам подходит:\n\n{0}".format(Porsche))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    elif(message.text == "Lamborghini"):
     bot.send_message(message.chat.id,"Вам подходит:\n\n{0}".format(Lamborghini))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    elif(message.text == "Отлично!"):
     bot.send_message(message.chat.id,text="Удачных поездок!😇")
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)


    if(message.text == "Семейный комфорт👨‍👩‍👧‍👦"):
     bot.send_message(message.chat.id,"Выберите марку автомобиля.\n\n")
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Audi__Q")
     btn2 = types.KeyboardButton("VW_")
     btn3 = types.KeyboardButton("Porsche_") 
     btn4 = types.KeyboardButton("Назад")   
     btn5 = types.KeyboardButton("Здорово!")  
     markup.add(btn1, btn2, btn3, btn4, btn5)
     bot.send_message(message.chat.id,text="Хорошенько подумайте!", reply_markup=markup)
  
    elif(message.text == "Audi__Q"):
     bot.send_message(message.chat.id,"Вам подходит:\n\n{0}".format(Audi__Q))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     
    elif(message.text == "VW_"):
     bot.send_message(message.chat.id,"Вам подходит:\n\n{0}".format(VW_))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    elif(message.text == "Porsche_"):
     bot.send_message(message.chat.id,"Вам подходит:\n\n{0}".format(Porsche_))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    elif(message.text == "Здорово!"):
     bot.send_message(message.chat.id,text="Удачных поездок!😇")
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)


    if(message.text == "Маленький городской🚘"):
     bot.send_message(message.chat.id,"Выберите марку автомобиля.\n\n")
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("VW")
     btn2 = types.KeyboardButton("Audi__A")
     btn3 = types.KeyboardButton("Назад")   
     btn4 = types.KeyboardButton("Годится!")  
     markup.add(btn1, btn2, btn3, btn4)
     bot.send_message(message.chat.id,text="Хорошенько подумайте!", reply_markup=markup)
  
    elif(message.text == "VW"):
     bot.send_message(message.chat.id,"Вам подходит:\n\n{0}".format(VW))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     
    elif(message.text == "Audi__A"):
     bot.send_message(message.chat.id,"Вам подходит:\n\n{0}".format(Audi__A))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    elif(message.text == "Годится!"):
     bot.send_message(message.chat.id,text="Удачных поездок!😇")
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)






# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
