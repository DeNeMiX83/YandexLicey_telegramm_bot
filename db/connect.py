from .data import db_session, Roles

db_session.global_init("db/notice.db")
session = db_session.create_session()
roles = {'none': 'Нету',
        'chief': 'Начальник',
        'subordinate': 'Подчиненный'}
