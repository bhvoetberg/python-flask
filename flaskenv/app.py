from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def home():
#     return "Hello World "

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


# app.run()

if __name__ == '__main__':
    app.run(debug=True)
