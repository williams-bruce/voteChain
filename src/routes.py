from flask import render_template
from flask import request
from src import app
from src.forms import FormEleitor

@app.route('/', methods = ['POST','GET'])
def home():
    if request.method == 'POST':
        numero = request.form.get('numero')
        return f'<h1>O numero do eleitor é {numero}</h1>'
    return render_template('urna-copy.html')
