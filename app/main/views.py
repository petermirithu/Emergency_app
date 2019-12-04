from ..models import Emergency,User
from .forms import EmergencyForm
from .. import db
from . import main
from flask import render_template,redirect,url_for,abort
from flask_login import login_required,current_user


@main.route('/', methods = ['GET','POST'])
def index():
  EmerForm = EmergencyForm()

  if EmerForm.validate_on_submit():
      new_emergency = Emergency(victim = current_user.username, category = EmerForm.category.data, description = EmerForm.description.data) 
      new_emergency.save_emergency()

      return redirect(url_for('.index'))
  
  return render_template('index.html', form = EmerForm)

@main.route('/emergency/<category>')
def emergency(category):
  '''
  view function that renders emergency template with the specific category displaying emergencies by category
  '''
  title=category

  emergencies=Emergency.get_emergencies(category)

  return render_template('emergency.html',title=title,emergencies=emergencies)


# Updating profile
@main.route('/user/<yusername>')
def profile(yusername):
  user = User.query.filter_by(username = yusername).first()

  if user is None:
    abort(404)
  return render_template('profile/profile.html',user = user)