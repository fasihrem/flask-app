from flask import Flask, render_template, request, Response
from werkzeug.utils import secure_filename
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import io

app = Flask(__name__)

image_name = "ibz.png"

data=[
    {
        'name':'Audrin',
        'place': 'kaka',
        'mob': '7736'
    },
    {
        'name': 'Stuvard',
        'place': 'Goa',
        'mob' : '546464'
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/uploader', methods = ['POST', 'GET'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return render_template("other.html", data=data)

@app.route("/interesting/")
def interesting():
    return render_template("interesting.html", data=image_name)

@app.route("/fasih/")
def fasih():
    return render_template("fasih.html")

@app.route("/ibz/")
def ibz():
    return render_template("ibz.html")

@app.route("/afaq/")
def afaq():
    return render_template("afaq.html")

if __name__ == '__main__':
    app.run(debug = True)