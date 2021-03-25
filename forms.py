from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Optional

class signin(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    ip_address = StringField('IPaddress', validators=[DataRequired()])
    SBA_pass = PasswordField('SBA Password (Optional)', validators=[Optional()])
    submit = SubmitField('Sign In')