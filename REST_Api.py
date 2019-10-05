from flask import Flask, render_template, request, jsonify, app
# import werkzeug

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import sqlite3
import json
import pandas as pd
import numpy as np
from fastai.vision import *
from scipy import misc, ndimage
import os
import cv2

# init App
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


@app.route('/train', methods=['GET', 'POST'])
def index():

    count = 0
    flag = request.json['flag']
    a = request.json['result']
    b = request.json['webs1']
    c = request.json['webs2']
    d = request.json['webs3']

    if flag == 1:
        cap = cv2.VideoCapture(0)

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))


        while True and count<5:
            ret, frame = cap.read()
            # if (count % 10 == 0):
            cv2.imwrite("./test_waste/frame%d.jpg" % count, frame)
            cv2.imshow('frame', frame)
            count += 1
            print("hello")

    cap.release()
    cv2.destroyAllWindows()

    #resnet32 used for transfer learning of CNN
    filename = "wet_waste.jpg"

    pic = misc.imread(os.path.join(os.getcwd(), filename))
    dim1 = len(pic)
    dim2 = len(pic[0])
    if dim1 > dim2:
        pic = np.rot90(pic)
    picResized = misc.imresize(pic, 384, 512)
    misc.imsave(os.path.join(os.getcwd(), filename), picResized)
    learn = load_learner(os.getcwd(), 'export.pkl')
    label, index, prob = learn.predict(filename)
    # label contains solid_waste or wet_waste
    print(label)

    search google for progressive solutions
    # generate the query to be searched

    query0 = "list of methods to reduce 'dry' waste" if label == "solid_waste" else "list of methods to reduce 'wet' waste"
    query1 = "home remedies to manage 'dry' waste" if label == "solid_waste" else "home remedies to manage 'wet' waste"
    query2 = "government projects to manage 'dry' waste" if label == "solid_waste" else "government projects to manage 'wet' waste"
    results=[]

    for j in search(query0, tld="co.in", num=10, stop=1, pause=2):
        results.append(j)
    for j in search(query1, tld="co.in", num=10, stop=1, pause=2):
        results.append(j)
    for j in search(query2, tld="co.in", num=10, stop=1, pause=2):
        results.append(j)

    return jsonify({"result": label, "webs1": results[0], "webs2": results[1], "webs3": results[2]})


if __name__ == "__main__":
    app.debug = True
    app.run(host='192.168.43.191',port=5000,debug=True)
