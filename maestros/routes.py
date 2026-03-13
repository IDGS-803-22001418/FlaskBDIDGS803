from . import maestros
from flask import render_template, request, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError
from models import db, Maestros
import forms

@maestros.route('/perfil/<nombre>')
def perfil(nombre: str):
    return f"Perfil de {nombre}"

@maestros.route("/maestros")
def index():
	maestros = Maestros.query.all() # type: ignore
	return render_template("maestros/index.html", maestros=maestros)

@maestros.route("/maestros/detalle")
def detalle():
	matricula = request.args.get("matricula")
	maestro = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
	return render_template("maestros/detalle.html", maestro=maestro)

@maestros.route("/maestros/crear", methods=["GET", "POST"])
def crear():
	create_form = forms.MaestroForm(request.form)
	if request.method == "POST":
		maestro = Maestros(
			matricula=create_form.matricula.data, # type: ignore
			nombre=create_form.nombre.data,  # type: ignore
			apellidos=create_form.apellidos.data,  # type: ignore
			especialidad=create_form.especialidad.data, # type: ignore
			email=create_form.email.data,  # type: ignore
		)
		try:
			db.session.add(maestro)
			db.session.commit()
			flash('Maestro registrado correctamente.', 'success')
		except IntegrityError as error:
			db.session.rollback()
			if 'duplicate' in str(error.orig).lower() or 'unique' in str(error.orig).lower():
				flash('La matricula ya esta registrada para otro maestro.', 'error')
			else:
				flash(f'Error de base de datos: {error.orig}', 'error')
		return redirect(url_for('maestros.index'))
	return render_template("maestros/crear.html", form=create_form)

@maestros.route("/maestros/modificar", methods=["GET", "POST"])
def modificar():
	create_form = forms.MaestroForm(request.form)
	matricula = request.args.get("matricula")
	maestro = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
	if request.method == "GET":
		create_form.matricula.data = maestro.matricula # type: ignore
		create_form.nombre.data = maestro.nombre # type: ignore
		create_form.apellidos.data = maestro.apellidos # type: ignore
		create_form.especialidad.data = maestro.especialidad # type: ignore
		create_form.email.data = maestro.email # type: ignore
	if request.method == "POST":
		maestro.matricula = create_form.matricula.data # type: ignore
		maestro.nombre = create_form.nombre.data # type: ignore
		maestro.apellidos = create_form.apellidos.data # type: ignore
		maestro.especialidad = create_form.especialidad.data # type: ignore
		maestro.email = create_form.email.data  # type: ignore
		try:
			db.session.add(maestro)
			db.session.commit()
			flash('Maestro actualizado correctamente.', 'success')
		except IntegrityError as error:
			db.session.rollback()
			if 'duplicate' in str(error.orig).lower() or 'unique' in str(error.orig).lower():
				flash('La matricula ya esta registrada para otro maestro.', 'error')
			else:
				flash(f'Error de base de datos: {error.orig}', 'error')
		return redirect(url_for('maestros.index'))
	return render_template("maestros/modificar.html", form=create_form)

@maestros.route("/maestros/eliminar", methods=["GET", "POST"])
def eliminar():
	create_form = forms.MaestroForm(request.form)
	matricula = request.args.get("matricula")
	maestro = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
	if request.method == "GET":
		create_form.matricula.data = maestro.matricula # type: ignore
		create_form.nombre.data = maestro.nombre # type: ignore
		create_form.apellidos.data = maestro.apellidos # type: ignore
		create_form.especialidad.data = maestro.especialidad # type: ignore
		create_form.email.data = maestro.email # type: ignore
	if request.method == "POST":
		db.session.delete(maestro)
		db.session.commit()
		return redirect(url_for('maestros.index'))
	return render_template("maestros/eliminar.html", form=create_form)
