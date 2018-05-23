from flask import Flask, render_template

app = Flask('primeira_app', template_folder='templates')

@app.route("/")
def index():
    return render_template('base.html')


@app.route("/eventos")
def lista_eventos():
    lista = ['ENCOINFO', 'CAOS', 'Jornanda de Iniciação Cientifica']
    return render_template('lista_eventos.html', eventos=lista)

app.run(debug=True, use_reloader=True)

