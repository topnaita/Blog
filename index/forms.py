from flask_wtf import FlaskForm #this is the module to use login
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistratitonForm (FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email ()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('Cornfirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('sign up')


class LoginForm (FlaskForm):
    
    email = StringField('Email', validators=[DataRequired(), Email ()])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')