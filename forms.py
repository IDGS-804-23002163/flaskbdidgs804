from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, IntegerField
from wtforms.validators import DataRequired


class UsuarioForm(FlaskForm):
    id = IntegerField(
        "id"
    )
    nombre = StringField(
        "nombre", validators=[DataRequired(message="elcampo es requerido")]
    )
    apellidos = StringField(
        "apellidos", validators=[DataRequired(message="elcampo es requerido")]
    )
    correo = EmailField(
        "correo", validators=[DataRequired(message="elcampo es requerido")]
    )
    telefono = StringField(
        "telefono", validators=[DataRequired(message="elcampo es requerido")]
    )


class MaestroForm(FlaskForm):
    matricula = IntegerField(
        "matricula"
    )
    nombre=StringField(
        "nombre",validators=[DataRequired(message="el campo es requerido")]
    )
    apellidos = StringField(
        "apellidos", validators=[DataRequired(message="el campo es requerido")]
    )
    especialidad = StringField(
        "especialidad", validators=[DataRequired(message="el campo es requerido")]
    )
    email = EmailField(
        "email", validators=[DataRequired(message="el campo es requerido")]
    )

