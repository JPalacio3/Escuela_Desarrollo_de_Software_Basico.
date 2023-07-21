from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hola():
    # return '<h1>Hola Mundo de FLask</h1>'
    mensaje = 'Hola Mundo con variable de Flask !!!'
    return render_template('index.html', msm=mensaje)


class Blog:
    def __init__(self, titulo, desc):
        self.titulo = titulo
        self.desc = desc


@app.route('/blogs')
def blog():
    b1 = Blog(
        'Qué es Python?',
        'Descripción de Blog 1'
    )

    b2 = Blog(
        'Qué es Flask?',
        'Descripción de Blog 2'
    )

    blogs = [b1, b2]

    return render_template('blog.html', blogs=blogs)


# RECIBIR PARÁMETROS EN LAS URL
@app.route('/saludar')
@app.route('/saludar/<nombre>')
@app.route('/saludar/<nombre>/<edad>')
def saludar(nombre=None, edad=None):
    return render_template('hola.html', nombre=nombre, edad=edad)


if __name__ == '__main__':
    app.run(debug=True)
