import schedule
import time
import telebot
from telebot import types

bot = telebot.TeleBot("970640600:AAGbcjHy1cO97SdUDChVkwNNyYU0ueHSttw")

def add():
	global msg
	msg = bot.send_message(chat_id='@saveeyes', text='Пора делать упражнение для глаз!')

def dele():
	bot.delete_message(chat_id='@saveeyes', message_id=msg.message_id)
	time.sleep(1)

time.sleep(5820)

msg = bot.send_message(chat_id='@saveeyes', text='Пора делать упражнение для глаз!')
schedule.every(3).hours.do(dele)
schedule.every(3).hours.do(add)

while (1):
	schedule.run_pending();
	time.sleep(1)

bot.polling()
