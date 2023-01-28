
virtualenv flaskenv -p python3
 . flaskenv/bin/activate

pip install Flask

python
>>
    import flask
    exit()

___

boilerplate
http://www.initializr.com/


---
jinja used base.html for base setup of page
the following is used to address different titles on different pages
  <title>{% block title %} {% endblock %}</title>

index.html inherits base.html:
{% extends "base.html%}


___
in console:
python
from app import app
app.url_map
    Map([<Rule '/feedback' (HEAD, OPTIONS, GET) -> feedback>,
     <Rule '/' (HEAD, OPTIONS, GET) -> home>,
    <Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>])



___
make key for session encoding/decoding:

PyDev console: starting.
Python 3.9.12 (main, Apr  5 2022, 06:56:58)
[GCC 7.5.0] on linux
import os
os.urandom(8)
b'\xda\x8cGU\xe3\x00\xa4\xc0'

___
Form templates
pip install flask-wtf

___
To prevent csrf attacks
{{form.hidden_tag()}}

___
Create columns in class database from console
db.create_all()


___
pip installs:
pip install flask
pip install email_validator
pip install flask-sqlalchemy


___
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
bcrypt.generate_password_hash('testing')
b'$2b$12$kVo0DY367e1IJ95mbTl4x.D5lasKSNq1XhJIrYhfANPl98asGU..G'
bcrypt.generate_password_hash('testing').decode('utf-8')
'$2b$12$xn8C4Jw8lGV9GWza4eoLleIE8xZascgayERBhIT92iVsTOEkkU4Xm'
hashed_pw = bcrypt.generate_password_hash('testing').decode('utf-8')
bcrypt.check_password_hash(hashed_pw, 'password')
False
bcrypt.check_password_hash(hashed_pw, 'testing')
True
