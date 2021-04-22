import sqlalchemy

from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Roles(SqlAlchemyBase):
    __tablename__ = 'roles'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    tag = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String)

    users = orm.relation('Users', back_populates='role')

    def __repr__(self):
        return f'id: {self.id}, tag: {self.tag}, name: {self.name}'