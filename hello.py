import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def map():
  render_template('map.html')
