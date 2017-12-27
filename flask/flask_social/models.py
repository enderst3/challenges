import datetime

from flask.ext.login import UserMixin
from flask.ext.bcrypt import generate_password_hash, check_password_hash
from peewee import *

DATABASE = SqliteDatabase('social.db')

class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default=False)

    class Meta:
        database = DATABASE
        '''newest mebers first in the db.  the - will do that for us'''
        order_by = ('-joined_at', )

    '''cls will create the model instance when it runs the method.  Basically calls User.create'''
    @classmethod
    def create_user(cls, username, email, password, admin=False):
        try:
            cls.create(
                username=username,
                email=email,
                password=generate_password_hash(password),
                is_admin=admin)
        except IntegrityError:
            raise ValueError('User already exists')      

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()