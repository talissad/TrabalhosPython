from flask_restful import Resource

class PessoaController(Resource):
    def get(self):
        return 'Você está acessando o método GET'

    def post(self):
        return 'Agora você está no metodo POST'

    def put(self):
        return 'Acessando o PUT'

    def delete(self):
        return 'Tem certeza? Você está no método DELETE'