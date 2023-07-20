from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    employee_number = StringField('Employee Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class TableAssignmentForm(FlaskForm):
    table = SelectField("Table", coerce=int)
    employee = SelectField("Employee", coerce=int)
    assign = SubmitField("Assign")


class OrderForm(FlaskForm):
    table = SelectField("Table", coerce=int)
    item = SelectField("Item", coerce=int)
    order = SubmitField("Order")