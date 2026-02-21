

from flask import Flask, render_template, request, redirect, url_for

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
import forms
from models import db
from models import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

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
            apellido=create_form.apellido.data,
            correo=create_form.correo.data
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
    apellido = ""
    correo = ""
    if id:
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        if alum1:
            nombre = alum1.nombre
            apellido = alum1.apellido
            correo = alum1.correo
    if request.method == "POST" and create_form.validate():
        pass

    return render_template("detalles.html", id=id, nombre=nombre, apellido=apellido, correo=correo)

@app.route("/modificar", methods=["GET", "POST"])
def modificar():
    pass

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.run()

