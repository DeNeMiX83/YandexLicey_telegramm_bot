from aiogram.dispatcher.filters import Text

from handlers.func.user import get_user_panel, show_panel
from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(Text(equals=['Назад']), state='*')
async def back(msg: types.Message, state: FSMContext):
    await state.finish()
    await show_panel(msg.from_user.id, 'Возвращение')


@dp.message_handler(state='*')
async def bot_echo(msg: types.Message, state: FSMContext):
    await show_panel(msg.from_user.id, 'Произошла ошибка')
