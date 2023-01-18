from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from logging import DEBUG

app = Flask(__name__)
app.logger.setLevel(DEBUG)
app.secret_key = b'\xda\x8cGU\xe3\x00\xa4\xc0'


# @app.route('/')
# def home():
#     return "Hello World "


response = []


def store_feedback(url):
    response.append(dict(
        url=url,
        user='Me',
        date=datetime.utcnow()
    ))


print(store_feedback("hello"))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == "POST":
        url = request.form['url']
        store_feedback(url)
        app.logger.debug('stored feedback : ' + url)
        flash("Your Feedback: " + url)
        return redirect(url_for('index'))
    return render_template('feedback.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# app.run()

if __name__ == '__main__':
    app.run(debug=True)
