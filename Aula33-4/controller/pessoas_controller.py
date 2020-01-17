import sys
sys.path.append('/Users/900161/Documents/TrabalhosPython/Aula33-4')
from model.pessoa import Pessoa
from dao.pessoa_db import PessoaDb
from controller.endereco_controller import EnderecoController

class PessoaController:
    dao = PessoaDb()
    endereco_controller = EnderecoController()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self, id):
        return self.dao.buscar_por_id(id)

    def salvar(self, pessoa:Pessoa):
        pessoa.endereco.id = self.endereco_controller.salvar(pessoa.endereco)
        return self.dao.salvar(pessoa)

    def alterar(self, pessoa:Pessoa):
        self.dao.alterar(pessoa)

    def deletar(self, id):
        self.dao.deletar(id)