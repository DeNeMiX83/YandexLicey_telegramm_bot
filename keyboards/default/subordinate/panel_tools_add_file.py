from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

panel_tools_add_file = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Аудиосообщения'),
            KeyboardButton(text='Фотографии'),
        ],
        [
            KeyboardButton(text='Назад'),
        ],
    ],
    resize_keyboard=True
)