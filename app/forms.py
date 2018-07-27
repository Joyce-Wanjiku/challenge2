from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask import Flask
from flask_bootstrap import Bootstrap


Bootstrap(app)

class LoginForm(FlaskForm):
    username = StringField('username',validators=[InputRequired(), Length(min=4,max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4,max=80)])
    remember = BooleanField('remember me')

class RegistrationForm(FlaskForm):
    email = StringField('email',validators=[InputRequired(), Email(message='Invalid email'),Length(max=50)])
    username = StringField('username',validators=[InputRequired(), Length(min=4,max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4,max=80) validators.EqualTo('confirm' , message='password must much')])
    confirm = passwordField('repeat password')
    accept_tos = BooleanField('I accept TOS', [validators.DataRequired()])
