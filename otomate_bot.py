import logging
import time
import random
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# informasi logging dengan fromat waktu,nama,critical,pesan
logging.basicConfig(filename='otomate_bot.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO
                    )

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Hai {} :), Selamat datang di Otomate Bot. Kamu bisa dengan mudah untuk mendapatkan outline dari sebuah artikel, hanya dengan send linknya ke aku :). Contohnya /read https://www.otamtebot/artikel/python.com" . format((update.message.from_user.first_name) + ' ' + (update.message.from_user.last_name)))

def read(bot, update):
    browser = webdriver.Chrome('C:\Program Files (x86)\Chrome Driver\chromedriver.exe')
    browser.get('https://outline.com/')
    linkbar = browser.find_element_by_id('source')
    link = update.message.text
    linkbar.send_keys(link.replace("/read ",''))
    linkbar.send_keys(Keys.ENTER)
    time.sleep(20)
    bot.send_message(chat_id=update.message.chat_id, text= "Here your link " + browser.current_url)


def about(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Edited by Hari Kesuma")

# def img(bot, update):
#     directory = "C://Users/Hari Kesuma/Pictures/MyerSplash"
#     random_image = random.choice(os.listdir(directory))
#     random_image =  directory + random_image
#     bot.send_photo(chat_id=update.message.chat_id, photo=random_image)

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def main():
    # Create updater and pass in Bot's auth key.
    updater = Updater(token='YOUR_TOKEN')
    # Get dispatcher to register handlers
    dispatcher = updater.dispatcher
    # answer commands
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('read', read))
    dispatcher.add_handler(CommandHandler('about', about))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    # dispatcher.add_handler(CommandHandler('img', img))
    # start the bot
    updater.start_polling()
    # Stop
    updater.idle()


if __name__ == '__main__':
    main()
