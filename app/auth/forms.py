from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import User
from ..models import Checksheet

#student registration form
class RegistrationForm(FlaskForm):
    
    honors_id = StringField('Honors ID', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), 
                                            EqualTo('confirm_password')
                                            ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')
    
    #check to see if the honors_id is already in the database if no, error
    def validate_honors_id(self, field):
        honors = User.query.filter_by(email=field.data).first()
        #if honors is None:
            #raise ValidationError('That Honors ID is not in the database. Please check your Honors ID and try again.')

    #check to see if the email address is already in the database. if yes, error
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email account is already in use.')
    
#login form on login page         
class LoginForm(FlaskForm):
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# Form logged in User to change password
class ChangePasswordForm(FlaskForm):
    new_password1 = PasswordField('New Password', validators=[DataRequired()])
    new_password2 = PasswordField('New Password', validators=[DataRequired(), EqualTo('new_password1')])
    submit = SubmitField('Change Password')
    
class ResetPasswordEmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Reset Password')
    
# Form for User to request a password change if they have forgotten
class ResetPasswordForm(FlaskForm):
    old_password = PasswordField('Current Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired(), EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired()])
    submit = SubmitField('Reset Password')
    
    