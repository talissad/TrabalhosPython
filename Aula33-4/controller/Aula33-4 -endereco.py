import sys
sys.path.append('/Users/900161/Documents/TrabalhosPython/Aula33-4/')

from model.endereco import Endereco
from dao.endereco_db import EnderecoDb

e = Endereco()
e_db = EnderecoDb()

def exportar():
    lpc = e_db.listar_todos()
    e.exportar_txt(lpc)