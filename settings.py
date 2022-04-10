import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db_dir = os.path.abspath('data.sqlite')


app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+db_dir
db = SQLAlchemy(app)
