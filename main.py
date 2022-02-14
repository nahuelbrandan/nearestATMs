"""
Nearest ATMs - Telegram bot.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
"""

import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import settings

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    message = (
        'I can help you to locate the nearest ATMs around you\.\n\n'
        'You can control me by sending these commands:\n\n'
        '/Link \- Get the list of the nearest ATMs of the **Link network**\n'
        '/Banelco \- Get the list of the nearest ATMs of the **Banelco network**'
    )

    update.message.reply_markdown_v2(
        message
    )


def link(update: Update, context: CallbackContext) -> None:
    """Get list of the nearest ATMs, of the Link network."""
    message = (
        'Get list of nearest ATMs, of the Link network\.'
    )

    update.message.reply_markdown_v2(
        message
    )


def banelco(update: Update, context: CallbackContext) -> None:
    """Get list of the nearest ATMs, of the Banelco network."""
    message = (
        'Get list of nearest ATMs, of the Banelco network\.'
    )

    update.message.reply_markdown_v2(
        message
    )


def not_get_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_markdown_v2(
        'The message is not a command\.\n\n'
        'See /Help for get the command list that you can use\.'
    )


def main() -> None:
    """Start the bot."""
    updater = Updater(settings.TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler(["start", "help"], start))
    dispatcher.add_handler(CommandHandler("link", link))
    dispatcher.add_handler(CommandHandler("banelco", banelco))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, not_get_command))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
