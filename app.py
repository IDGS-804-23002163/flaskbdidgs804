

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from config import DevelopmentConfig
import forms
from models import db
from models import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate=Migrate(app,db)
csrf = CSRFProtect()

@app.route("/", methods=["GET", "POST"])
@app.route("/index")
def index():
    create_form = forms.UsuarioForm(request.form)
    alumno = Alumnos.query.all()
    return render_template("index.html", form=create_form, alumnos=alumno)


@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"),404


@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    create_form = forms.UsuarioForm(request.form)
    if request.method == "POST" and create_form.validate():
        alum = Alumnos(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            correo=create_form.correo.data
            #telefono=create_form.telefono.data
        )
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template("alumnos.html", form=create_form)



@app.route("/detalles", methods=["GET", "POST"])
def detalle():
    create_form = forms.UsuarioForm(request.form)

    id = request.args.get('id')
    nombre = ""
    apellidos = ""
    correo = ""
    telefono = ""
    if id:
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        if alum1:
            nombre = alum1.nombre
            apellidos = alum1.apellidos
            correo = alum1.correo
            telefono = alum1.telefono

    if request.method == "POST" and create_form.validate():
        pass

    return render_template("detalles.html", id=id, nombre=nombre, apellidos=apellidos, correo=correo, telefono=telefono)

@app.route("/modificar", methods=["GET", "POST"])
def modificar():
    create_form = forms.UsuarioForm(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        if id:
            alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
            if alum1:
                create_form.id.data = alum1.id
                create_form.nombre.data = alum1.nombre
                create_form.apellidos.data = alum1.apellidos
                create_form.correo.data = alum1.correo
                create_form.telefono.data = alum1.telefono


    if request.method == "POST" and create_form.validate():
        id = create_form.id.data
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        if alum1:
            alum1.nombre = create_form.nombre.data
            alum1.apellidos = create_form.apellidos.data
            alum1.correo = create_form.correo.data
            alum1.telefono = create_form.telefono.data
            db.session.add(alum1)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template("modificar.html", form=create_form)


@app.route("/eliminar", methods=["GET", "POST"])
def eliminar():
    create_form = forms.UsuarioForm(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        if id:
            alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
            if alum1:
                create_form.id.data = alum1.id
                create_form.nombre.data = alum1.nombre
                create_form.apellidos.data = alum1.apellidos
                create_form.correo.data = alum1.correo
                create_form.telefono.data = alum1.telefono



    if request.method == "POST" and create_form.validate():
        id = create_form.id.data
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        if alum1:
            db.session.delete(alum1)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template("eliminar.html", form=create_form)



if __name__ == '__main__':
    csrf.init_app(app)


    with app.app_context():
        db.create_all()
    app.run()
