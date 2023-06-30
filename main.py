from deep_translator import GoogleTranslator
import telebot

token = "your_token"
trg = "ru"
greeting = "Привет, я бот переводчик. Отправь мне любой текст и я переведу его на русский!"
bot = telebot.TeleBot(token)
translator = GoogleTranslator(source="auto", target=trg)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, greeting)


@bot.message_handler(content_types=['text'])
def after_text(message):
    bot.send_message(message.chat.id, translator.translate(message.text))


bot.infinity_polling()
