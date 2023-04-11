from deci import *
from email import message
import os
import telebot


bot = telebot.TeleBot('5208741101:AAH7RzGlEqA7MB7vLFGl8LQMZV_il1_l9B0')
str = ''



def fog(a):
	return True


@bot.message_handler(func=fog)
def sc(message):
	str = message.text
	response = GPIO_Handler.match(str)
	bot.send_message(message.chat.id,response)
	
	




#bot.polling()
bot.infinity_polling()

