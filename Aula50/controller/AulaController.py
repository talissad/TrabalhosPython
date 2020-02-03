from flask_restful import Resource
from flask import request

from Aula50.model.AulaModel import Aula
from Aula50.dao.AulaDao import AulaDao

class AulaController(Resource):
    def __init__(self):
        self.dao = AulaDao()

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.list_all()

    def post(self):
        professor = request.json['professor']
        quantidade = int(request.json['quantidade'])
        sala = request.json['sala']
        disciplina = request.json['disciplina']
        sala = Aula(professor, quantidade, sala, disciplina)
        msg = self.dao.insert(sala)
        return msg

    def put(self, id):
        professor = request.json['professor']
        quantidade = int(request.json['quantidade'])
        sala = request.json['sala']
        disciplina = request.json['disciplina']
        sala = Aula(professor, quantidade, sala, disciplina, id)
        msg = self.dao.update(sala)
        return msg

    def delete(self, id):
        return self.dao.remove(id)