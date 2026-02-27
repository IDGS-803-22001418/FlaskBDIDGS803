from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect # type: ignore
from flask_migrate import Migrate # type: ignore
from config import DevelopmentConfig

import forms

from models import db, Alumnos

app = Flask(__name__)
app.config['SECRET_KEY'] = 'una-clave-secreta-muy-dificil-de-adivinar'
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e): # type: ignore
	return render_template("404.html")

@app.route("/", methods=["GET"])
@app.route("/index")
def index():
	alumnos = Alumnos.query.all() # type: ignore
	return render_template("index.html", alumnos=alumnos)

@app.route("/Alumnos", methods=["GET", "POST"])
def alumnos():
	create_form = forms.UserForm(request.form)
	if request.method == "POST":
		alumno = Alumnos(
			nombre=create_form.nombre.data,  # type: ignore
			apellidos=create_form.apellidos.data,  # type: ignore
			email=create_form.email.data,  # type: ignore
			telefono=create_form.telefono.data # type: ignore
		)
		db.session.add(alumno)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("Alumnos.html", form=create_form)

@app.route("/detalle")
def detalle():
	id = request.args.get("id")
	alumno = db.session.query(Alumnos).filter(Alumnos.id==id).first()
	return render_template("detalles.html", alumno=alumno)

@app.route("/modificar", methods=["GET", "POST"])
def modificar():
	create_form = forms.UserForm(request.form)
	id = request.args.get("id")
	alumno = db.session.query(Alumnos).filter(Alumnos.id==id).first()
	if request.method == "GET":
		create_form.id.data = id # type: ignore
		create_form.nombre.data = alumno.nombre # type: ignore
		create_form.apellidos.data = alumno.apellidos # type: ignore
		create_form.email.data = alumno.email # type: ignore
		create_form.telefono.data = alumno.telefono # type: ignore
	if request.method == "POST":
		alumno.nombre = create_form.nombre.data # type: ignore
		alumno.apellidos = create_form.apellidos.data # type: ignore
		alumno.email = create_form.email.data  # type: ignore
		alumno.telefono = create_form.telefono.data # type: ignore
		db.session.add(alumno)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("modificar.html", form=create_form)

@app.route("/eliminar", methods=["GET", "POST"])
def eliminar():
	create_form = forms.UserForm(request.form)
	id = request.args.get("id")
	alumno = db.session.query(Alumnos).filter(Alumnos.id==id).first()
	if request.method == "GET":
		create_form.id.data = id # type: ignore
		create_form.nombre.data = alumno.nombre # type: ignore
		create_form.apellidos.data = alumno.apellidos # type: ignore
		create_form.email.data = alumno.email # type: ignore
		create_form.telefono.data = alumno.telefono # type: ignore
	if request.method == "POST":
		db.session.delete(alumno)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("eliminar.html", form=create_form)



if __name__ == '__main__':
	csrf.init_app(app) # type: ignore
	
	with app.app_context():
		db.create_all()
	app.run(debug=True)
