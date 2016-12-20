# encoding:utf8

from flask import  Flask, request , abort
from flask import  send_from_directory
import os

app = Flask(__name__)

@app.route("/images/<imageid>")
def download(imageid):
#  using this link  to download file http://localhost:5000/images/image2.png
#  images/image2.png
    if request.method == "GET":
        if os.path.isfile(os.path.join('images/',imageid)):
            return send_from_directory('images', imageid, as_attachment = True)
        abort(404)




if __name__ == '__main__':
    app.run(debug=True)


