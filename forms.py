from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, IntegerField
from wtforms.validators import DataRequired


class UsuarioForm(FlaskForm):
    id = IntegerField(
        "id", validators=[DataRequired(message="elcampo es requerido")]
    )
    nombre = StringField(
        "nombre", validators=[DataRequired(message="elcampo es requerido")]
    )
    apellido = StringField(
        "apellido", validators=[DataRequired(message="elcampo es requerido")]
    )
    correo = EmailField(
        "correo", validators=[DataRequired(message="elcampo es requerido")]
    )
