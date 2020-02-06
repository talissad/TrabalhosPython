from Aula54.model.aula_model import AulaModel
from Aula54.dao.base_dao import BaseDao


class AulaDao(BaseDao):
    def list_all(self):
        return self.sessao.query(AulaModel).all()
