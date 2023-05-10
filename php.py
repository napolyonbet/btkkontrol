import urllib.request
from bs4 import BeautifulSoup
import telegram
from telegram.ext import Updater, CommandHandler
import time

# Telegram bot tokenınızı buraya girin
bot_token = '6065725080:AAFMQbZWXAW7CVGyGVEZi2CE9BTd6hhVJLA'

# Kontrol edeceğiniz URL'leri buraya ekleyin
kontrol_et = ['http://napolyonbet304.com/', 'https://www.napolyonbet305.com/', 'http://napolyonbet300.com/']

def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Napolyonbet BTK site sorgulamaya hoş geldiniz!")

def btk_kontrol(update, context):
    chat_id = update.effective_chat.id

    while True:
        for url in kontrol_et:
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
                req = urllib.request.Request(url, headers=headers)
                html = urllib.request.urlopen(req).read()
                soup = BeautifulSoup(html, 'html.parser')
                span_tags = soup.find_all('span')
                err = 0
                for tag in span_tags:
                    if tag.get_text() == 'Yasadışı bahis TERÖRÜN FİNANSMANINDA kullanılabilmektedir. Yasadışı bahis sitelerine gönderdiğiniz paralar sizi suçlu duruma düşürebilir. Ayrıca yasadışı bahis ve kumar suçtur.':
                        message = url + " Domain BTK Tarafından Engellenmiştir."
                        context.bot.send_message(chat_id=chat_id, text=message)
                        err = 1
                if err == 0:
                    message = url + ' Uygulanan Karar Yoktur.'
                    context.bot.send_message(chat_id=chat_id, text=message)
            except urllib.error.HTTPError as e:
                message = "HTTP Hatası: " + str(e.code) + " " + e.reason
                context.bot.send_message(chat_id=chat_id, text=message)
        
        time.sleep(60)  # 60 saniye bekle

def main():
    updater = Updater(token=bot_token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('btkkontrol', btk_kontrol))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
