from ..models import Emergency,User,Subscribers
from ..models import Emergency,User,Conversation,Reply,Solution
from .forms import ConvoForm,UpdateProfile,chatboxForm,SolutionsForm,Update_emergency,SubscriberForm,EmergencyForm
from .. import db,photos
from . import main
from flask import render_template,redirect,url_for,abort,request,flash
from flask_login import login_required,current_user
from ..email import mail_message
from ..request import article_source,location
import urllib.request,json

@main.route('/', methods = ['GET','POST'])
def index():
  title="Home"
  Form=SubscriberForm()
  formE=EmergencyForm()

  locations=location()
  for x in locations:
    lat=x.latitude
    lon=x.longitude
    latitude=lat
    longitude=lon

  if formE.validate_on_submit():
    category=formE.category.data
    description=formE.description.data

    new_post=Emergency(category=category,description=description,latitude=latitude,longitude=longitude,victim=current_user.username)
    new_post.save_emergency()

    subscriber = Subscribers.query.all()
    for my_subscriber in subscriber:
      mail_message("New emergecy posted","email/new_emergency",my_subscriber.email,emergency = emergency)
      
    return redirect(url_for('main.chatbox',category=new_post.category))

  return render_template('index.html',title=title,subscriber_form=Form,formE=formE,locations=locations)

@main.route('/emergency/<category>')
def emergency(category):
  '''
  view function that renders emergency template with the specific category displaying emergencies by category
  '''
  title=category
  Form=SubscriberForm()
  emergencies=Emergency.get_emergencies(category)
        
  
  return render_template('emergency.html',subscriber_form=Form,title=title,emergencies=emergencies)


# Updating profile
@main.route('/user/<yusername>')
@login_required
def profile(yusername):
  user=User.query.filter_by(username = yusername).first()
  emergencies = Emergency.get_emergency_by_user(current_user.username)
  Form=SubscriberForm() 
  if user is None:
    abort(404)
  return render_template('profile/profile.html',subscriber_form=Form,user = user,emergencies = emergencies)


@main.route('/emergency/conversation/<int:id>', methods=['GET','POST'])
@login_required
def convo(id):
  '''
  view function that renders the conversation page for people to talk
  '''  
  emergency=Emergency.query.filter_by(id=id).first()
  form = ConvoForm()
  Form=SubscriberForm()
  title='Conversations'
  convos=Conversation.get_convos(id)  

  if form.validate_on_submit():
    new_convo=Conversation(emergency_id=id,convo=form.convo.data,posted_by=current_user.username)

    new_convo.save_convo()

    return redirect(url_for('main.convo',id=id))

  return render_template('conversation.html',subscriber_form=Form,ConvoForm=form,title=title,convos=convos,emergency=emergency)  

@main.route('/emergency/conversation/reply/<int:id>', methods=['GET','POST'])
@login_required
def reply(id):
  '''
  view function that renders the reply page for people to reply a conversation
  '''  

  form = ConvoForm()
  title='Reply'
  replies=Reply.get_replies(id)
  Form=SubscriberForm()
  convo=Conversation.query.filter_by(id=id).first()

  if form.validate_on_submit():
    new_reply=Reply(convo_id=id,reply=form.convo.data,posted_by=current_user.username)

    new_reply.save_reply()

    return redirect(url_for('main.reply',id=id))

  return render_template('reply.html',subscriber_form=Form,ConvoForm=form,title=title,replies=replies,convo=convo)  


@main.route('/emergency/new/solution', methods = ['GET','POST'])
@login_required
def new_solution():
  '''
  views function that renders the solution form template in the solution.html
  '''

  form = SolutionsForm()
  title ='new solution'
  Form=SubscriberForm()

  if form.validate_on_submit():
    new_solution = Solution(body =form.solution.data ,title =form.title.data ,posted_by =current_user.username,category = form.category.data )

    new_solution.save_solution()

    return redirect(url_for('main.solution'))

  return render_template('solution_form.html',subscriber_form=Form,form = form,title=title)

@main.route('/emergency/solution', methods = ['GET','POST'])
def solution():
  '''
  this view function is responsible for displaying our the solution on solution.html
  '''
  Form=SubscriberForm()
  accidentSol = Solution.get_solution_by_category('Accidents')
  floodSol = Solution.get_solution_by_category('Floods')
  earthquakeSol = Solution.get_solution_by_category('Earthquakes')
  fluSol = Solution.get_solution_by_category('Flu')
  landslideSol = Solution.get_solution_by_category('Landslide')
  fireSol = Solution.get_solution_by_category('Fire')
  powerSol = Solution.get_solution_by_category('PowerOutage')
  terrorismSol = Solution.get_solution_by_category('Terrorism')
  wildfireSol = Solution.get_solution_by_category('Wildfire')

  return render_template('solution.html',subscriber_form=Form,accidents = accidentSol, floods = floodSol,earthquakes = earthquakeSol,flus = fluSol, landslides = landslideSol,fire = fireSol,power = powerSol,terrorism = terrorismSol,wildfire = wildfireSol)

@main.route("/map")
def map():
  Form=SubscriberForm()

  return render_template('map.html',subscriber_form=Form)
  


