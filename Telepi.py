from deci import *
from email import message
import os
import telebot


bot = telebot.TeleBot('Enter API Token here')
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

