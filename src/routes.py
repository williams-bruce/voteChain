from flask import render_template, session
from flask import request
from src import app
from src import db
from src.models.Block import Block


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
                session['eleitor'] = resultado[0][1]
                return render_template('urna-findstudent.html', **vars)
            else:
                vars['eleitorFound'] = False
                return render_template('urna-findstudent.html', **vars)
    return render_template('urna-initialpage.html', **vars)


@app.route('/votacao', methods=['POST','GET'])
def votacao():
    vars = {'candidatoFound': True}
    if request.method == 'POST':
        if 'branco' in request.form:
            return render_template('urna-null.html')
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


@app.route('/confirmarVoto', methods=['POST','GET'])
def confirma():
    if request.method =='POST' and 'confirma' in request.form:
        eleitor = session['eleitor']
        if request.form['confirma'] == 'branco':
            Block('branco', eleitor)
            return render_template('urna-end.html')
        
        candidato = request.form.get('confirma')
        print(candidato, '->',type(candidato))
        print(eleitor, '->',type(eleitor))
        Block(str(candidato), str(eleitor))
        return render_template('urna-end.html')
        