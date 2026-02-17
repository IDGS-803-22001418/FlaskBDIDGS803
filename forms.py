from wtforms import Form, StringField, IntegerField, EmailField, validators

class UserForm(Form):
    id = IntegerField('id')
    nombre = StringField('nombre', [
        validators.DataRequired('El campo es requerido'),
        validators.length(min=4, max=10, message='Ingresa un nombre valido')
    ])
    apaterno = StringField('apaterno', [validators.DataRequired('El campo es requerido')])
    email = EmailField('correo', [
        validators.DataRequired('El campo es requerido'), 
        validators.Email('Ingresa un correo valido')
    ])
