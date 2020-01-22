import sys
sys.path.append('/Users/900161/Documents/TrabalhosPython/Aula37/')
from Dao.squads_dao import SquadsDao
from Model.squads import Squads

class SquadsController:
    dao = SquadsDao()

    def listar_todos(self):
        lista_times = []
        lista_tuplas = self.dao.listar_todos()
        for p in lista_tuplas:
            squads = Squads()
            squads.id =  p[0]
            squads.nome = p[1]
            squads.descricao = p[2]
            squads.numeroPessoas = p[3]
            squads.linguagemBackEnd = p[4]
            squads.frameworkFrontEnd = p[5]
            lista_times.append(squads)
        return lista_times

    def buscar_por_id(self, id):
        p = self.dao.buscar_por_id(id)
        squads = Squads()
        squads.id =  p[0]
        squads.nome = p[1]
        squads.descricao = p[2]
        squads.numeroPessoas = p[3]
        squads.linguagemBackEnd = p[4]
        squads.frameworkFrontEnd = p[5]
        return squads

    def salvar(self, squads):
        return self.dao.salvar(squads)

    def alterar(self, squads):
        self.dao.alterar(squads)

    def deletar(self, id):
        self.dao.deletar(id)