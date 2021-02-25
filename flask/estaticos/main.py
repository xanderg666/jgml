from flask import Flask
from flask import render_template

app = Flask(__name__,static_folder='templates/static')#nuevo objeto con name


@app.route('/') #recibe un decorador con un string, la ruta es base
def index():
    title = 'Curso Flask'
    return render_template('index.html',title=title)




if __name__ == '__main__':
    app.run(debug=True,port=8000) # debug y puerto