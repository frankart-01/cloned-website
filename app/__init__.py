from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__, static_folder='static')
app.secret_key = "" 
DATABASE_URL = 'postgresql+psycopg2://admin:DB0passw0rd@localhost:5432/staffdb'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

engine = create_engine(DATABASE_URL)

db = SQLAlchemy(app)

# Create a session
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()