import os
from telegram.ext import (
    Updater, CommandHandler,
)
from callback_functions import (
    start,
    users,
)


# get token from env variables
TOKEN = os.environ.get('TOKEN')


def main():
    # create updater obj
    updater = Updater(token=TOKEN)

    # create dispatcher obj
    dp = updater.dispatcher

    # add handlers
    dp.add_handler(handler=CommandHandler(command='start', callback=start))
    dp.add_handler(handler=CommandHandler(command='users', callback=users))


    # start polling
    updater.start_polling()
    updater.idle()

main()
