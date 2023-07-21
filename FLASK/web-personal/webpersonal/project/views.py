from flask import Blueprint, render_template, request, redirect, url_for
from webpersonal import db
from sqlalchemy import desc
from webpersonal.project.models import Project

project = Blueprint('project', __name__)


@project.route('/project/')
@project.route('/project/index')
def index():
    # Indicamos para recuperar toda la información de la base de datos
    # projects = Project.query.all()
    projects = Project.query.order_by(desc(Project.id)).all()
    db.session.commit()

    return render_template('project/index.html', projects=projects)


@project.route('/project/create')
def create():
    return render_template('project/create.html')


@project.route('/project/insert', methods=['POST'])
def insert():
    # Para Guardar la información, primero debemos recuperar la informaciónd el formulario
    title = request.form.get('title')
    description = request.form.get('description')

    # Segundo, creamos un objeto y le asignamos los valores recuperados del formulario
    project = Project(title, description)

    # Almacenamos la información a la Base de datos
    db.session.add(project)

    # Hacemos la actualización para aplicar los cambios
    db.session.commit()

    # Redireccionamos
    return redirect(url_for('project.index'))


@project.route('/project/edit/<int:id>')
def edit(id):
    # Indicamos que se haga una búsqueda por el id seleccionado, en caso de que no existe, devuelve 404
    project = Project.query.get_or_404(id)

    # Redireccionamos para enviar al formulario en donde se hará la edición
    return render_template('project/edit.html', project=project)


@project.route('/project/update/<int:id>', methods=['POST'])
def update(id):
    # Para Guardar la información, primero debemos recuperar la información del formulario
    project = Project.query.get_or_404(id)
    project.title = request.form.get('title')
    project.description = request.form.get('description')

    # Segundo, creamos un objeto y le asignamos los valores recuperados del formulario

    # Almacenamos la información con la actualización a la Base de datos
    db.session.add(project)

    # Hacemos la actualización para aplicar los cambios
    db.session.commit()

    # Redireccionamos
    return redirect(url_for('project.index'))


@project.route('/project/delete/<int:id>')
def delete(id):
    # Para eliminar la información, primero debemos recuperar el id
    project = Project.query.get_or_404(id)
    # Almacenamos la información con la actualización a la Base de datos
    db.session.delete(project)
    # Hacemos la actulización para aplicar los cambios
    db.session.commit()
    # Redireccionamos
    return redirect(url_for('project.index'))
