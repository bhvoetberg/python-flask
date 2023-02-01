from flask_package import app, db


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/')
# def home():
#     return "Hello World"
