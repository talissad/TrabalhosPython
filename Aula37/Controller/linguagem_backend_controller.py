import sys
sys.path.append('/Users/900161/Documents/TrabalhosPython/Aula37/')
from Dao.linguagem_backend_dao import BackDao
from Model.linguagem_backend import LinguagemBackend

class LinguagemBackendController:
    dao = BackDao()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self, id):
        return self.dao.buscar_por_id(id)

    def salvar(self, linguagemBackend:LinguagemBackend):
        return self.dao.salvar(linguagemBackend)

    def alterar(self, linguagemBackend:LinguagemBackend):
        self.dao.alterar(linguagemBackend)

    def deletar(self, id):
        self.dao.deletar(id)
