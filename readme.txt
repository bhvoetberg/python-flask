
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
