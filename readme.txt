
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
