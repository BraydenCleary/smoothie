import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def map():
  render_template('map.html')
