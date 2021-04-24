from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from db import session
from db.data import Users, Roles
from handlers.chief.func import show_chief_panel
from keyboards.default.chief.panel_subordinate_list import panel_subordinates_list
from keyboards.inline import inline_exit
from loader import dp
from states.chief import ChiefRoleState


@dp.message_handler(Text(equals=['Подчиненные']), state=ChiefRoleState.Start)
async def org_with_rob(msg: types.Message, state: FSMContext):
    await show_chief_panel(msg.from_user.id)


