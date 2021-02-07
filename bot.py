import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)

memes = {'https://ibb.co/5Gr6gRH',
'https://ibb.co/StZjYsP',
'https://ibb.co/R36zR9h',
'https://ibb.co/jrbRWzf',
'https://ibb.co/khv7P84',
'https://ibb.co/Kqnvg8q',
'https://ibb.co/9YdLd0f',
'https://ibb.co/wBqtB60'}

@bot.message_handler(commands=['start'])
def welcome(message):
    id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Давай уже кидай мемы")
    markup.add(item1)
    bot.send_message(id, "Давай начнём?", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mem(message):
    id = message.chat.id
    if message.text == "Давай уже кидай мемы":
        for i in memes:
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Мне нравится", callback_data='good')
            item2 = types.InlineKeyboardButton("Скучно", callback_data='bad')
            markup.add(item1, item2)
            bot.send_photo(id, i, reply_markup=markup)




bot.polling(none_stop=True)
