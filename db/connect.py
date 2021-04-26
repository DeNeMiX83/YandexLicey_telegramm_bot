from .data import db_session

db_session.global_init("db/notice.db")
session = db_session.create_session()
