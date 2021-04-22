from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from db import session
from db.data import Users
from db.data.roles import Roles
from .func.user import register_user, get_user_panel
from loader import dp


@dp.message_handler(CommandStart(), state='*')
async def bot_start(msg: types.Message):
    user_id = msg.from_user.id
    user_name = msg.from_user.username
    name = msg.from_user.full_name
    user = session.query(Users).get(user_id)
    if not user:
        if not user_name:
            await msg.answer(text='Укажите в настройках имя пользователя')
            await msg.answer(text='Затем отправьте в чат командку /start')
        else:
            register_user(user_id, user_name, name)
    user = session.query(Users).get(user_id)
    panel = await get_user_panel(user_id)
    await msg.answer(f'Привет, {name}'
                     f'\nВаша роль: {user.role.name}',
                     reply_markup=panel
                     )
