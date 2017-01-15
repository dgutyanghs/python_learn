# encoding utf-8 

from flask import  Flask, request , abort, Response, jsonify
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
        # return {'ok':1, 'data': [{'index':1,'title':'Yamaha', 'icon':'https://120.25.207.78/images/yamaha_1.jpg'},{'index':2, 'title':'Kawai','icon':'https://120.25.207.78/images/kawai_1.jpg'}]}
        # piano_news = Pianonews.query.all()
        # piano_jsons = map(str, piano_news)
        # return jsonify(piano_news) 
        return jsonify(pianonews = [item.serialize for item in Pianonews.query.all()]) 
        

    def post(self):
        from models import Pianonews
        # return {'ok':1, 'data': [{'index':1,'title':'Yamaha', 'icon':'https://120.25.207.78/images/yamaha_1.jpg'},{'index':2, 'title':'Kawai','icon':'https://120.25.207.78/images/kawai_1.jpg'}]}
        # jsons = []
        return jsonify(pianonews = [item.serialize for item in Pianonews.query.all()]) 


api.add_resource(Hotnews, '/hotnews')


parser = reqparse.RequestParser()
parser.add_argument('imageid')

class Download(Resource):
    def get(self, imageid):
       # if request.method == 'GET':
        if os.path.isfile(os.path.join('images/',imageid)):
            #return send_from_directory('images', imageid, as_attachment =True)
            return send_from_directory('images', imageid)
        abort(404)

#    def post(self):
#        args = parser.parse_args()
#        imageid = args['imageid']
#        if os.path.isfile(os.path.join('images/', imageid)):
#            return send_from_directory('images', imageid, as_attachment=True)
#        abort(404)

#api.add_resource(Download, '/images/<string:imageid>', '/images')
api.add_resource(Download, '/images/<string:imageid>')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

#def application(environ, start_response):
#
#    response_body = "<h1>Hello World wsgi </h1>"
#
#    header = [('Content-Type', 'text/html')]
#    status = "200 OK"
#
#    start_response(status, header)
#
#    print "environ http request method:"+environ['REQUEST_METHOD']
#
#    return [response_body]
#
#if __name__ == '__main__':
#	from wsgiref.simple_server import make_server
#	httpd = make_server("0.0.0.0", 8080, application)
#	print "httpd run on :"+str(httpd.server_port)
#	httpd.serve_forever()




