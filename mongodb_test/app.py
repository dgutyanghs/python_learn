from flask import Flask
from flask_mongoengine import MongoEngine
# flask.ext.mongoengine is depress, using flask_mongoengine installed
# from flask.ext.mongoengine import MongoEngine


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'db':'jikexueyuan'}
db = MongoEngine(app)

@app.route('/')
def hello_world():
    return 'Hello world , this is Alex test Flash'


if __name__ == '__main__':
    app.run()


