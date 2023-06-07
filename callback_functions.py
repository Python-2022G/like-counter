from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext

like = 0
dislike = 0

def start(update: Update, context: CallbackContext) -> None:
    """welcome function"""
    # create buttons
    btn1 = KeyboardButton(text='👍')
    btn2 = KeyboardButton(text='👎')

    # create keyboard
    keyboard = [[btn1, btn2]]

    # get first name 
    first_name = update.message.chat.first_name

    # send message with two buttons
    update.message.reply_html(
        text=f'Hello, <b>{first_name}</b>. Welcome to our bot!\n\npress one of the buttons.',
        reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    )


def like_or_dislike(update: Update, context: CallbackContext) -> None:
    """welcome function"""
    global like
    global dislike

    if update.message.text == '👍':
        like += 1
    elif update.message.text == '👎':
        dislike += 1

    update.message.reply_html(text=f'<b>likes:</b> {like}\n<b>dislikes:</b> {dislike}')
