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
