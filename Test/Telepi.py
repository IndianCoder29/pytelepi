from deci import *
from email import message
import os
import telebot

bot = telebot.TeleBot('6207211081:AAE1pgK_ojDDaY_heE3rhOUszfurBoes5jk')
str = ''



def fog(a):
	return True

@bot.message_handler(commands=['Init'])
def Init(message):
	INIT_STATUS = GPIO_Handler.InitPI()
	bot.send_message(message.chat.id,INIT_STATUS)
	
@bot.message_handler(commands=['Help'])
def cmd(message):
	cmds = '/Init\n'+'Turn on led x\n'+'Turn off led x\n'+'turn all leds on cw\n'
	bot.send_message(message.chat.id,cmds)

@bot.message_handler(func=fog)
def sc(message):
	str = message.text
	response = GPIO_Handler.match(str)
	bot.send_message(message.chat.id,response)
	
	




#bot.polling()
bot.infinity_polling()

