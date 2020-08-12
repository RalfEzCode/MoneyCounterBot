from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import telebot




# Клавиатура карт
def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("УралСиб_А", callback_data="UralSib_A"), InlineKeyboardButton("Сбер_А", callback_data="Sber_A"), InlineKeyboardButton("Нал_А", callback_data="Nal_A"))
    markup.add(InlineKeyboardButton("Сбер_И", callback_data="Sber_I"), InlineKeyboardButton("Нал_И", callback_data="Nal_I"), InlineKeyboardButton("Нал_кв", callback_data="Nal_kv"))
    return markup


# Клавиатура команд
commands = telebot.types.ReplyKeyboardMarkup(True, True)
commands.row("/show_info","/help")
