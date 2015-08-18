import os
from flask import Flask
from flask import render_template
from datetime import datetime
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl'))

@app.route('/')
def map():
  # SAN_FRANCISCO_ZIP_CODES = [94102, 94109, 94123, 94117, 94134, 94112, 94124, 94121, 94133, 94116, 94115, 94110, 94127, 94114, 94107, 94132, 94122, 94103, 94105, 94104, 94108, 94118, 94158, 94111, 94131, 94130, 94014, 94129, 94015]
  # # [94014, 94015] not present in sf zip codes I parsed for application

  # WEEKEND_DAYS    = ['Saturday', 'Sunday']
  # EARLY_MORNING   = [5,6,7]
  # LATE_MORNING    = [8,9,10]
  # EARLY_AFTERNOON = [11,12,13]
  # LATE_AFTERNOON  = [14,15,16]
  # EARLY_EVENING   = [17,18,19]
  # LATE_EVENING    = [20,21,22]
  # EARLY_NIGHT     = [23,0,1]
  # LATE_NIGHT      = [2,3,4]

  # def determine_time_of_day_bucket(datetime):
  #   hour = datetime.hour
  #   if hour in EARLY_MORNING:
  #       return 1
  #   elif hour in LATE_MORNING:
  #       return 2
  #   elif hour in EARLY_AFTERNOON:
  #       return 3
  #   elif hour in LATE_AFTERNOON:
  #       return 4
  #   elif hour in EARLY_EVENING:
  #       return 5
  #   elif hour in LATE_EVENING:
  #       return 6
  #   elif hour in EARLY_NIGHT:
  #       return 7
  #   elif hour in LATE_NIGHT:
  #       return 8


  # def parse_for_map(datetime):
  #   zip_predictions = []
  #   for zip in SAN_FRANCISCO_ZIP_CODES:
  #     day_of_month        = datetime.day
  #     time_of_day_bucket  = determine_time_of_day_bucket(datetime)
  #     month_of_year       = datetime.month
  #     year                = datetime.year
  #     DayOfWeek_Friday    = datetime.isoweekday() == 5
  #     DayOfWeek_Wednesday = datetime.isoweekday() == 3
  #     DayOfWeek_Tuesday   = datetime.isoweekday() == 2
  #     DayOfWeek_Thursday  = datetime.isoweekday() == 4
  #     DayOfWeek_Monday    = datetime.isoweekday() == 1
  #     DayOfWeek_Saturday  = datetime.isoweekday() == 6
  #     DayOfWeek_Sunday    = datetime.isoweekday() == 7
  #     is_weekend          = datetime.isoweekday() in [6,7]
  #     zip_predictions.append({zip: model.predict([day_of_month, time_of_day_bucket, month_of_year, year, DayOfWeek_Friday, DayOfWeek_Wednesday, DayOfWeek_Tuesday, DayOfWeek_Thursday, DayOfWeek_Monday, DayOfWeek_Saturday, DayOfWeek_Sunday, is_weekend, zip])[0]})
  #   return zip_predictions

  # data = parse_for_map(datetime.now())
  # do model stuff with current time and pass through model's results
  return render_template('map.html', data={})
