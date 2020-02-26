from flask import Flask
from flask_restful import Api

from Aula50.controller.AulaController import AulaController

app = Flask(__name__)
api = Api(app)

api.add_resource(AulaController, '/api/aula', endpoint='aulas')
api.add_resource(AulaController, '/api/aula/<int:id>', endpoint='aula')

@app.route('/')
def inicio():
    return 'Bem vindo ao API sobre aula!'

app.run(debug=True, port=80)