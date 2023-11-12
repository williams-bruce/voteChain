from flask import render_template
from flask import request
from src import app
from src import db

@app.route('/', methods = ['POST','GET'])
def home():
    vars = {
        'page': 'inicio'
    }
    if request.method == 'POST':
        
        numero = request.form.get('numero')
        resultado = db.search('eleitores', codigo = numero)
        if resultado:
            vars['page'] = 'votacao'
            return render_template('urna-copy-copy.html', **vars)
        else:
            vars['page'] = 'eleitorNotFound'
            return render_template('urna-copy-copy.html', **vars)
    return render_template('urna-copy-copy.html', **vars)


@app.route('/vote', methods = ['POST', 'GET'])
def vote():
    if request.method == 'POST':
        voto = request.form.get('voto')
        resultado = db.search('candidatos', codigo = voto)
        if resultado:
            return # Mostrar foto, nome, partido, etc na mesma tela
        
    return render_template('vote.html')


@app.route('/confirmVote', methods = ['POST', 'GET'])
def confirm_vote():
    return render_template('confirm_vote.html')
