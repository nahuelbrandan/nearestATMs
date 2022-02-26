"""
Nearest ATMs - Telegram bot.

First, a few handler functions are defined.
Then, those functions are passed to the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
"""

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from nearest_atms import settings
from nearest_atms.atm_manager import ATMManager
from nearest_atms.utils import request_location, get_logger

logger = get_logger()
atm = ATMManager()


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


def nearest_atm(update: Update, context: CallbackContext) -> None:
    """Get list of the nearest ATMs of the user, of the Link network."""
    location = update.message.location

    if not location:
        context.user_data["network_atm_requested"] = update.message.text
        request_location(update)
    else:
        if context.user_data["network_atm_requested"].lower() == '/link':
            nearest_link_atms = atm.get_nearest_link_atms(location)
        else:
            nearest_link_atms = atm.get_nearest_banelco_atms(location)

        if not nearest_link_atms:
            message = (
                'we did not find an ATM near you\.'
            )
        else:
            message = 'We find the next ATMs near you:\n\n'
            for e in nearest_link_atms:
                message += '\- {}\, dir: {}\.\n'.format(e[3], e[5])

        update.message.reply_markdown_v2(
            message
        )


def not_get_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_markdown_v2(
        'The message is not a command\.\n\n'
        'See /Help for get the command list that you can use\.'
    )


def location_callback(update: Update, context: CallbackContext) -> None:
    """Get the location of the user and continue the process view."""
    nearest_atm(update, context)


def main() -> None:
    """Start the bot."""
    updater = Updater(settings.TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler(["start", "help"], start))
    dispatcher.add_handler(CommandHandler("link", nearest_atm))
    dispatcher.add_handler(CommandHandler("banelco", nearest_atm))
    dispatcher.add_handler(MessageHandler(Filters.location, location_callback))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, not_get_command))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
