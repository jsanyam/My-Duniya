# coding:utf-8
from wtforms import StringField, PasswordField
from flask_wtf import Form
from wtforms.validators import DataRequired, Regexp,ValidationError, Email,Length
from untitled1 import User

def email_exists(form,field):
    if User.query.filter_by(email=field.data).count()>0:#where(User.username == field.data).exists():
        raise ValidationError("User with that email already exists")



class RegisterForm(Form):
    username = StringField('Username',validators=[DataRequired(),Regexp(r'^[a-zA-Z0-9_]+$',
                        message="Username should be one word,letters,"
                        "numbers and underscores only")])
    email=StringField('Email',validators=[DataRequired(),Email(),email_exists])

    password = PasswordField('Password',validators=[DataRequired(),Length(min=6)])

class LoginForm(Form):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])