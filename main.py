
import telebot

import random
#import textwrap
import simplejson

Tests = simplejson.load(open('test.json', 'r'))
# Tests =[{'q':'', 'a':[]}]
def send_test(m_id):
    curindx=random.randint(0, len(Tests)-1)
    key=telebot.types.InlineKeyboardMarkup()
    randomlist = random.sample(Tests[curindx]['a'][:],len(Tests[curindx]['a']))
    for el in randomlist:
        if el == Tests[curindx]['a'][0]:
            a="yes"
        else:
            a="no"
        kb=telebot.types.InlineKeyboardButton(callback_data=a, text=el)
        key.add(kb)
    bot.send_message(m_id, text=Tests[curindx]['q'], reply_markup=key, disable_web_page_preview=True)


bot = telebot.TeleBot('')

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "yes":
        bot.answer_callback_query(call.id, "Yes")
        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAECN6pggewqpJ4Ld_1oOvmn2JSYWrqvuQACZA0AAoyomEp44GKmn4ZkZB8E')
        send_test(call.message.chat.id)
    elif call.data == "no":
        bot.answer_callback_query(call.id, "No")
        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAECN6hggewed4St7O9glX6z3eNf2FN_JgACPwwAApY8mUpnbPjV8d_pwR8E')
#        send_test(call.message.chat.id)

@bot.message_handler(commands=['start', 'next'])
def start_message(message):
    send_test(message.chat.id)

@bot.message_handler(commands=['quanto'])
def how_much_test(message):
    bot.send_message(message.chat.id, text=f'В базе всего {len(Tests)} тестов. Да прибудет с тобой сила!')

bot.polling(none_stop=False, interval=0, timeout=20)
