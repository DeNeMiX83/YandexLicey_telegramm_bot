from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp


@dp.message_handler(CommandStart(), state='*')
async def bot_start(msg: types.Message):
    name = msg.from_user.full_name
    await msg.answer(f'Привет, {name}')
