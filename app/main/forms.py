from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import Required
from wtforms import ValidationError

class EmergencyForm(FlaskForm):
    category = SelectField(u'Select category', choices = [('Accident','Accident'),('Floods','Floods'),('Earthquakes','Earthquakes'),('Flu','Flu'),('Fire','Fire'),('Landslide','Landslide'),('PowerOutage','PowerOutage'),('Terrorism','Terrorism'),('Wildfire','Wildfire')], validators = [Required()])
    description = StringField('write a brief description of the emergency (optional)')
    location = StringField('Write your location', validators = [Required()]
    submit = SubmitField('Submit')
    

class ConvoForm(FlaskForm):
    '''
    class definig convo form
    '''
    convo=SelectField('Enter your text',validators=[Required()])     
    submit=SubmitField('post')

class SolutionsForm(FlaskForm):
    '''
    this class defines our solutions form
    '''
    category = SelectField(u'Select category', choices = [('Accident','Accident'),('Floods','Floods'),('Earthquakes','Earthquakes'),('Flu','Flu'),('Fire','Fire'),('Landslide','Landslide'),('PowerOutage','PowerOutage'),('Terrorism','Terrorism'),('Wildfire','Wildfire')], validators = [Required()])
    solution = StringField('Write your your solution', validators = [Required()]
    title = StringField('Title of the solution', validators = [Required()])
    submit = StringField('Submit')
