# encoding utf-8 

from flask import  Flask, request , abort
from flask_restful import Resource, Api, reqparse
from flask import send_from_directory
import os


app = Flask(__name__)
api = Api(app)


class Hotnews(Resource):
    def get(self):
        return {'ok':1, 'data': [{'index':1,'title':'Yamaha', 'icon':'http://120.25.207.78/images/yamaha_1.jpg'},{'index':2, 'title':'Kawai','icon':'http://120.25.207.78/images/kawai_1.jpg'}]}

    def post(self):
        return {'ok':1, 'data': [{'index':1,'title':'Yamaha', 'icon':'http://120.25.207.78/images/yamaha_1.jpg'},{'index':2, 'title':'Kawai','icon':'http://120.25.207.78:8080/images/kawai_1.jpg'}]}

api.add_resource(Hotnews, '/hotnews')


parser = reqparse.RequestParser()
parser.add_argument('imageid')

class Download(Resource):
    def get(self, imageid):
       # if request.method == 'GET':
        if os.path.isfile(os.path.join('images/',imageid)):
            return send_from_directory('images', imageid, as_attachment =True)
        abort(404)

    def post(self):
        args = parser.parse_args()
        imageid = args['imageid']
        if os.path.isfile(os.path.join('images/', imageid)):
            return send_from_directory('images', imageid, as_attachment=True)
        abort(404)

api.add_resource(Download, '/images/<string:imageid>', '/images')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)





