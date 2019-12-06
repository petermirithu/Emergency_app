from flask import render_template
from . import main
from .forms import SubscriberForm

@main.app_errorhandler(404)
def fourOfour(error):
  '''
  view function that renders 404 error page when there is a 404 error in the app
  '''
  Form=SubscriberForm()
  return render_template('fourofour.html',subscriber_form=Form),404
  
