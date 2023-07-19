from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired
# from .models import db, Employee, Table

class LoginForm(FlaskForm):
    employee_number = StringField('Employee Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class TableAssignmentForm(FlaskForm):
    tables = SelectField("Tables", coerce=int)
    servers = SelectField("Servers", coerce=int)
    assign = SubmitField("Assign")