import os
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackQueryHandler, Filters, MessageHandler, Updater

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(BOT_TOKEN)
updater = Updater(BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

WELCOME_TEXT = "Welcome To Void Protocol,\nShare the group and Get access,\nDon't forget to check the status below"
BUTTON_TEXT = "Open Media"
POPUP_TEXT = "Try To Share 1 More Time Dude"

def welcome(update: Update, context):
    for member in update.message.new_chat_members:
        kb = InlineKeyboardMarkup([[InlineKeyboardButton(BUTTON_TEXT, callback_data='fake_open')]])
        context.bot.send_message(chat_id=update.effective_chat.id, text=WELCOME_TEXT, reply_markup=kb)

def button_click(update: Update, context):
    query = update.callback_query
    query.answer(text=POPUP_TEXT, show_alert=True)

dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))
dispatcher.add_handler(CallbackQueryHandler(button_click, pattern='fake_open'))

if __name__ == '__main__':
    updater.start_polling()
    updater.idle()
