import telebot
import sqlite3 as sql
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import config
import keyboards
import strings
import usefull
import traceback
import DBC
answer = ""
bot = telebot.TeleBot(config.token)
#con = sql.connect('info.db')



if __name__ == '__main__':
    print("Начинаю работать...")




@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Ну привет :)",reply_markup=keyboards.commands)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, strings.help_msg)

@bot.message_handler(commands=['show_info'])
def start_message(message):
    bot.send_message(message.chat.id, DBC.show_db('inoutcomes'))


@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(message.chat.id, strings.sourse_question, reply_markup=keyboards.gen_markup())
    global answer
    answer = message.text.lower()

    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        global answer
        answ = answer
        if call.data == "UralSib_A":
            answ += " УралСиб_А"
        elif call.data == "Sber_A":
            answ += " Сбер_А"
        elif call.data == "Nal_A":
            answ += " Нал_А"
        elif call.data == "Sber_I":
            answ += " Сбер_И"
        elif call.data == "Nal_I":
            answ += " Нал_И"
        elif call.data == "Nal_kv":
            answ += " Нал_кв"
        try: # write_to_db(from,to,how_much)      get_info_from_mess-> target, price, sourse
            usefull.write_to_db(usefull.get_info_from_mess(answ)[2],usefull.get_info_from_mess(answ)[0], "-"+usefull.get_info_from_mess(answ)[1])
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
            bot.send_message(message.chat.id, strings.success_msg)
        except Exception as e:
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
            bot.send_message(message.chat.id, strings.error_msg)
            print('Ошибка:\n', traceback.format_exc())

bot.polling()

