from flask import render_template
from flask import request
from src import app
from src import db

@app.route('/', methods = ['POST','GET'])
def home():
    vars = {
        'page': 'inicio',
        'eleitorFound': True
    }
    if request.method == 'POST':
        numero = request.form.get('numero')
        resultado = db.search('eleitores', codigo = numero)
        if resultado:
            return render_template('urna-findstudent.html', **vars)
        else:
            vars['eleitorFound'] = False
            return render_template('urna-findstudent.html', **vars)
    return render_template('urna-initialpage.html', **vars)


