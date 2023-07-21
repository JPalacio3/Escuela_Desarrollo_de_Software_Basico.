from webpersonal import db


class Project(db.Model):

    # Asignar el nombre de la tabla
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.Text)

    # Definir el constructor que inicializa la base de datos
    def __init__(self, title, description):
        self.title = title
        self.description = description

    # Definir la representación de la TABLA
    def __repr__(self):
        return f'Project: {self.title}'
