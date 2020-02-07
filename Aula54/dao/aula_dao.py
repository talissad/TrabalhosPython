from Aula54.model.aula_model import AulaModel
from Aula54.dao.base_dao import BaseDao


class AulaDao(BaseDao):
    def list_all(self):
        return self.sessao.query(AulaModel).all()

    def buscar_por_id(self, id):
        return self.sessao.query(AulaModel).filter_by(id=id).one()

    def deletar(self, id):
        model = self.sessao.query(AulaModel).filter_by(id=id).one()
        self.sessao.delete(model)
        self.sessao.commit()
        return 'Deletado obj de id: {}'.format(id)

# metodo Abioluz
    def cadastrar(self, sala):
        self.sessao.add(sala)
        self.sessao.commit()

    def alterar(self, model:AulaModel) -> str:
        self.sessao.merge(model)
        self.sessao.commit

# banco não relacional
# mongo
# docker
# teste unitário
# Mensageria
# Rabbit