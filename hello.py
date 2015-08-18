import os
from flask import Flask
import datetime from datetime

app = Flask(__name__)

@app.route('/')
def map():
  "The time is " + str(datetime.now())
