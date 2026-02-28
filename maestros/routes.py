from . import maestros, maestros
import forms
from flask import render_template, request
from models import Maestros
from flask import render_template, request, redirect, url_for
from models import db

@maestros.route("/maestros", methods=["GET", "POST"])
def index():
    create_form=forms.MaestroForm(request.form)
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
        return redirect(url_for('maestros.index'))

    return render_template("maestros/maestros.html", form=create_form)




@maestros.route("/maestros/detalle", methods=["GET", "POST"])
def detalle():
    create_form = forms.MaestroForm(request.form)
    matricula = request.args.get('matricula')
    nombre = ""
    apellidos = ""
    especialidad = ""
    email = ""
    if matricula:
        maestro = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        if maestro:
            nombre = maestro.nombre
            apellidos = maestro.apellidos
            especialidad = maestro.especialidad
            email = maestro.email

    if request.method == "POST" and create_form.validate():
        pass

    return render_template("maestros/detalles.html", matricula=matricula, nombre=nombre, apellidos=apellidos, especialidad=especialidad, email=email)



@maestros.route("/maestros/modificar", methods=["GET", "POST"])
def modificar():
    create_form = forms.MaestroForm(request.form)

    if request.method == 'GET':
        matricula = request.args.get('matricula')
        if matricula:
            maes = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
            if maes:
                create_form.matricula.data = maes.matricula
                create_form.nombre.data = maes.nombre
                create_form.apellidos.data = maes.apellidos
                create_form.especialidad.data = maes.especialidad
                create_form.email.data = maes.email


    if request.method == "POST" and create_form.validate():
        matricula = create_form.matricula.data
        maes = db.session.query(Maestros).filter(Maestros.matricula== matricula).first()
        if maes:
            maes.nombre = create_form.nombre.data
            maes.apellidos = create_form.apellidos.data
            maes.especialidad = create_form.especialidad.data
            maes.email = create_form.email.data
            db.session.add(maes)
            db.session.commit()
            return redirect(url_for('maestros.index'))
    return render_template("maestros/editar.html", form=create_form)




@maestros.route("/maestros/eliminar", methods=["GET", "POST"])
def eliminar():
    create_form = forms.MaestroForm(request.form)

    if request.method == 'GET':
        matricula = request.args.get('matricula')
        if matricula:
            maestro = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
            if maestro:
                create_form.matricula.data = maestro.matricula
                create_form.nombre.data = maestro.nombre
                create_form.apellidos.data = maestro.apellidos
                create_form.especialidad.data = maestro.especialidad
                create_form.email.data = maestro.email

    if request.method == "POST" and create_form.validate():
        matricula = create_form.matricula.data
        maestro = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        if maestro:
            db.session.delete(maestro)
            db.session.commit()
            return redirect(url_for('maestros.index'))
    return render_template("/maestros/eliminar.html", form=create_form)


@maestros.route("/perfill/<nombre>", methods=["GET", "POST"])
def perfil(nombre):
    return f"perfil de {nombre}"
