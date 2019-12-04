from ..models import Emergency,User,Subscribers
from .forms import EmergencyForm
from ..models import Emergency,User,Conversation,Reply
from .forms import EmergencyForm,ConvoForm,UpdateProfile
from .. import db,photos
from . import main
from flask import render_template,redirect,url_for,abort
from flask_login import login_required,current_user


@main.route('/', methods = ['GET','POST'])
def index():
  EmerForm = EmergencyForm()

  if EmerForm.validate_on_submit():
      new_emergency = Emergency(victim = current_user.username,location = location, category = EmerForm.category.data, description = EmerForm.description.data) 
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
@main.route('/emergency/conversation/<int:id>', methods=['GET','POST'])
def convo(id):
  '''
  view function that renders the conversation page for people to talk
  '''  
  # emergency=Emergency.query.filter_by(id=id).first()
  form = ConvoForm()
  title='Conversations'
  convos=Conversation.get_convos(id)  

  if form.validate_on_submit():
    new_convo=Conversation(emergency_id=id,convo=form.convo.data,posted_by=current_user.username)

    new_convo.save_convo()

    return redirect(url_for('main.convo',id=id))

  return render_template('conversation.html',ConvoForm=form,title=title,convos=convos)  

@main.route('/emergency/conversation/reply/<int:id>', methods=['GET','POST'])
def reply(id):
  '''
  view function that renders the reply page for people to reply a conversation
  '''  

  form = ConvoForm()
  title='Reply'
  replies=Reply.get_replies(id)

  if form.validate_on_submit():
    new_reply=Reply(convo_id=id,reply=form.convo.data,posted_by=current_user.username)

    new_reply.save_reply()

    return redirect(url_for('main.reply',id=id))

  return render_template('reply.html',ConvoForm=form,title=title,replies=replies)  

@main.route('/user/<yusername>/update',methods = ['GET','POST'])
@login_required
def update_profile(yusername):
  '''
  View function for rendering te update profile page
  
  Args:
  yusername:The current user's username
  '''
  user = User.query.filter_by(username = yusername).first()
  if user is None:
    abort(404)

  form = UpdateProfile()
  if form .validate_on_submit():
    user.bio = form.bio.data

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('.profile',yusername = user.username))

  return render_template('profile/update.html',form = form)

@main.route('//user/<yusername>/update/pic',methods = ['POST'])
login_required
def update_pic(yusername):
  '''
  View function that will help a user upload a photo
  '''
  user = User.query.filter_by(username = yusername).first()
  if 'photo' in request.files:
    filename = photos.save(request.files['photo'])
    path = f'photos/{filename}'
    user.profile_pic_path = path
    db.session.commit()
  return redirect(url_for('main.profile',yusername = yusername))
  