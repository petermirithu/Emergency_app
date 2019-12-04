from ..models import Emergency,User,Conversation,Reply,Solution
from .forms import EmergencyForm,ConvoForm,SolutionsForm
from .. import db
from . import main
from flask import render_template,redirect,url_for
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


@main.route('/emergency/new/solution', methods = ['GET','POST'])
def solutionForm():
  '''
  views function that renders the solution form template in the solution.html
  '''

  form = SolutionsForm
  title = ' new solution'

  if form.validate_on_submit():
    new_solution = Solution(body =form.solution.data ,title =form.title.data ,posted_by =current_user.username,category = form.category.data )

    new_solution.save_solution()

    return redirect(url_for('.solution'))

  return render_template('solution_form.html',form = form)

@main.route('/emergency/solution', methods = ['GET','POST'])
def solution():
  '''
  this view function is responsible for displaying our the solution on solution.html
  '''
  accidentSol = Solution.get_solution_by_category(Accident)
  floodSol = Solution.get_solution_by_category(Floods)
  earthquakeSol = Solution.get_solution_by_category(Earthquakes)
  fluSol = Solution.get_solution_by_category(Flu)
  landslideSol = Solution.get_solution_by_category(Landslide)
  fireSol = Solution.get_solution_by_category(Fire)
  powerSol = Solution.get_solution_by_category(PowerOutage)
  terrorismSol = Solution.get_solution_by_category(Terrorism)
  wildfireSol = Solution.get_solution_by_category(Wildfire)

  return render_template('solution.html',accident = accidentSol, floods = floodSol,earthquake = earthquakeSol,flu = fluSol, landslide = landslideSol,fire = fireSol,power = powerSol,terrorism = terrorismSol,wildfire = wildfireSol)

  


