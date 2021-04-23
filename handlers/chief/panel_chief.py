from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.chief.panel_subordinate_list import panel_subordinates_list
from loader import dp
from states.chief import ChiefRoleState


@dp.message_handler(Text(equals=['Подчиненные']), state=ChiefRoleState.Start)
async def org_with_rob(msg: types.Message):
    panel = panel_subordinates_list(msg.from_user.id)
    n = len(panel.values["keyboard"])
    await msg.answer(text=f'Подчиненные: {n}',
                     reply_markup=panel if n != 0 else ReplyKeyboardRemove())
