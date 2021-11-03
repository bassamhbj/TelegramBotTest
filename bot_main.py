import logging

from telegram import Update
from telegram.ext import Updater
from telegram.ext import Dispatcher
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = ''


def start_command(update: Update, context: CallbackContext):
    logger.info("start command called")
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Hi, I am a bot. My name is Skynet.'
    )

def name_commnand(update: Update, context: CallbackContext):
    logger.info("name command called")
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='My name is Skynet.'
    )

def unknown_message(update: Update, context: CallbackContext):
    logger.info("received unkown message")
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='I do not understand what are you saying...'
    )

def init_command_handlers(dispacher: Dispatcher):
    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('name', name_commnand))

def init_message_handlers(dispacher: Dispatcher):
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), unknown_message))

if __name__ == '__main__':
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    init_command_handlers(dispatcher)
    init_message_handlers(dispatcher)

    updater.start_polling()

    updater.idle()

