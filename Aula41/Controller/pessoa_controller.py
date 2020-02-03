from flask_restful import Resource
from flask import request               #Request traz do HTML/Insomnia as informações

from Aula41.dao.pessoa_dao import PessoaDao
from Aula41.Model.pessoa_model import PessoaModel

class PessoaController(Resource):
    def __init__(self):
        self.dao = PessoaDao()

    def get(self, id=None):                             #Quando adiciona o None ele indica que é parametro opcional
        if id:
            return self.dao.get_by_id(id)               #Com o return ele sai do metodo e devolve o que está dentro dele
        return self.dao.list_all()

    def post(self):
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        idade = int(request.json['idade'])
        pessoa = PessoaModel(nome, sobrenome, idade)
        msg = self.dao.insert(pessoa)
        return msg


    def put(self, id):
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        idade = int(request.json['idade'])
        pessoa = PessoaModel(nome, sobrenome, idade, id)
        msg = self.dao.update(pessoa)
        return msg

    def delete(self, id):
        return self.dao.remove(id)