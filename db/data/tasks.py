from datetime import datetime

import sqlalchemy

from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Tasks(SqlAlchemyBase):
    __tablename__ = 'tasks'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.ForeignKey('users.user_id'))
    contant = sqlalchemy.Column(sqlalchemy.String)
    voice_id = sqlalchemy.Column(sqlalchemy.String)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now())

    user = orm.relation('Users')