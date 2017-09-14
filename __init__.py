# Creates an app object of class flask then imports views module

from flask import Flask
app = Flask(__name__)

# import statement at end to avoid circular imports
from app import views