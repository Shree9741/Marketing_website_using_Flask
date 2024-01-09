from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,DataRequired,Email,ValidationError
from markets.models import Users


class RegisterForm(FlaskForm):
    
    def validate_username(self,username_to_check):
        user=Users.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('username already exists! Please try different username')
        
    
    def validate_email_address(self,email_addresss_to_check):
        email_address=Users.query.filter_by(email_address=email_addresss_to_check.data).first()
        if email_address:
            raise ValidationError('Email address already exist !Please try with different Email Address') 
    username=StringField(label='User name',validators=[Length(min=2,max=30),DataRequired()])
    email_address=StringField(label='Email Address',validators=[Email(),DataRequired()])
    password1=PasswordField(label='password',validators=[Length(min=6),DataRequired()])
    password2=PasswordField(label='Confirm password',validators=[EqualTo('password1'),DataRequired()])
    submit=SubmitField(label='Create Account')
    
class LoginForm(FlaskForm):
    username=StringField(label='User Name',validators=[DataRequired()])
    password=PasswordField(label='Password',validators=[DataRequired()])
    submit=SubmitField(label='Login')
    
    
class PurchaseItemForm(FlaskForm):
    submit=SubmitField(label='Purchase Item!')
    
    
class SellItemForm(FlaskForm):
    submit=SubmitField(label='Sell Item!')
        
    
    
    
    