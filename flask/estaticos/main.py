from flask import Flask, url_for
from flask import render_template
from flask import request
from flask import make_response

from flask import session

from flask import redirect


#se agrega el campo del py creado
import forms
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__,static_folder='templates/static')#nuevo objeto con name
app.secret_key = 'hola'
csrf = CSRFProtect(app)



@app.route('/',methods=['POST','GET']) #recibe un decorador con un string, la ruta es base
def index():
    if 'username' in session:
        username = session['username']
        print(username)
    title = 'Curso Flask'
    comment_form = forms.CommentForm(request.form)#Commentform es la clase creada en el archivo forms,
    if request.method == 'POST' and comment_form.validate():
        print(comment_form.username.data)
        print(comment_form.email.data)
        print(comment_form.comment.data)
    else:
        print('Error en el fomulario ')

    return render_template('index.html',title=title, form = comment_form)


@app.route('/login',methods=['POST','GET'])
def login():
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        session['username'] = login_form.username.data

    return render_template('login.html', form = login_form)


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login'))#se regresa la ruta por medio de urlfor


@app.route('/cookie')
def cookie():
    response = make_response( render_template('cookie.html') )
    response.set_cookie('nombrecookie', 'jorge')
    return response

if __name__ == '__main__':
    app.run(debug=True,port=8000) # debug y puerto