from flask_wtf import FlaskForm #this is the module to use login
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from index.models import User
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed

class RegistratitonForm (FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email ()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('Cornfirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('sign up')
    
    def validate_username(self, username):
        
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
  
    def validate_email(self, email):
        
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm (FlaskForm):
    
    email = StringField('Email', validators=[DataRequired(), Email ()])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
