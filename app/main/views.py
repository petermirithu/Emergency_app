from flask import render_template,redirect
from .  import main



@main.route('/emergency/<category>')
def emergency(category):
  '''
  view function that renders emergency template with the specific category displaying emergencies by category
  '''
  title=category

  # emergencies=

  return render_template('emergency.html',title=title,emergencies=emergencies)





