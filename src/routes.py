from flask import render_template
from flask import request
from src import app
from src import db

@app.route('/', methods = ['POST','GET'])
def home():
    if request.method == 'POST':
        print(request.form)
        numero = request.form.get('numero')
        resultado = db.search('eleitores', codigo = numero)
        if resultado:
            return f'<h1>O numero do eleitor é {numero}</h1><br> e o nome é {resultado[0][0]}'
        return f'<h1>O numero do eleitor é {numero}</h1><br>Mas esse eleitor não estã no BD'
    return render_template('urna-copy.html')


@app.route('/vote', methods = ['POST', 'GET'])
def vote():
    if request.method == 'POST':
        voto = request.form.get('voto')
        resultado = db.search('candidatos', codigo = voto)
        if resultado:
            return # Mostrar foto, nome, partido, etc na mesma tela
        
    return render_template('vote.html')