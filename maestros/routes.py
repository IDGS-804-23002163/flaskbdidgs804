from . import maestros, maestros
import forms
from flask import render_template, request
from models import Maestros
from flask import render_template, request, redirect, url_for
from models import db

@maestros.route("/maestros", methods=["GET", "POST"])
@maestros.route("/index")
def index():
    create_form=forms.UsuarioForm(request.form)
    maestros=Maestros.query.all()
    return render_template("maestros/listadoMes.html",form=create_form,maestros=maestros)


@maestros.route("/maestros/nuevo", methods=["GET", "POST"])
def nuevo():
    create_form = forms.MaestroForm(request.form)
    if request.method == "POST" and create_form.validate():
        maestros = Maestros(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            especialidad=create_form.especialidad.data,
            email=create_form.email.data
            )
        db.session.add(maestros)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template("maestros/maestros.html", form=create_form)




@maestros.route("/detalles", methods=["GET", "POST"])
def detalle():
    create_form = forms.MaestroForm(request.form)

    matricula = request.args.get('matricula')
    nombre = ""
    apellidos = ""
    especialidad = ""
    email = ""
    if id:
        maestro = db.session.query(Maestros).filter(Maestros.id == id).first()
        if maestro:
            nombre = maestro.nombre
            apellidos = maestro.apellidos
            especialidad = maestro.correo
            email = maestro.telefono

    if request.method == "POST" and create_form.validate():
        pass

    return render_template("maestros/detalles.html", id=id, nombre=nombre, apellidos=apellidos, especialidad=especialidad, email=email)


@maestros.route("/perfill/<nombre>", methods=["GET", "POST"])
def perfil(nombre):
    return f"perfil de {nombre}"
