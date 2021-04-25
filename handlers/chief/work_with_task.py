from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from handlers.chief.add_task import show_add_task_panel
from handlers.chief.func import show_tools_with_subordinate, show_work_with_task_panel
from keyboards.default.chief import panel_task
from loader import dp
from states.chief import ShowSubordinatesState, PanelTaskState


@dp.message_handler(Text(equals=['Добавить']), state=PanelTaskState.Start)
async def add_task(msg: Message, state: FSMContext):
    await show_add_task_panel(msg.from_user.id, state)


@dp.message_handler(Text(equals=['Назад']), state=PanelTaskState.Start)
async def start_notice(msg: Message):
    await show_tools_with_subordinate(msg.from_user.id)