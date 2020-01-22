from flask import Flask, render_template, request, redirect
import sys
sys.path.append('/Users/900161/Documents/TrabalhosPython/Aula37/')

from Controller.squads_controller import SquadsController
from Controller.framework_frontend_controller import FrameworkFrontendController
from Controller.linguagem_backend_controller import LinguagemBackendController
from Controller.sqbds_controller import SgbdsController

from Model.squads import Squads
from Model.framework_frontend import FrameworkFrontend
from Model.linguagem_backend import LinguagemBackend
from Model.sgbds import Sgbds

app = Flask(__name__, template_folder="template")
squads_controller = SquadsController()
front_controller = FrameworkFrontendController()
back_controller = LinguagemBackendController()
sgbds_controller = SgbdsController()
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
    squads.linguagemBackend = LinguagemBackend()
    squads.frameworkFrontend = FrameworkFrontend()
    squads.sgbds = Sgbds()
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

    back = LinguagemBackend()
    back.id_backend = request.args['id_backend']
    back.linguagem = request.args['linguagem']
    back.fk_back = request.args['fk_back']

    front = FrameworkFrontend()
    front.id_front = request.args['id_front']
    front.nome = request.args['nome']
    front.fk_front = request.args['fk_front']

    sgbds = Sgbds()
    sgbds.id_sgbds = request.args['id_sgbds']
    sgbds.fk_sgbds = request.args['fk_sgbds']
    sgbds.nomebd = request.args['nomebd']

    squads.linguagemBackend = back
    squads.frameworkFrontend = front
    squads.sgbds = sgbds
     
    if squads.id == 0:
        squads_controller.salvar(squads)
    else:
        squads_controller.alterar(squads)
    return redirect('/listar')

app.run(debug=True)
