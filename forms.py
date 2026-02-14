from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


class UsuarioForm(FlaskForm):
    nombre = StringField(
        "nombre", validators=[DataRequired(message="El nombre es requerido")]
    )
    apellido = StringField(
        "apellido", validators=[DataRequired(message="El apellido es requerido")]
    )
    correo = EmailField(
        "correo", validators=[DataRequired(message="El correo es requerido"), Email(message="Correo inválido")]
    )
    submit = SubmitField("Guardar")
