from wtforms import Form, StringField, TextField
from wtforms.fields.html5 import EmailField

class CommentForm(Form):
    username = StringField('username')
    email = EmailField('email')
    comment = TextField('Comentario')

