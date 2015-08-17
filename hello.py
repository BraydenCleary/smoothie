import os
from flask import Flask
import datetime from datetime

app = Flask(__name__)

@app.route('/')
def map():
  return render_template('map.html', now=datetime.now)
