import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from callback_functions import (
    start,
    like_or_dislike,
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
    dp.add_handler(handler=MessageHandler(filters=Filters.text(['👍', '👎']), callback=like_or_dislike))


    # start polling
    updater.start_polling()
    updater.idle()

main()
