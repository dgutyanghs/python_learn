# encoding utf-8 

from flask import  Flask, request , abort, Response, jsonify, render_template
from flask_restful import Resource, Api, reqparse
from flask import send_from_directory
import os
import json
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:password@localhost:3306/popdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Hotnews(Resource):
    def get(self):
        from models import Pianonews
        return jsonify(pianonews = [item.serialize for item in Pianonews.query.all()]) 
        

    def post(self):
        from models import Pianonews
        return jsonify(pianonews = [item.serialize for item in Pianonews.query.all()]) 


api.add_resource(Hotnews, '/hotnews')


parser = reqparse.RequestParser()
parser.add_argument('imageid')

class Download(Resource):
    def get(self, imageid):
        if os.path.isfile(os.path.join('images/',imageid)):
            return send_from_directory('images', imageid)
        abort(404)


api.add_resource(Download, '/images/<string:imageid>')

# parser.add_argument('videoid')
# class Videoplay(Resource):
#     def get(self, videoid):
#         if os.path.isfile(os.path.join('videos/', videoid)):
#             return render_template('video.html')
#         abort(404)

# api.add_resource(Videoplay, '/videos/<string:videoid>')


@app.route('/videos/<videoid>')
def videohtml(videoid=None):
    if os.path.isfile(os.path.join('videos/', videoid)):
        return render_template('video.html')
    abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)





