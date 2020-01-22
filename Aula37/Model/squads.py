from framework_frontend import FrameworkFrontend
from linguagem_backend import LinguagemBackend
from sgbds import Sgbds

class Squads:
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.descricao= ''
        self.numeroPessoas = 0
        # self.linguagemBackend = ''
        # self.frameworkFrontend = ''
        self.linguagemBackend = ()
        self.frameworkFrontend = ()
        self.Sgbds = ()

    def __str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.numeroPessoas};{self.linguagemBackEnd};{self.frameworkFrontEnd};{self.sgbds}'

squads = Squads()