@main.route('/chatbox/<category>', methods=['GET','POST'])
@login_required
def chatbox(category):
  '''
  view function that renders chatbox html for chatting
  '''

  if category=='Accidents':
    flash('Thank for Posting the emergency. Please call our \'First Aid & Rescue Team\': \' 0722233333 \' to assist you immediately')    

  elif category=='Floods':
    flash('Thank for Posting the emergency. Please call our \'First Aid & Rescue Team\' : \' 0733344444 \' to assist you immediately')      

  elif category=='Earthquakes':
    flash('Thank for Posting the emergency. Please call our \'Disaster Team\' : \' 0744455555 \' to assist you immediately')      

  elif category=='Flu':
    flash('Thank for Posting the emergency. Please call our \'Health Team\' : \' 0755566666 \' to assist you immediately')        

  elif category=='Fire':
    flash('Thank for Posting the emergency. Please call our \'Fire Extinguisher Team\' : \' 0766677777 \' to assist you immediately')      

  elif category=='Landslide':
    flash('Thank for Posting the emergency. Please call our \'First Aid & Rescue Team\' : \' 0777788888 \' to assist you immediately')      
    
  elif category=='PowerOutage':
    flash('Thank for Posting the emergency. Please call the \'KPLC Team\' : \' 0788899999 \' to assist you immediately')      

  elif category=='Terrorism':
    flash('Thank for Posting the emergency. Please call the \'Police \' : \' 999 \' to assist you immediately')      

  elif category=='Wildfire':
    flash('Thank for Posting the emergency. Please call our \'Fire Extinguisher Team & Animal rescue Team\' : \' 0700011111 \' to assist you immediately')      
  else:
    flash("Welcome to Help centre......")  
              
  form=chatboxForm()  
  Form=SubscriberForm()
  if form.validate_on_submit():
    
    if form.chatbox.data=='Accidents':
      emergencies=Emergency.get_emergencies('Accidents')
      
      return render_template('emergency.html',subscriber_form=Form,emergencies=emergencies)

    elif form.chatbox.data=='Floods':
      emergencies=Emergency.get_emergencies('Floods')

      return render_template('emergency.html',subscriber_form=Form,emergencies=emergencies) 

    elif form.chatbox.data=='Help':
      accidentSol = Solution.get_solution_by_category('Accidents')
      floodSol = Solution.get_solution_by_category('Floods')
      earthquakeSol = Solution.get_solution_by_category('Earthquakes')
      fluSol = Solution.get_solution_by_category('Flu')
      landslideSol = Solution.get_solution_by_category('Landslide')
      fireSol = Solution.get_solution_by_category('Fire')
      powerSol = Solution.get_solution_by_category('PowerOutage')
      terrorismSol = Solution.get_solution_by_category('Terrorism')
      wildfireSol = Solution.get_solution_by_category('Wildfire')

      return render_template('solution.html',subscriber_form=Form,accidents = accidentSol, floods = floodSol,earthquakes = earthquakeSol,flus = fluSol, landslides = landslideSol,fire = fireSol,power = powerSol,terrorism = terrorismSol,wildfire = wildfireSol)

    elif form.chatbox.data=='Home':
      return redirect(url_for('main.index'))

    elif form.chatbox.data=='News':  
      return redirect(url_for('main.article'))
    else:
      flash('Did Not get that Message')

  
  return render_template('chatbox.html', form=form,subscriber_form=Form)

@main.route('/user/<yusername>/update',methods = ['GET','POST'])
@login_required
def update_profile(yusername):
  '''
  View function for rendering te update profile page
  
  Args:
  yusername:The current user's username
  '''
  Form=SubscriberForm()
  user = User.query.filter_by(username = yusername).first()
  if user is None:
    abort(404)

  form = UpdateProfile()
  if form .validate_on_submit():
    user.bio = form.bio.data

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('.profile',subscriber_form=Form,yusername = user.username))

  return render_template('profile/update.html',subscriber_form=Form,form = form)

@main.route('/user/<yusername>/update/pic',methods = ['POST'])
@login_required
def update_pic(yusername):
  '''
  View function that will help a user upload a photo
  '''
  Form=SubscriberForm()
  user = User.query.filter_by(username = yusername).first()
  if 'photo' in request.files:
    filename = photos.save(request.files['photo'])
    path = f'photos/{filename}'
    user.profile_pic_path = path
    db.session.commit()
    
  return redirect(url_for('main.profile',subscriber_form=Form,yusername = yusername))
  

@main.route('/article')
def article():
  '''
  view article page function that returns article details page and its data
  '''
  articles = article_source()
  Form=SubscriberForm()
  return render_template('news.html',subscriber_form=Form,articles=articles)

@main.route('/emergency/update_emergency/<int:id>' , methods=['GET','POST'])
def update_emergency(id):
  '''
  view function that renders update emergency form
  '''
  Form=SubscriberForm()
  u_emergency=Emergency.query.filter_by(id=id).first()
  title='Update Emergency'
  if emergency is None:
    abort(404)

  form=Update_emergency()
  if form.validate_on_submit():
    u_emergency.category=form.category.data
    u_emergency.description=form.description.data    

    db.session.add(u_emergency)
    db.session.commit()

    return redirect(url_for('main.emergency',subscriber_form=Form,category=form.category.data))

  return render_template('updateemergency.html',subscriber_form=Form,title=title,form=form)  

@main.route('/delEmergency/<int:id>')
@login_required
def delEmergency(id):
  '''
  view function that deletes an emergency if only the emergency belongs to the current user
  '''
  Form=SubscriberForm()
  
  emergency_del=Emergency.query.filter_by(id=id).first()

  emergency_del.delete_emergency()

  return redirect(url_for('main.emergency',subscriber_form=Form,category=emergency_del.category))



    


