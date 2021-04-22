from db import session
from db.data import Users
from keyboards.default import no_role
from states import NoRoleState


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
    return panel