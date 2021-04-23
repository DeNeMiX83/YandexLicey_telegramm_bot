from .data import db_session, Roles

db_session.global_init("db/notice.db")
session = db_session.create_session()
roles = {'none': 'Нету',
        'chief': 'Начальник',
        'subordinate': 'Подчиненный'}
# for tag, name in roles.items():
#    role = Roles(tag=tag, name=name)
#    session.add(role)
# session.commit()