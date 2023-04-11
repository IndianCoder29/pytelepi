from ast import Global
from dec import *
from email import message
import os
import telebot


bot = telebot.TeleBot('6207211081:AAE1pgK_ojDDaY_heE3rhOUszfurBoes5jk')
str = ''
Fg = False
flag = True

def fog(a):
	return True


# @bot.message_handler(commands=['Login'])
# def Init_GPIO(message):
#     #INIT_STATUS = GPIO_Handler.InitPI()
#     bot.send_message(message.chat.id,INIT_STATUS)



@bot.message_handler(commands=['Login'])
def Auth(message):
    global Fg
    Fg = True
    
        

@bot.message_handler(func=fog)
def fun(message):
    global Fg
    if(Fg):
        print(message.text)
    if(message.text == 'start'):
        print('huu')
        Fg = False
        flag = False
    if(not Fg):
        str = message.text
        print(Fg)
        response = GPIO_Handler.match(str)
        bot.send_message(message.chat.id,response)
        


# @bot.message_handler(func=fog)
# def sc(message):
#     str = message.text
#     print(Fg)
#     response = GPIO_Handler.match(str)
#     bot.send_message(message.chat.id,response)
    

	

# bot.polling()
bot.infinity_polling()

	
    
    
	
