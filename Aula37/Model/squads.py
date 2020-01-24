import sys
sys.path.append('/Users/900161/Documents/TrabalhosPython/Aula37')

from Model.framework_frontend import FrameworkFrontend
from Model.linguagem_backend import LinguagemBackend
from Model.sgbds import Sgbds

class Squads:
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.descricao= ''
        self.numeroPessoas = 0
        self.linguagemBackend = None
        self.frameworkFrontend = None
        self.sgbds = None

    def __str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.numeroPessoas};{self.linguagemBackEnd};{self.frameworkFrontEnd};{self.sgbds}'

squads = Squads()
