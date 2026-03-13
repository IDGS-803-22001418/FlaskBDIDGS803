from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect # type: ignore
from flask_migrate import Migrate # type: ignore
from config import DevelopmentConfig
from maestros.routes import maestros
from alumnos.routes import alumnos
from cursos.routes import cursos
from inscripciones.routes import inscripciones
from models import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'una-clave-secreta-muy-dificil-de-adivinar'
app.config.from_object(DevelopmentConfig)

app.register_blueprint(maestros) # Registrar el blueprint de maestros
app.register_blueprint(alumnos)
app.register_blueprint(cursos)
app.register_blueprint(inscripciones)

db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect()


@app.errorhandler(404)
def page_not_found(e): # type: ignore
	return render_template("404.html")

@app.route("/", methods=["GET"])
@app.route("/index")
def index():
	return render_template("index.html")


if __name__ == '__main__':
	csrf.init_app(app) # type: ignore
	
	with app.app_context():
		db.create_all()
	app.run(debug=True)
