# encoding utf-8 

from flask import  Flask, request , abort
from flask_restful import Resource, Api
from flask import send_from_directory
import os


app = Flask(__name__)
api = Api(app)

class Hotnews(Resource):
    def get(self):
        return {'ok':1, 'data': [{'index':1, 'link':'http://localhost:5000/images/image2.png'},{'index':2, 'link':'http://localhost:5000/images/image1.png'}]}

api.add_resource(Hotnews, '/hotnews')


class Download(Resource):
    def get(self, imageid):
       if request.method == 'GET':
           if os.path.isfile(os.path.join('images/',imageid)):
               return send_from_directory('images', imageid, as_attachment =True)
           abort(404)

api.add_resource(Download, '/images/<string:imageid>')

if __name__ == '__main__':
    app.run(debug=True)





