import telebot

token = '1550742706:AAHGxUhxlokRVAZcOUWI-pWS5iMseqWBCdE'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('курс биткоина', 'обменять валюту')
    bot.send_message(message.chat.id, 'это обменник, епт', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'курс биткоина':
        bot.send_message(message.chat.id, 'Сори, парсер в разработке')
    elif message.text.lower() == 'обменять валюту':
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('биток', 'рубли')
        bot.send_message(message.chat.id, 'что хотите обменять', reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, 'функция недоступна или в разработке!')      


 
bot.polling() 
# Запуск кода
# if __name__ == '__main__':
#     main()