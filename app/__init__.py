# Creates an app object of class flask then imports views module

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# import statement at end to avoid circular imports
from app import views, models







