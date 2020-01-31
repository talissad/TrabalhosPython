from flask import Flask
from flask_restful import Api
from Aula41.Controller.pessoa_controller import PessoaController

app = Flask(__name__)
api = Api(app)

api.add_resource(PessoaController, '/api/pessoa', endpoint='pessoas')
api.add_resource(PessoaController, '/api/pessoa/<int:id>', endpoint='pessoa')

@app.route('/')
def inicio():
    return 'Bem vindo a API! Ela irá ligar a Web ao Sistema'

app.run(debug=True, port=100)