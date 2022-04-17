from email.policy import default
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, BooleanField, SubmitField, SelectField
from wtforms.validators import  Length, Email, EqualTo,ValidationError,InputRequired
from todoapp.models import User



class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])   
    submit = SubmitField('Sign Up') 
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class TicketForm(FlaskForm):
    name = StringField('Ticket name',validators=[InputRequired()]) 
    label = SelectField('Labels', choices=[('light','White'),('danger', 'Red'), ('primary', 'Blue'), ('success', 'Green')] , default="light")
    status = SelectField('Status', choices=[('todo', 'To do'), ('doing', 'Doing'), ('done', 'Done')],default="todo" ) 
    comment = StringField('Write a comment') 
       
    

class NewTicketForm(FlaskForm):
    name = StringField('Name of ticket', validators=[InputRequired()]) 
    status = HiddenField('Status')
    

# class NewCommentForm(FlaskForm):
#     name = StringField('Comment', validators=[InputRequired()]) 
    
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired('Oppa'), Email()])
    password = PasswordField('Password', validators=[InputRequired('Oppala')]) 
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')    