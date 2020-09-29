import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from config import DevConfig
from flask_bootstrap import Bootstrap



app = Flask(__name__)
db = SQLAlchemy(app)
bootstrap = Bootstrap()
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

mail = Mail(app)


app = Flask(__name__,instance_relative_config=True)


app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


bootstrap.init_app(app)
db.init_app(app)
login_manager.init_app(app)
mail.init_app(app)


from app import views