from flask import Flask, render_template, request, jsonify, app
import werkzeug

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import sqlite3
import json

# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
import os


# {
#     "key": "how are you",
#     "array": ["zero", "one", "two", "three"]
#
# }
# init App
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# conn = sqlite3.connect('db.sqlite')
# cur = conn.cursor()
#
# cur.execute('DROP TABLE IF EXISTS Weather')
# cur.execute('CREATE TABLE Weather (outlook TEXT, temp TEXT, humidity TEXT, windy TEXT, play TEXT)')
# conn.close()

@app.route('/train', methods=['GET', 'POST'])
def index():
    # fetch image file from android to python

    imagefile = flask.request.files['image']
    filename = werkzeug.utils.secure_filename(imagefile.filename)
    print("\nReceived image File name : " + imagefile.filename)
    imagefile.save(filename)

    # vipul's magic

    # search google for progressive solutions

    #generate the query to be searched
    # query =
    #
    # results=[]
    # for j in search(query, tld="co.in", num=10, stop=3, pause=2):
    #     results.append(j)

    #scrape list of solutions from site.













    return jsonify({'outlook': "succesful"})


if __name__ == "__main__":
    app.debug = True
    app.run(debug=True)
