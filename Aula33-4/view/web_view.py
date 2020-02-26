from flask import Flask, render_template
import sys
sys.path.append('C:/Users/900161/Documents/TrabalhosPython/Aula33-4')
from controller.pessoas_controller import PessoaController
from controller.endereco_controller import EnderecoController

app = Flask(__name__)
pc = PessoaController()
ec = EnderecoController()

@app.route('/')
def inicio():
    pessoas = pc.listar_todos()
    endereco = ec.listar_todos()
    return render_template('index.html', lista = pessoas, lista_endereco = endereco)

app.run()