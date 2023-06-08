from telegram import (
    Update, 
    InlineKeyboardMarkup, 
    InlineKeyboardButton,
)
from telegram.ext import CallbackContext

like = 0
dislike = 0

def start(update: Update, context: CallbackContext) -> None:
    """welcome function"""
    # create buttons
    btn1 = InlineKeyboardButton(text='👍', callback_data='like button')
    btn2 = InlineKeyboardButton(text='👎', callback_data='dislike button')

    # create keyboard
    inline_keyboard = [[btn1, btn2]]

    # get first name 
    first_name = update.message.chat.first_name

    # send message with two buttons
    update.message.reply_html(
        text=f'Hello, <b>{first_name}</b>. Welcome to our bot!\n\npress one of the buttons.',
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    )


def callback_func(update: Update, context: CallbackContext) -> None:
    """welcome function"""
    callback_data = update.callback_query.data

    global like
    global dislike

    if callback_data == 'like button':
        like += 1
    if callback_data == 'dislike button':
        dislike += 1

    chat_id = update.callback_query.from_user.id
    context.bot.sendMessage(chat_id=chat_id, text=f'<b>likes:</b> {like}\n<b>dislikes:</b> {dislike}', parse_mode='HTML')
