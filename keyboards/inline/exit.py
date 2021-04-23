from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import exit_calldata


def create_panel(type):
    panel = InlineKeyboardMarkup()
    panel.add(InlineKeyboardButton(text='Назад', callback_data=exit_calldata.new(type=type)))
    return panel


inline_exit = create_panel