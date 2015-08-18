import os
from flask import Flask
from datetime import datetime0

app = Flask(__name__)

@app.route('/')
def map():
  "The time is " + str(datetime.now())
