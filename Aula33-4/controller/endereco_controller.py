import sys
sys.path.append('/Users/900161/Documents/TrabalhosPython/Aula33-4')
from model.endereco import Endereco
from dao.endereco_db import EnderecoDb

class EnderecoController:
    e = Endereco()
    e_db = EnderecoDb()

    def listar_todos(self):
        return self.e_db.listar_todos()

    def exportar(self):
        lpc = self.e_db.listar_todos()
        self.e.exportar_txt(lpc)

    def buscar_por_id(self, id):
        return self.e_db.buscar_por_id(id)

    def salvar(self, endereco:Endereco):
        return self.e_db.salvar(endereco)

    def alterar(self, endereco:Endereco):
        self.e_db.alterar(endereco)

    def deletar(self, id):
        self.e_db.deletar(id)