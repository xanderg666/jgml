from flask import Flask
from flask import render_template

app = Flask(__name__)#nuevo objeto con name


@app.route('/') #recibe un decorador con un string, la ruta es base
def index():
    name = 'Invitado'
    return render_template('index.html',name=name)

@app.route('/client') #recibe un decorador con un string, la ruta es base
def client():
    list_name = ['Test1', 'Test2', 'Test3']
    return render_template('client.html',list + list_name)


if __name__ == '__main__':
    app.run(debug=True,port=8000) # debug y puerto