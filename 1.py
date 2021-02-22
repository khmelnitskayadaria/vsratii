import telebot
bot = telebot.TeleBot('1655604294:AAFxRUT-pnpVi3Hji091JhbuG_H83ILoKFY')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('/фильмы', '/сериалы')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, reply_markup=keyboard1)

@bot.message_handler(commands=['фильм', 'фильмы', 'помощь бота'])
def send_film(message):
    bot.reply_to(message, 'https://youtu.be/1eQgfbtl-jU\nProject California\nAmerican honey\nДорогие товарищи')

@bot.message_handler(commands=['сериал', 'сериалы', 'помощь бота'])
def send_tv_show(message):
    bot.reply_to(message, 'Уйн\nSex education\nCommunity\nFinal space\nЭпизоды')

@bot.message_handler(commands=['сохрани фильм', 'сохрани сериал'])
def save_tv_show(message):
    bot.reply_to(message, f'Сорян, {message.from_user.first_name}, но я даун и у меня деменция')


# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text.lower() == 'фильм':
#         bot.send_message(message.from_user.id, 'https://youtu.be/1eQgfbtl-jU\nProject California\nAmerican honey\n')
#     if message.text.lower() == 'сериал':
#         bot.send_message(message.from_user.id, 'Уйн\nSex education\nCommunity\nFinal space\nЭпизоды\n')
#     else:
#         bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')

bot.polling(none_stop=True)