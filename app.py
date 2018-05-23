from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

app = Flask('primeira_app', template_folder='templates')


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class Evento(db.Model):
	_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	nome = db.Column(db.String)
	sigla = db.Column(db.String)


db.create_all()


@app.route("/")
def index():
    return render_template('base.html')


@app.route("/eventos")
def lista_eventos():
    lista = Evento.query.all()
    return render_template('lista_eventos.html', eventos=lista)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)