from Aula54.dao.aula_dao import AulaDao

dao = AulaDao()
aula = dao.list_all()

print(aula)
for info in aula:
    print(info)
