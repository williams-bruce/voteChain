from flask import render_template
from flask import request
from src import app
from src import db

@app.route('/', methods = ['POST','GET'])
def home():
    vars = {
        'eleitorFound': True
    }
    if request.method == 'POST':
        if 'confirma' in request.form and 'numero' in request.form:
            numero = request.form.get('numero')
            resultado = db.search('eleitores', codigo = numero)
            if resultado:
                vars['aluno'] = resultado[0][0]
                return render_template('urna-findstudent.html', **vars)
            else:
                print('entrei no else')
                vars['eleitorFound'] = False
                return render_template('urna-findstudent.html', **vars)
    return render_template('urna-initialpage.html', **vars)


@app.route('/votacao', methods=['POST','GET'])
def votacao():
    vars = {'candidatoFound': True}
    if request.method == 'POST':
        if 'confirma' in request.form:
            valor = request.form['confirma']
            print(valor)
            
        numeroCandidato = request.form.get('numeroCandidato')
        resultado = db.search('candidatos', codigo = numeroCandidato)
        if resultado:
            vars['nome'] = resultado[0][0]
            vars['numero'] = resultado[0][1]
            vars['partido'] = resultado[0][2]
            vars['foto'] = resultado[0][3]
            return render_template('urna-findcandidate.html', **vars)
        else:
            vars = {'candidatoFound': False}
            return render_template('urna-findcandidate.html', **vars)
    return render_template('urna-vote.html')