from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bc791cc0f3019a2c976d81673700b245'
if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URL'] = os.getenv("DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_criarconta'
login_manager.login_message_category = 'alert-info'

from comunidadeimpressionadora import routes
