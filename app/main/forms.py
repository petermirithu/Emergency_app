from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import Required
from wtforms import ValidationError
from ..models import Subscribers

class EmergencyForm(FlaskForm):
    category = SelectField(u'Select category', choices = [('Accidents','Accident'),('Floods','Floods'),('Earthquakes','Earthquakes'),('Flu','flu'),('Fire','Fire'),('Landslide','Landslide'),('PowerOutage','Power Outage'),('Terrorism','Terrorism'),('Wildfire','Wildfire')], validators = [Required()])
    description = StringField('write a brief description of the emergency (optional)')    
    submit = SubmitField('Submit')    

class Update_emergency(FlaskForm):
    category = SelectField(u'Select category', choices = [('Accidents','Accident'),('Floods','Floods'),('Earthquakes','Earthquakes'),('Flu','flu'),('Fire','Fire'),('Landslide','Landslide'),('PowerOutage','Power Outage'),('Terrorism','Terrorism'),('Wildfire','Wildfire')], validators = [Required()])    
    description = StringField('write a brief description of the emergency (optional)')    
    submit = SubmitField('Submit')    


class ConvoForm(FlaskForm):
    '''
    class definig convo form
    '''
    convo=TextAreaField('Enter your text',validators=[Required()])     
    submit=SubmitField('post')

class SolutionsForm(FlaskForm):
    '''
    this class defines our solutions form
    '''
    category = SelectField(u'Select category', choices = [('Accidents','Accident'),('Floods','Floods'),('Earthquakes','Earthquakes'),('Flu','flu'),('Fire','Fire'),('Landslide','Landslide'),('PowerOutage','Power Outage'),('Terrorism','Terrorism'),('Wildfire','Wildfire')], validators = [Required()])
    title=StringField('Title of the solution :', validators = [Required()])
    solution = StringField('Write your your solution :', validators = [Required()])
    submit=SubmitField('Submit')
    

class chatboxForm(FlaskForm):
    '''
    class defining the chat form
    '''
    chatbox=TextAreaField('Enter you text')
    submit=SubmitField('Submit')
    
class UpdateProfile(FlaskForm):
    '''
    Class for defining the update profile form
    '''
    bio = TextAreaField('Write something about yourself',validators=[Required()])
    submit = SubmitField('Submit')

class SubscriberForm(FlaskForm):
    '''
    Class for defining the subscribe form
    '''
    email = StringField('Email address',validators=[Required()])
    submit = SubmitField('Subscribe')

    def validate_email(self,data_field):
        '''
        Function to check that one email does not subscribe twice
        '''
        if Subscribers.query.filter_by(email = data_field.data).first():
            raise ValidationError("Account with that email is already subscribed")

        

