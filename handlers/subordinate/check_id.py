from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp
from states.subordinate import SubordinateRoleState


@dp.message_handler(Text(equals=['Узнать свой код']), state=SubordinateRoleState.Start)
async def print_rob_id(msg: types.Message):
    await msg.answer(text='Ваш код: \n'
                          f'{msg.from_user.id}')