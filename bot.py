# import telebot

# bot = telebot.TeleBot("6468217961:AAEIu4zPg8-nvLuhbiGh0yCIQTRda34xow0")

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)

# bot.infinity_polling()


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

logging.BasicConfig(filename="bot.log", level=loging.INFO)    

def greet_user(update, context):
    print('Вызван /start')
    update.message.replay_text('Привет !!! Ты вызвал старт')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    updata.message.replay_text(text)

def main():
    mybot = Updater(bot: PHL063_bot, update_queue: Queue[Token], use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

if __name__ == 
main()