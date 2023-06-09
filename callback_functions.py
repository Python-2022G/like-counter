from telegram import (
    Update,
)
from telegram.ext import CallbackContext
from tinydb import TinyDB
from tinydb.table import Document

db = TinyDB('users.json', indent=4)


def start(update: Update, context: CallbackContext) -> None:
    """welcome function"""
    # get user data 
    first_name = update.message.chat.first_name
    chat_id = update.message.chat.id
    username = update.message.chat.username

    if not db.contains(doc_id=chat_id):
        doc = Document(
            value={
                "first_name": first_name,
                "username": username
            },
            doc_id=chat_id
        )
        db.insert(doc)

        # send message
        update.message.reply_html(
            text=f'Hello, <b>{first_name}</b>. Welcome to our bot!\n\nyou are registred.',
        )
    else:
        update.message.reply_html(
            text=f'Hello again, <b>{first_name}</b>. you are already registred.',
        )



def users(update: Update, context: CallbackContext) -> None:
    """welcome function"""
    text = ''
    for user in db.all():
        text += f"{user['chat_id']}: {user['first_name']}\n"
    update.message.reply_html(
        text=text
    )
