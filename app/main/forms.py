from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import Required
from wtforms import ValidationError

class EmergencyForm(FlaskForm):
    category = SelectField(u'Select category', choices = [('Accidents','Accident'),('Floods','Floods'),('Earthquakes','Earthquakes'),('Flu','flu'),('Fire','Fire'),('Landslide','Landslide'),('PowerOutage','Power Outage'),('Terrorism','Terrorism'),('Wildfire','Wildfire')], validators = [Required()])
    description = StringField('write a brief description of the emergency (optional)')
    submit = SubmitField('Submit')

class ConvoForm(FlaskForm):
    '''
    class definig convo form
    '''
    convo=SelectField('Enter your text',validators=[Required()])     
    submit=SubmitField('post')   

class chatboxForm(FlaskForm):
    '''
    class defining the chat form
    '''
    chatbox=TextAreaField('Enter you text')
    submit=SubmitField('Submit')
    