# 09/09/19 15:42
import sys
import time
import json
import telepot
import telegram
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton


# def convert_list_in_str(list):
#     html_text = ''
#     for x, y in list:
#         y = '<b>' + str(y)
#         myString = ''.join(str(x))
#         html_text = html_text + myString + ' - ' + str(y) + ' руб.</b>' + '\n'
#     return html_text

def convert_list_in_str(list):
    html_text = ''
    for x in list:
        myString = ''.join(str(x))
        html_text = html_text + myString + '\n'+'\n'
    return html_text

def main_markup():
   w_bokal_btn = KeyboardButton(text='Вино по бокалам')
   w_botl_btn = KeyboardButton(text='Вино по бутылкам')
   vodka_btn = KeyboardButton(text='Крепкие напитки')
   coctail_btn = KeyboardButton(text='КОКТЕЙЛЬНАЯ КАРТА')
   markup = ReplyKeyboardMarkup(keyboard=[[w_bokal_btn], [w_botl_btn], [vodka_btn], [coctail_btn]])
   return markup

def w_bokal_markup():
    global back_main_menu
    w_bokal_red_btn = KeyboardButton(text='Красное (бокал)')
    w_bokal_white_btn = KeyboardButton(text='Белое (бокал)')
    w_bokal_pink_btn = KeyboardButton(text='Розовое (бокал)')
    w_bokal_strong_btn = KeyboardButton(text='Креплёное (бокал)')
    w_bokal_desert_btn = KeyboardButton(text='Десертное (бокал)')
    w_bokal_sparkling_btn = KeyboardButton(text='Игристое (бокал)')
    back_main_menu = KeyboardButton(text='Назад')
    markup = ReplyKeyboardMarkup(keyboard=[[w_bokal_red_btn], [w_bokal_white_btn],
                                           [w_bokal_pink_btn], [w_bokal_strong_btn],
                                           [w_bokal_desert_btn], [w_bokal_sparkling_btn], [back_main_menu]])
    return markup

def spisok_maker (name_of_wine):
    with open('alcohol.json', 'r', encoding='utf-8') as f:
        korobka = json.load(f)
    name = ''
    y = 0
    name = list(korobka[0].keys())
    for i in korobka:
        name = list(korobka[y].keys())
        if name[0] == name_of_wine:
            wine = i[name[0]]
        y = y + 1
    return convert_list_in_str(wine)

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat Message:', content_type, chat_type, chat_id,'Tекст сообщения юзера ---- "', msg['text'],'"')
    if content_type == 'text':
        if msg['text'] == '/start':
            bot.sendMessage(chat_id, 'выберите напиток', reply_markup= main_markup())
        elif msg['text'] == 'Вино по бокалам':
            bot.sendMessage(chat_id, 'выберите вино по бокалам', reply_markup= w_bokal_markup())
        elif msg['text'] == 'Белое (бокал)':
            bot.sendMessage(chat_id, spisok_maker("Белые вина (бокалы)"), parse_mode=telegram.ParseMode.HTML)
        elif msg['text'] == 'Красное (бокал)':
            bot.sendMessage(chat_id, spisok_maker("Красные вина (бокалы)"), parse_mode=telegram.ParseMode.HTML)
        elif msg['text'] == 'Розовое (бокал)':
            bot.sendMessage(chat_id, spisok_maker("Розовые вина (бокалы)"), parse_mode=telegram.ParseMode.HTML)
        elif msg['text'] == 'Креплёное (бокал)':
            bot.sendMessage(chat_id, spisok_maker("Креплёные вина (бокалы)"), parse_mode=telegram.ParseMode.HTML)
        elif msg['text'] == 'Десертное (бокал)':
            bot.sendMessage(chat_id, spisok_maker("Десертные вина (бокалы)"), parse_mode=telegram.ParseMode.HTML)
        elif msg['text'] == 'Игристое (бокал)':
            bot.sendMessage(chat_id, spisok_maker("Игристые вина (бокалы)"), parse_mode=telegram.ParseMode.HTML)
        else:
            bot.sendMessage(chat_id, 'выберите напиток', reply_markup=main_markup())

TOKEN = '869400286:AAEnJt8AAzgypKOrh0UYf5lNqeEMak4d4ek' # Robot-hobot
# TOKEN = '704863029:AAH271XQgaiUPOQ1jJniNDw3kToGuN2Exog'  # lednikmenu_bot

SetProxy = telepot.api.set_proxy("http://136.243.47.220:3128")
bot = telepot.Bot(TOKEN)
print('Listening ...')
bot.message_loop({'chat': on_chat_message}, run_forever=True)