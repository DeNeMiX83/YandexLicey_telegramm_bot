from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

no_role = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Выбрать роль'),
        ],
    ],
    resize_keyboard=True
)