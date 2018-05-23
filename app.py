from flask import Flask, render_template, request, redirect

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

@app.route("/eventos/novo")
def novo_evento():
	return render_template("cadastro.html")


@app.route("/criar_evento", methods=['GET', 'POST'])
def cadastro():
	if request.method == "POST":
		nome = (request.form.get("nome"))
		sigla = (request.form.get("sigla"))
		
		if nome and sigla:
			p = Evento(nome=nome, sigla=sigla)
			db.session.add(p)
			db.session.commit()
			
	return redirect('/eventos')


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)