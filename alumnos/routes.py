from . import alumnos
from flask import render_template, request, redirect, url_for
import forms
from models import db, Alumnos

@alumnos.route("/alumnos", methods=["GET"])
def index():
	alumnos = Alumnos.query.all() # type: ignore
	return render_template("alumnos/index.html", alumnos=alumnos)

@alumnos.route("/alumnos/crear", methods=["GET", "POST"])
def crear():
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
		return redirect(url_for('alumnos.index'))
	return render_template("alumnos/crear.html", form=create_form)

@alumnos.route("/alumnos/detalle")
def detalle():
	id = request.args.get("id")
	alumno = db.session.query(Alumnos).filter(Alumnos.id==id).first()
	return render_template("alumnos/detalles.html", alumno=alumno)

@alumnos.route("/alumnos/modificar", methods=["GET", "POST"])
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
		return redirect(url_for('alumnos.index'))
	return render_template("alumnos/modificar.html", form=create_form)

@alumnos.route("/alumnos/eliminar", methods=["GET", "POST"])
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
		return redirect(url_for('alumnos.index'))
	return render_template("alumnos/eliminar.html", form=create_form)

@alumnos.route("/alumnos/cursos-inscritos")
def cursos_inscritos():
	alumnos = Alumnos.query.order_by(Alumnos.nombre, Alumnos.apellidos).all() # type: ignore
	selected_id = request.args.get("id", type=int)
	alumno = None
	if alumnos:
		if selected_id is None:
			primer_alumno = alumnos[0] # type: ignore
			selected_id = primer_alumno.id # type: ignore
		alumno = db.session.query(Alumnos).filter(Alumnos.id==selected_id).first() # type: ignore
	cursos = alumno.cursos if alumno else [] # type: ignore
	return render_template(
		"alumnos/cursos_inscritos.html",
		alumnos=alumnos,
		alumno=alumno,
		cursos=cursos,
		selected_id=selected_id
	)