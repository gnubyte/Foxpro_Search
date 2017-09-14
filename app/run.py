'''
Runs the application web server
------
 - flag in app.run is a boolean, set to false for production value

'''

#!flask/bin/python
from app import app
app.run(debug=True)