from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery

from db import session
from db.data import Tasks
from keyboards.default import panel_exit
from keyboards.default.subordinate.func import show_tools_with_task
from keyboards.inline.callback_data import task
from keyboards.inline.subordinate import inline_new_task, inline_progress_task
from loader import dp
from states.subordinate import SubordinateRoleState


@dp.message_handler(Text(equals=['Новые']), state=SubordinateRoleState.TaskTools)
async def show_new_task(msg: Message, state: FSMContext):
    user_id = msg.from_user.id
    tasks = session.query(Tasks).filter(Tasks.user_id==user_id, Tasks.progress=='todo').all()
    await msg.answer(text=f'Кличество: {len(tasks)}',
                     reply_markup=panel_exit)
    for task in tasks:
        panel = inline_new_task(task.id)
        await msg.answer(text=f'Содержание: {task.title}',
                         reply_markup=panel)
    await SubordinateRoleState.NewTask.set()


@dp.callback_query_handler(task.filter(type='todo', attribute='start'), state="*")
async def start_new_task(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.delete()
    task_id = callback_data['info']
    task = session.query(Tasks).get(task_id)
    task.progress = 'in_progress'
    session.commit()


@dp.message_handler(Text(equals=['В процессе']), state=SubordinateRoleState.TaskTools)
async def show_progress_task(msg: Message, state: FSMContext):
    user_id = msg.from_user.id
    tasks = session.query(Tasks).filter(Tasks.user_id==user_id, Tasks.progress=='in_progress').all()
    await msg.answer(text=f'Кличество: {len(tasks)}',
                     reply_markup=panel_exit)
    for i, task in enumerate(tasks):
        panel = inline_progress_task(task.id)
        await msg.answer(text=f'Номер: {i + 1}\n'
                              f'Содержание: {task.title}',
                         reply_markup=panel)
    await SubordinateRoleState.ProgressTask.set()


@dp.callback_query_handler(task.filter(type='in_progress', attribute='voices'), state=SubordinateRoleState.ProgressTask)
async def start_new_task(call: CallbackQuery, callback_data: dict, state: FSMContext):
    task_id = callback_data['info']
    task = session.query(Tasks).get(task_id)
    voices = task.voices
    for voice in voices:
        print(voice.voice_id)
        await call.message.answer_audio(audio=voice.voice_id)


@dp.message_handler(Text(equals=['Назад']), state=[SubordinateRoleState.NewTask, SubordinateRoleState.ProgressTask])
async def exit_tools_task(msg: Message, state: FSMContext):
    await show_tools_with_task(msg.from_user.id)
