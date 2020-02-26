from flask_restful import Resource
from flask import request               #Request traz do HTML/Insomnia as informações

from Aula41.dao.endereco_dao import EnderecoDao
from Aula41.Model.endereco_model import EnderecoModel

class EnderecoController(Resource):
    def __init__(self):
        self.dao = EnderecoDao()

    def get(self, id=None):                             #Quando adiciona o None ele indica que é parametro opcional
        if id:
            return self.dao.get_by_id(id)               #Com o return ele sai do metodo e devolve o que está dentro dele
        return self.dao.list_all()

    def post(self):
        logradouro = request.json['logradouro']
        numero = request.json['numero']
        complemento = request.json['complemento']
        bairro = request.json['bairro']
        cidade = request.json['cidade']
        cep = request.json['cep']
        endereco = EnderecoModel(logradouro, numero, complemento, bairro, cidade, cep)
        msg = self.dao.insert(endereco)
        return msg

    def put(self, id):
        logradouro = request.json['logradouro']
        numero = request.json['numero']
        complemento = request.json['complemento']
        bairro = request.json['bairro']
        cidade = request.json['cidade']
        cep = request.json['cep']
        endereco = EnderecoModel(logradouro, numero, complemento, bairro, cidade, cep, id)
        msg = self.dao.update(endereco)
        return msg

    def delete(self, id):
        return self.dao.remove(id)