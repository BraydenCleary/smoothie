import os
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def map():
  # "The time is " + str(datetime.now())
  render_template('map.html', name='Brayden')
