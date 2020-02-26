import sys
sys.path.append('/Users/900161/Documents/TrabalhosPython/Aula37/')
from Dao.framework_frontend_dao import FrontDao
from Model.framework_frontend import FrameworkFrontend

class FrameworkFrontendController:
    dao = FrontDao()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self, id):
        return self.dao.buscar_por_id(id)

    def salvar(self, frameworkFrontend:FrameworkFrontend):
        return self.dao.salvar(frameworkFrontend)

    def alterar(self, frameworkFrontend:FrameworkFrontend):
        self.dao.alterar(frameworkFrontend)

    def deletar(self, id):
        self.dao.deletar(id)
