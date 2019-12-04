from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import Required
from wtforms import ValidationError

class EmergencyForm(FlaskForm):
    category = SelectField(u'Select category', choices = [('Accident','Accident'),('Floods','Floods'),('Earthquakes','Earthquakes'),('Flu','flu'),('Fire','Fire'),('Landslide','Landslide'),('Power Outage','Power Outage'),('Terrorism','Terrorism'),('Wildfire','Wildfire')], validators = [Required()])
    description = StringField('write a brief description of the emergency (optional)')
    location = StringField('Write your location', validators = [Required()])
    submit = SubmitField('Submit')