from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    '''
    Login Form for CRS page
    ------
    - DataRequired is a validator that checks the field is not empty
    - form.hidden_tag() template argument will get replaced with a hidden field that implements the CSRF prevention that we enabled in the configuration
    
    '''
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)