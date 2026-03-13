from flask import render_template, request, redirect, url_for
import forms
from models import db, Cursos, Maestros
from . import cursos

@cursos.route("/cursos", methods=["GET"])
def index():
	cursos = Cursos.query.all() # type: ignore
	return render_template("cursos/index.html", cursos=cursos)

@cursos.route("/cursos/crear", methods=["GET", "POST"])
def crear():
    create_form = forms.CursoForm(request.form)
    create_form.maestro_id.choices = [(maestro.matricula, f"{maestro.nombre} {maestro.apellidos}") for maestro in Maestros.query.all()] # type: ignore
    if request.method == "POST":
        curso = Cursos(
            nombre=create_form.nombre.data,  # type: ignore
            descripcion=create_form.descripcion.data,  # type: ignore
            maestro_id=create_form.maestro_id.data # type: ignore
        )
        db.session.add(curso)
        db.session.commit()
        return redirect(url_for('cursos.index'))
    return render_template("cursos/crear.html", form=create_form)

@cursos.route("/cursos/detalle")
def detalle():
    id = request.args.get("id")
    curso = db.session.query(Cursos).filter(Cursos.id==id).first()
    return render_template("cursos/detalles.html", curso=curso)

@cursos.route("/cursos/modificar", methods=["GET", "POST"])
def modificar():
    create_form = forms.CursoForm(request.form)
    create_form.maestro_id.choices = [(maestro.matricula, f"{maestro.nombre} {maestro.apellidos}") for maestro in Maestros.query.all()] # type: ignore
    id = request.args.get("id")
    curso = db.session.query(Cursos).filter(Cursos.id==id).first()
    if request.method == "GET":
        create_form.id.data = id # type: ignore
        create_form.nombre.data = curso.nombre # type: ignore
        create_form.descripcion.data = curso.descripcion # type: ignore
        create_form.maestro_id.data = curso.maestro_id # type: ignore
    if request.method == "POST":
        curso.nombre = create_form.nombre.data # type: ignore
        curso.descripcion = create_form.descripcion.data  # type: ignore
        curso.maestro_id = create_form.maestro_id.data # type: ignore
        db.session.add(curso)
        db.session.commit()
        return redirect(url_for('cursos.index'))
    return render_template("cursos/modificar.html", form=create_form)

@cursos.route("/cursos/eliminar", methods=["GET", "POST"])
def eliminar():
    create_form = forms.CursoForm(request.form)
    create_form.maestro_id.choices = [(maestro.matricula, f"{maestro.nombre} {maestro.apellidos}") for maestro in Maestros.query.all()] # type: ignore
    id = request.args.get("id")
    curso = db.session.query(Cursos).filter(Cursos.id==id).first()
    if request.method == "GET":
        create_form.id.data = id # type: ignore
        create_form.nombre.data = curso.nombre # type: ignore
        create_form.descripcion.data = curso.descripcion # type: ignore
        create_form.maestro_id.data = curso.maestro_id # type: ignore
    if request.method == "POST":
        db.session.delete(curso)
        db.session.commit()
        return redirect(url_for('cursos.index'))
    return render_template("cursos/eliminar.html", form=create_form)

@cursos.route("/cursos/alumnos-inscritos")
def alumnos_inscritos():
    cursos = Cursos.query.order_by(Cursos.nombre).all() # type: ignore
    selected_id = request.args.get("id", type=int)
    curso = None
    if cursos:
        if selected_id is None:
            primer_curso = cursos[0] # type: ignore
            selected_id = primer_curso.id # type: ignore
        curso = db.session.query(Cursos).filter(Cursos.id==selected_id).first() # type: ignore
    alumnos = curso.alumnos if curso else [] # type: ignore
    return render_template(
        "cursos/alumnos_inscritos.html",
        cursos=cursos,
        curso=curso,
        alumnos=alumnos,
        selected_id=selected_id
    )