from Aula54.dao.aula_dao import AulaDao
from Aula54.model.aula_model import AulaModel


dao = AulaDao()

# Imprime toda as informações contidas no banco de dados
aula = dao.list_all()
for info in aula:
    print(info)

# Imprimi somente uma variavel


# Cadastra salas de aula
sala = AulaModel(professor='Pedro 2', quantidade=30, sala='green', disciplina='Python')
dao.cadastrar(sala)
print(sala)

# Altera as informações
input('Aperte enter')
sala.professor = 'Paulo'
dao.cadastrar(sala)

print(sala)