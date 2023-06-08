from telegram import (
    Update, 
    InlineKeyboardMarkup, 
    InlineKeyboardButton,
)
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    """welcome function"""
    # create buttons
    btn1 = InlineKeyboardButton(text='👍: 0', callback_data='like')
    btn2 = InlineKeyboardButton(text='👎: 0', callback_data='dislike')

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

    like_and_dislike_data = update.callback_query.message.reply_markup.inline_keyboard

    like_data = like_and_dislike_data[0][0]
    dislike_data = like_and_dislike_data[0][1]

    
    if callback_data == 'like':
        _, count = like_data.text.split(': ') 
        like_data.text = f'👍: {int(count) + 1}'
    
    if callback_data == 'dislike':
        _, count = dislike_data.text.split(': ')
        dislike_data.text = f'👎: {int(count) + 1}'

    # create buttons
    btn1 = InlineKeyboardButton(text=like_data.text, callback_data=like_data.callback_data)
    btn2 = InlineKeyboardButton(text=dislike_data.text, callback_data=dislike_data.callback_data)

    # create keyboard
    inline_keyboard = [[btn1, btn2]]
    
    update.callback_query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard))