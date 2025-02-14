from wtforms import Form
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, Length, number_range, ValidationError, Optional, Regexp
from wtforms import StringField, PasswordField, SubmitField, IntegerField,SelectField,DecimalField,EmailField

class RegistroForm(Form):   
    matricula = StringField('Matricula')
    edad = IntegerField('Edad')
    nombre = StringField('Nombre')
    apellido = StringField('Apellido')
    email = EmailField('Email')
    