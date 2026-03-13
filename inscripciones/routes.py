from flask import render_template, request, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError
import forms
from models import db, Cursos, Alumnos, Inscripciones
from . import inscripciones

@inscripciones.route('/inscripciones', methods=['GET', 'POST'])
def crear():
    create_form = forms.InscripcionForm(request.form)
    create_form.curso_id.choices = [(curso.id, curso.nombre) for curso in Cursos.query.all()] # type: ignore
    create_form.alumno_id.choices = [(alumno.id, f"{alumno.nombre} {alumno.apellidos}") for alumno in Alumnos.query.all()] # type: ignore
    if request.method == 'POST':
        inscripcion = Inscripciones(
            curso_id=create_form.curso_id.data,  # type: ignore
            alumno_id=create_form.alumno_id.data  # type: ignore
        )
        try:
            db.session.add(inscripcion)
            db.session.commit()
            flash('Inscripcion registrada correctamente.', 'success')
            return redirect(url_for('inscripciones.crear'))
        except IntegrityError as error:
            db.session.rollback()
            if 'unique_inscripcion' in str(error.orig).lower() or 'duplicate' in str(error.orig).lower():
                flash('El alumno ya esta inscrito en este curso.', 'error')
            else:
                flash(f'Error de base de datos: {error.orig}', 'error')
            return redirect(url_for('inscripciones.crear'))
    return render_template('inscripciones/crear.html', form=create_form)