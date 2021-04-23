from aiogram.types import Message
from telebot.types import ReplyKeyboardRemove

from keyboards.default.chief.panel_subordinate_list import panel_subordinates_list
from keyboards.inline.chief import inline_tools_with_subordinates
from loader import bot
from states.chief import ShowSubordinatesState


async def show_panel(user_id):
    panel = panel_subordinates_list(user_id)
    n = len(panel.values["keyboard"])
    await bot.send_message(chat_id=user_id, text=f'Подчиненные: {n}',
                           reply_markup=panel if n != 0 else ReplyKeyboardRemove())
    await bot.send_message(chat_id=user_id, text='Инструменты',
                           reply_markup=inline_tools_with_subordinates)
    await ShowSubordinatesState.Start.set()
