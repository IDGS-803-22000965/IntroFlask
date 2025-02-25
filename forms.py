from wtforms import Form
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, Length, number_range, ValidationError, Optional, Regexp
from wtforms import StringField, PasswordField, SubmitField, IntegerField,SelectField,DecimalField,EmailField
from wtforms import validators

class RegistroForm(Form):   
    matricula = StringField('Matricula',[
        validators.DataRequired(message="El campo Matricula es obligatorio")
    ])
    edad = IntegerField('Edad',[
        validators.DataRequired(message="El campo Edad es obligatorio"),
    ])
    nombre = StringField('Nombre',[
        validators.DataRequired(message="El campo Nombre es obligatorio"),
    ])
    apellido = StringField('Apellido',[
        validators.DataRequired(message="El campo Apellido es obligatorio"),
    ])
    email = EmailField('Email',[
        validators.email(message="El campo debe ser un correo electrónico válido")
    ])
    