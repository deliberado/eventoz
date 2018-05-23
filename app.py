from flask import Flask, render_template

app = Flask('primeira_app', template_folder='templates')

@app.route("/")
def index():
    return render_template('base.html')


app.run(debug=True, use_reloader=True)

