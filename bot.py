import os
from telegram.ext import (
    Updater, CommandHandler, 
    MessageHandler, Filters, 
    CallbackQueryHandler,
)
from callback_functions import (
    start,
    callback_func,
)

# get token from env variables
TOKEN = os.environ.get('TOKEN')


def main():
    # create updater obj
    updater = Updater(token=TOKEN)

    # create dispatcher obj
    dp = updater.dispatcher

    # add handlers
    dp.add_handler(handler=CommandHandler(command=['start', 'boshlash'], callback=start))
    dp.add_handler(handler=CallbackQueryHandler(callback=callback_func))


    # start polling
    updater.start_polling()
    updater.idle()

main()
