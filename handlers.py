import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from main import bot
import strings
import keyboards
markup_sourses = keyboards.gen_markup()

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Ну привет :)")


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, strings.help_msg)


@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(message.chat.id, strings.sourse_question, reply_markup=markup_sourses)
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
        try:
            # write_to_db(get_info_from_mess(answ)[0],get_info_from_mess(answ)[1], get_info_from_mess(answ)[2])
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
            bot.send_message(message.chat.id, strings.success_msg)
        except Exception:
            print("Какая-то ошибочка")
            print(Exception)
            # bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
            bot.send_message(message.chat.id, "Какая-то ошибочка")

bot.polling()