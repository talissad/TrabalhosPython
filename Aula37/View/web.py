from flask import Flask, render_template, request, redirect
import sys
sys.path.append('/Users/900161/Documents/TrabalhosPython/Aula37/')

from Controller.squads_controller import SquadsController
from Model.squads import Squads

app = Flask(__name__)
squads_controller = SquadsController()
nome = 'Cadastros'

@app.route('/')
def inicio():
    return render_template('index.html', titulo_app = nome )

@app.route('/listar')
def listar():
    times = squads_controller.listar_todos()
    return render_template('listar.html', titulo_app = nome, lista = times)

@app.route('/cadastrar')
def cadastrar():
    squads = Squads()
    if 'id' in request.args:
        id = request.args['id']
        squads = squads_controller.buscar_por_id(id)
    return render_template('cadastrar.html', titulo_app = nome, squads = squads )


@app.route('/excluir')
def excluir():
    id = int(request.args['id'])
    squads_controller.deletar(id)
    return redirect('/listar')

@app.route('/salvar')
def salvar():
    squads = Squads()
    squads.id = request.args['id']
    squads.nome = request.args['nome']
    squads.descricao = request.args['descricao']
    squads.numeroPessoas = request.args['numeroPessoas']
    squads.linguagemBackEnd = request.args['linguagemBackEnd']
    squads.frameworkFrontEnd = request.args['frameworkFrontEnd']

    if squads.id == 0:
        squads_controller.salvar(squads)
    else:
        squads_controller.alterar(squads)
    return redirect('/listar')

app.run(debug=True)