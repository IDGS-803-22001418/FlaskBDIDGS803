from flask import Flask, render_template, request, redirect, url_for, flash, g
from flask_wtf.csrf import CSRFProtect # type: ignore
from config import DevelopmentConfig

import forms

from models import db, Alumnos

app = Flask(__name__)
app.config['SECRET_KEY'] = 'una-clave-secreta-muy-dificil-de-adivinar'
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e): # type: ignore
	return render_template("404.html")

@app.route("/", methods=["GET", "POST"])
@app.route("/index")
def index():
	alumnos = Alumnos.query.all() # type: ignore
	return render_template("index.html", alumnos=alumnos)

@app.route("/detalle")
def detalle():
	id = request.args.get("id")
	alumno = db.session.query(Alumnos).filter(Alumnos.id==id).first()
	return render_template("detalles.html", alumno=alumno)

@app.route("/Alumnos", methods=["GET", "POST"])
def alumnos():
	create_form = forms.UserForm(request.form)
	if request.method == "POST":
		alumno = Alumnos(
			nombre=create_form.nombre.data,  # type: ignore
			apaterno=create_form.apaterno.data,  # type: ignore
			email=create_form.email.data  # type: ignore
		)
		db.session.add(alumno)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("Alumnos.html", form=create_form)

if __name__ == '__main__':
	csrf.init_app(app) # type: ignore
	db.init_app(app)
	with app.app_context():
		db.create_all()
	app.run(debug=True)
