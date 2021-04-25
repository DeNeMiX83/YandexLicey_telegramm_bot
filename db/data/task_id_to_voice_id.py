from datetime import datetime

import sqlalchemy

from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class TaskToVoice(SqlAlchemyBase):
    __tablename__ = 'task_to_voice'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    task_id = sqlalchemy.Column(sqlalchemy.ForeignKey('tasks.id'))
    voice_id = sqlalchemy.Column(sqlalchemy.String)

    task = orm.relation('Tasks')