from wtforms import Form, StringField, TextField, PasswordField
from wtforms.fields.html5 import EmailField
# import email_validator


# validaciones de formulario
from wtforms import validators


def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio')


class CommentForm(Form):
    # validaciones , usa un segundo parametro de string []
    username = StringField('username',
                           [
                               validators.required('el usuario es requerido'),
                               validators.length(min=4, max=25, message="minimo 4 y max 25")

                           ])
    email = EmailField('email'
                       )
    comment = TextField('Comentario')

    # campo oculto para atacantes
    honeypot = TextField('', [length_honeypot])


class LoginForm(Form):
    username = StringField('username',
                           [
                               validators.required('el usuario es requerido'),
                               validators.length(min=4, max=25, message="minimo 4 y max 25")

                           ])
    password = PasswordField('Password', [validators.required(message='El password es requerido')])
