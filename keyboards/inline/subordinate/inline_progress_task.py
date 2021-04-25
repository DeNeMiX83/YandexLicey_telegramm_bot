from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import task


def create_panel(task_id):
    panel = InlineKeyboardMarkup()
    panel.add(InlineKeyboardButton(text='Голосовухи', callback_data=task.new(type='in_progress',
                                                                             attribute='voices',
                                                                             info=str(task_id))))

    return panel


inline_progress_task = create_panel