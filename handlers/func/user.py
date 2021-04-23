from loader import bot

from db import session
from db.data import Users
from keyboards.default import no_role, panel_chief, panel_subordinate
from states import NoRoleState, ChiefRoleState, SubordinateRoleState


def register_user(user_id, user_name, name):
    user = Users(user_id=user_id,
                 user_name=user_name,
                 name=name,
                 role_id=1)
    session.add(user)
    session.commit()


async def get_user_panel(user_id):
    tag = session.query(Users).get(user_id).role.tag
    panel = no_role
    await NoRoleState.Start.set()
    if tag == 'chief':
        panel = panel_chief
        await ChiefRoleState.Start.set()
    elif tag == 'subordinate':
        panel = panel_subordinate
        await SubordinateRoleState.Start.set()
    return panel


async def show_panel(user_id, text=''):
    panel = await get_user_panel(user_id)
    await bot.send_message(chat_id=user_id,
                           text=text,
                           reply_markup=panel
                           )
