from flask import Flask
from sqlalchemy.orm import backref
from flask_sqlalchemy import SQLAlchemy

# Config
app = Flask(__name__)
app.config['SECRET_KEY'] = 'e0fff506caeff08d660240ee10e953e9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from Flask_App import routes