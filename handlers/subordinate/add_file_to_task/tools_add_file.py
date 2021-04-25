from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery, Message

from handlers.subordinate.func import show_toola_for_add_file
from keyboards.default import panel_exit
from keyboards.default.chief import panel_save_add_file
from keyboards.inline.callback_data import task
from loader import dp, bot
from states.subordinate import SubordinateRoleState, AddFileToTaskState


@dp.callback_query_handler(task.filter(type='in_progress', attribute='add_file'),
                           state=SubordinateRoleState.ProgressTask)
async def tools_add_file(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await show_toola_for_add_file(call.from_user.id, state)


@dp.message_handler(Text(equals=['Аудиосообщения']), state=SubordinateRoleState.ChooseTypeAddFile)
async def button_add_voice(msg: Message):
    await msg.answer(text='Начинайте присылать сообщения',
                     reply_markup=panel_save_add_file)
    await AddFileToTaskState.AddVoice.set()


@dp.message_handler(Text(equals=['Назад']), state=SubordinateRoleState.ChooseTypeAddFile)
async def back_add_file(msg: Message, state: FSMContext):
    data = await state.get_data()
    msg_id = data['msg_id_tools_add_file']
    await bot.delete_message(chat_id=msg.from_user.id, message_id=msg_id)
    await msg.delete()
    msg = await msg.answer('Возвращение',
                           reply_markup=panel_exit)
    await state.set_data({'msg_id_tools_add_file': msg.message_id})
    await SubordinateRoleState.ProgressTask.set()
