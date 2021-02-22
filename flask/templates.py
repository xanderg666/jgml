from flask import Flask
from flask import render_template

app = Flask(__name__)#nuevo objeto con name


@app.route('/') #recibe un decorador con un string, la ruta es base

def hello_world(): # requiere una funcion
    return render_template('index.html')


@app.route('/user1/<nn>')
def usernn(nn='Invitado'):
    return render_template('user.html',nombre = nn)


@app.route('/user/<name>') #la varable name usa para poder capturar desde la barra
def user(name='Jorge'): # Por defecto el nombre
    age = 19
    my_list = [1,2,3,4]
    return render_template('user.html',name = name, age = age,list = my_list)#en el reder se pone la var a enviar al html


if __name__ == '__main__':
    app.run(debug=True,port=8000) # debug y puerto