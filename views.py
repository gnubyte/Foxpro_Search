# #########
# @Author: Patrick Hastings
# @Title: views
# @Purpose: Serves up different views of the model
# #########

from flask import render_template

from app import views
CompanyName = "Generic"


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title=CompanyName)