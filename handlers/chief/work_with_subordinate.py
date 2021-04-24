from aiogram import types
from aiogram.dispatcher import FSMContext

from db import session
from db.data import Users
from keyboards.default.chief import panel_tools_with_subordinate
from loader import dp
from states.chief import ShowSubordinatesState
import re


@dp.message_handler(content_types=['text'], state=ShowSubordinatesState.Start)
async def work_with_sub(msg: types.Message, state: FSMContext):
    text = msg.text
    pattern = r'Имя: [\w\s]*\(@\w*\)[\w\s]*: (\d*)'
    text = re.findall(pattern, text)
    if not text:
        return
    user_id = text[0]
    # user = session.query(Users).get(user_id)
    await msg.answer(text='Инструменты',
                     reply_markup=panel_tools_with_subordinate)
    await ShowSubordinatesState.Tools.set()
    data = {'subordinate_id': user_id}
    await state.update_data(data)


@dp.message_handler(Text(equals=['Удалить подчиненного']), state=ShowSubordinatesState.Start)
async def delete_sub(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    user_id = data['subordinate_id']
    user = session.query(Users).get(user_id)
    session.delete(user)
    session.commit()




