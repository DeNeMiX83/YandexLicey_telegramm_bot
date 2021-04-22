import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String)
    age = sqlalchemy.Column(sqlalchemy.Integer)
    position = sqlalchemy.Column(sqlalchemy.String)
    city_from = sqlalchemy.Column(sqlalchemy.String, default=None)
    speciality = sqlalchemy.Column(sqlalchemy.String)
    address = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True)
    hashed = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    modifited_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())

    jobs = orm.relation('Jobs', back_populates='user')

    def set_password(self, password):
        self.hashed = generate_password_hash(str(password))

    def check_password(self, password):
        return check_password_hash(self.hashed, password)

    def __repr__(self):
        return f'<Colonist> {self.id} {self.surname} {self.name}'