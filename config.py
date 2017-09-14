import os
basedir = os.path.abspath(os.path.dirname(__file__))


# URI is requested by Flask-SQLAlchemy Object relation mapper
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
# migrate repo is folder where we will store SQLAlchemy-mgirate data files

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
#Flask WTF prevents corss site request forgery

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]