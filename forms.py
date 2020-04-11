from flask_wtf import FlaskForm
from wtforms import TextAreaField,StringField,SubmitField
from wtforms.validators import Length

class textForm(FlaskForm):
    normalText = TextAreaField('Text', validators=[Length(min=2, max=128)])
    key = StringField('Your Key', validators=[Length(min=2, max=20)])
    submit = SubmitField('Encrypt Text')