from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:password@localhost:3306/jikexueyuan"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello world! flask'


if __name__ == '__main__':
    app.run()

