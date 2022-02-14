"""Utils functions."""
from telegram import ReplyKeyboardMarkup, KeyboardButton


def request_location(update):
    location_keyboard = KeyboardButton(text="send_location", request_location=True)  # creating location button object
    custom_keyboard = [[location_keyboard]]  # creating keyboard object
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    update.message.reply_text(
        "Would you mind sharing your location with me?",
        reply_markup=reply_markup,
    )
