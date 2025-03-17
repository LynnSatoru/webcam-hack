import telebot
import sys
import os

try:
  
  chat_id = int(sys.argv[1])
  file = str(chat_id)+'.png'
  bot = telebot.TeleBot("8193457229:AAGH8k1NRdobNGzndOQyA_hJ1hFDhqfI-Aw")
  img = open(file, 'rb')
  bot.send_photo(chat_id, img)
  os.remove(file)

except:
  pass
