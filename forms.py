from wtforms import Form, StringField, IntegerField, EmailField, validators, SelectField

class UserForm(Form):
    id = IntegerField('id')
    nombre = StringField('nombre', [
        validators.DataRequired('El campo es requerido'),
        validators.length(min=4, max=10, message='Ingresa un nombre valido')
    ])
    apellidos = StringField('apellidos', [validators.DataRequired('El campo es requerido')])
    email = EmailField('correo', [
        validators.DataRequired('El campo es requerido'), 
        validators.Email('Ingresa un correo valido')
    ])
    telefono = StringField('telefono', [validators.DataRequired('El campo es requerido')])

class MaestroForm(Form):
    matricula = IntegerField('matricula')
    nombre = StringField('nombre', [
        validators.DataRequired('El campo es requerido')
    ])
    apellidos = StringField('apellidos', [
        validators.DataRequired('El campo es requerido')
    ])
    especialidad = StringField('especialidad', [
        validators.DataRequired('El campo es requerido')
    ])
    email = EmailField('correo', [
        validators.DataRequired('El campo es requerido'), 
        validators.Email('Ingresa un correo valido')
    ])

class CursoForm(Form):
    id = IntegerField('id')
    nombre = StringField('nombre', [
        validators.DataRequired('El campo es requerido')
    ])
    descripcion = StringField('descripcion', [
        validators.DataRequired('El campo es requerido')
    ])
    maestro_id = SelectField('maestro_id', coerce=int, validators=[validators.DataRequired('El campo es requerido')])

class InscripcionForm(Form):
    id = IntegerField('id')
    alumno_id = SelectField('alumno_id', coerce=int, validators=[validators.DataRequired('El campo es requerido')])
    curso_id = SelectField('curso_id', coerce=int, validators=[validators.DataRequired('El campo es requerido')])
