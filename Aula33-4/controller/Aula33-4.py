import sys
sys.path.append('/Users/900161/Documents/TrabalhosPython/Aula33-4/')

from model.pessoa import Pessoa
from dao.pessoa_db import PessoaDb

p = Pessoa()
p_db = PessoaDb()

def exportar():
    lpc = p_db.listar_todos()
    p.exportar_txt(lpc)