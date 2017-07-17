# encoding utf-8 

from flask import  Flask, request , abort, Response, jsonify, render_template
from flask_restful import Resource, Api, reqparse
from flask import send_from_directory
import os
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc


app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:password@localhost:3306/popdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Hotnews(Resource):
    def get(self):
        from models import Pianonews
        return jsonify(pianonews = [item.serialize for item in Pianonews.query.order_by(desc(Pianonews.index))]) 
        

    def post(self):
        from models import Pianonews
        # return jsonify(pianonews = [item.serialize for item in Pianonews.query.order_by(desc(Pianonews.index))]) 
        return jsonify(pianonews = [item.serialize for item in Pianonews.query.all()]) 


api.add_resource(Hotnews, '/api/hotnews')


parser = reqparse.RequestParser()
parser.add_argument('imageid')

class Download(Resource):
    def get(self, imageid):
        if os.path.isfile(os.path.join('images/',imageid)):
            return send_from_directory('images', imageid)
        abort(404)


api.add_resource(Download, '/api/images/<string:imageid>')


class VideoInfo(Resource):
    def post(self):
        from models import Videoslist
        return jsonify(videoslist = [item.serialize for item in Videoslist.query.order_by(desc(Videoslist.index))]) 
        # return jsonify(videoslist = [item.serialize for item in Videoslist.query.all()]) 


api.add_resource(VideoInfo, '/api/videoinfo')



@app.route('/videos/<videoid>')
def videohtml(videoid=None):
    if os.path.isfile(os.path.join('videos/', videoid)):
        return render_template('video.html')
    abort(404)



class FlashmobInfo(Resource):
    def post(self):
        from models import Flashmoblist
        return jsonify(flashmobinfolist = [item.serialize for item in Flashmoblist.query.order_by(desc(Flashmoblist.index))]) 
        # return jsonify(videoslist = [item.serialize for item in Videoslist.query.all()]) 

api.add_resource(FlashmobInfo, '/api/flashmobinfo')


class BachInventionInfo(Resource):
    def post(self):
        from models import BachInventionInfo
        return jsonify(bachinventioninfo = [item.serialize for item in BachInventionInfo.query.order_by(desc(BachInventionInfo.index))]) 

api.add_resource(BachInventionInfo, '/api/bachinventioninfo')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081)





