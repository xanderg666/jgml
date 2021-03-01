from flask import Flask
from flask import render_template
from flask import request

#se agrega el campo del py creado
import forms

app = Flask(__name__,static_folder='templates/static')#nuevo objeto con name


@app.route('/',methods=['POST','GET']) #recibe un decorador con un string, la ruta es base
def index():
    title = 'Curso Flask'
    comment_form = forms.CommentForm(request.form)#Commentform es la clase creada en el archivo forms,
    if request.method == 'POST' and comment_form.validate():
        print(comment_form.username.data)
        print(comment_form.email.data)
        print(comment_form.comment.data)
    else:
        print('Error en el fomulario ')

    return render_template('index.html',title=title, form = comment_form)




if __name__ == '__main__':
    app.run(debug=True,port=8000) # debug y puerto