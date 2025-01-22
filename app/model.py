from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from app import engine, db


Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False)
    staff_id = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(256), nullable=False)

    def __init__(self, username:str, staff_id:str, password:str):
        self.username = username
        self.staff_id = staff_id
        self.password = password

Base.metadata.create_all(engine)

