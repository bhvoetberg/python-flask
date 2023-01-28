from flask import render_template, request, redirect, url_for, flash
from flask_package import app, bcrypt, db
from flask_package.forms import RegistrationForm, LoginForm
from flask_package.models import User
from datetime import datetime


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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        print(db)
        print(user)
        db.session.commit()
        flash('Account created!')
        return redirect(url_for('login'))
    if form.errors:
        flash('Validation error:' + str(form.errors))
        app.logger.error('Validation error:\n' + str(form.errors))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Logged in')
        return redirect(url_for('index'))
    else:
        flash('Login unsuccessful')
    return render_template('login.html', title='Login', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
