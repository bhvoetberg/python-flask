from flask import Flask
from logging import DEBUG
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = b'\x8d\x07t\xe3\xf4Q\xb1Y'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.logger.setLevel(DEBUG)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flask_package import routes