from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from handlers.subordinate.func import show_toola_for_add_file
from loader import dp
from states.subordinate import AddFileToTaskState, SubordinateRoleState


@dp.message_handler(content_types=['voice'], state=AddFileToTaskState.AddVoice)
async def add_voice(msg: Message, state: FSMContext):
    data = await state.get_data()
    data['voice_id'] = data.get('voice_id', []) + [msg.voice.file_id]
    await state.set_data(data)


@dp.message_handler(Text(equals=['Сохранить']), state=AddFileToTaskState.AddVoice)
async def save_voice(msg: Message, state: FSMContext):
    data = await state.get_data()
    print(data)
    await msg.answer('Аудиосообщения добавлены')
    await show_toola_for_add_file(msg.from_user.id)