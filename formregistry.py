from wtforms import Form, StringField, PasswordField, TextAreaField, validators

class RegisterForm(Form):
    name = StringField('Name', [validators.DataRequired(), validators.Length(min=1, max=25)])
    username= StringField('Username', [validators.DataRequired(), validators.Length(min=1, max=25)])
    email= StringField('Email', [validators.DataRequired(), validators.Length(min=4, max=25)])
    password=PasswordField('Password', [ validators.DataRequired(), validators.EqualTo('confirm', message='Please Retry. Passwords dont match!!')])
    confirm=PasswordField('Confirm Password', [validators.DataRequired()])

class LoginForm(Form):
    username= StringField('Username', [validators.DataRequired(), validators.Length(min=1, max=25)])
    password=PasswordField('Password', [ validators.DataRequired()])

class ForgotPasswordForm(Form):
    email= StringField('Username', [validators.DataRequired(), validators.Length(min=1, max=25)])