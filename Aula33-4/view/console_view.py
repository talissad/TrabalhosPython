import sys
sys.path.append('C:/Users/900161/Documents/TrabalhosPython/Aula33-4')
from controller.pessoa_controller import PessoaController
from controller.endereco_controller import EnderecoController

pc = PessoaController()
ec = EnderecoController()

for p in pc.listar_todos():
    print(p)

for e in ec.listar_todos():
    print(e)

    