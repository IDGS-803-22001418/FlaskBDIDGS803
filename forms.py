from wtforms import Form, StringField, IntegerField, EmailField, validators

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
