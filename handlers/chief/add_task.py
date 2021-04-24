from datetime import datetime

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from data.constant import MONTH
from db import session
from db.data import Tasks
from handlers.chief.func import show_tools_with_subordinate, show_work_with_task_panel
from keyboards.default.chief import panel_task
from keyboards.inline import inline_exit
from keyboards.inline.callback_data import task, exit_calldata
from keyboards.inline.chief import inline_add_task
from loader import dp, bot
from states.chief import PanelTaskState, AddTaskState


@dp.callback_query_handler(task.filter(type='edit', attribute='voice_message'),
                           state=AddTaskState.Add)
async def notice_change_time(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text='Пришли 1 голосовое сообщение',
                              reply_markup=inline_exit('add_task'))
    await AddTaskState.ChangeVoiceMessage.set()


@dp.message_handler(content_types=['voice'], state=AddTaskState.ChangeVoiceMessage)
async def voice_processing(msg: Message, state: FSMContext):
    data = await state.get_data()
    data['voice_id'] = msg.voice.file_id
    await state.set_data(data)
    await msg.answer(text='Сообщение принято')
    await show_add_task_panel(msg.from_user.id, state)


@dp.callback_query_handler(task.filter(type='edit', attribute='contant'), state=AddTaskState.Add)
async def notice_change_contant(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.delete()
    await call.message.answer(text='Отправьте содержание',
                              reply_markup=inline_exit('add_task'))
    await AddTaskState.ChangeContant.set()


@dp.message_handler(content_types=['text'], state=AddTaskState.ChangeContant)
async def notice_edit_contant(msg: Message, state: FSMContext):
    text = msg.text
    data = {'contant': text}
    await state.update_data(data)
    await show_add_task_panel(msg.from_user.id, state)


@dp.callback_query_handler(task.filter(type='save'), state=AddTaskState.Add)
async def notice_change_time(call: CallbackQuery, callback_data: dict, state: FSMContext):
    data = await state.get_data()
    content = data.get('contant', '-')
    subordinate_id = data.get('subordinate_id')
    voice_id = data.get('voice_id', '')
    new_task = Tasks(user_id=subordinate_id,
                     contant=content,
                     voice_id=voice_id)
    session.add(new_task)
    session.commit()
    await state.reset_data()
    await call.message.delete()
    await call.message.answer(text='Задача сохранена')
    await show_work_with_task_panel(call.from_user.id)


@dp.callback_query_handler(task.filter(type='back'), state=AddTaskState.Add)
async def back_from_task(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.delete()
    await show_work_with_task_panel(call.from_user.id)


@dp.callback_query_handler(exit_calldata.filter(type='add_task'), state='*')
async def task_change_data(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.delete()
    await show_add_task_panel(call.from_user.id, state)


async def show_add_task_panel(user_id, state):
    # date_and_time = datetime.today()
    # date = date_and_time.date().strftime('%d.%m.%Y')
    # time = date_and_time.time().strftime('%H:%M')
    contant = '-'
    data = await state.get_data()
    # date = data.get('date', date)
    # time = data.get('time', time)
    contant = data.get('contant', contant)
    await bot.send_message(chat_id=user_id, text='🗒',
                           reply_markup=ReplyKeyboardRemove())
    # f'Дата: {date}\n'
    # f'Время: {time}\n'
    await bot.send_message(chat_id=user_id, text=f'Содержание: \n{contant}',
                           reply_markup=inline_add_task
                           )
    await AddTaskState.Add.set()
