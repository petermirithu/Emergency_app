from flask import render_template
from . import main

@main.app_errorhandler(404)
def fourOfour(error):
  '''
  view function that renders 404 error page when there is a 404 error in the app
  '''
  return render_template('fourofour.html'),404
  
