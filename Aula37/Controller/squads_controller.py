import sys
sys.path.append('/Users/900161/Documents/TrabalhosPython/Aula37/')

from Dao.squads_dao import SquadsDao

from Model.squads import Squads
from Model.framework_frontend import FrameworkFrontend
from Model.linguagem_backend import LinguagemBackend
from Model.sgbds import Sgbds

from Controller.framework_frontend_controller import FrameworkFrontendController
from Controller.linguagem_backend_controller import LinguagemBackendController
from Controller.sqbds_controller import SgbdsController

class SquadsController:
    dao = SquadsDao()
    frontend_controller = FrameworkFrontendController()
    backend_controller = LinguagemBackendController()
    sgbds_controller = SgbdsController()

    def listar_todos(self):
        lista_times = []
        lista_tuplas = self.dao.listar_todos()
        for p in lista_tuplas:
            squads = Squads()
            squads.id =  p[0]
            squads.nome = p[1]
            squads.descricao = p[2]
            squads.numeroPessoas = p[3]
            squads.linguagemBackend = p[4]
            squads.frameworkFrontend = p[5]
            
            squads.linguagemBackend = LinguagemBackend()
            squads.linguagemBackend.id =  p[0]
            squads.linguagemBackend.id =  p[0]
            squads.linguagemBackend.id =  p[0]
            
            squads.frameworkFrontend = FrameworkFrontend()
            squads.frameworkFrontend.id =  p[0]
            squads.frameworkFrontend.id =  p[0]
            squads.frameworkFrontend.id =  p[0]
            
            squads.sgbds = Sgbds()
            squads.sgbds.id =  p[0]
            squads.sgbds.id =  p[0]
            squads.sgbds.id =  p[0]

            
            lista_times.append(squads)
        return lista_times

    def buscar_por_id(self, id):
        p = self.dao.buscar_por_id(id)
        squads = Squads()
        squads.id =  p[0]
        squads.nome = p[1]
        squads.descricao = p[2]
        squads.numeroPessoas = p[3]
        squads.linguagemBackend = p[4]
        squads.frameworkFrontend = p[5]

        squads.linguagemBackend.id = p[6]
        squads.linguagemBackend.linguagem = p[7]
        squads.linguagemBackend.fk_back = p[8]

        squads.frameworkFrontend.id = p[9]
        squads.frameworkFrontend.nome = p[10]
        squads.frameworkFrontend.fk_front = p[11]

        squads.sgbds.id = p[12]
        squads.sgbds.fk_sgbds = p[13]
        squads.sgbds.nomebd = p[14]
       
        return squads

    def salvar(self, squads):
        squads.linguagemBackend.id = self.linguagem_backend_controller.salvar(squads.linguagemBackend)
        #### Verificar como salvar todos os 4 banco de dados juntos
        return self.dao.salvar(squads)

    def alterar(self, squads):
        self.linguagem_backend_controller.alterar(squads.linguagem_backend)
        #### Verificar como altera todos os 4 banco
        self.dao.alterar(squads)

    def deletar(self, id):
        self.dao.deletar(id)