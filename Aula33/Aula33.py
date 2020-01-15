import MySQLdb

#conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
conexao = MySQLdb.connect(host='127.0.0.1', database='aulabd', user='root', passwd='')
cursor = conexao.cursor()

lista_pessoa = []

comando_sql_select = "SELECT * FROM pessoa"
cursor.execute(comando_sql_select)

resultado = cursor.fetchall()

for p in resultado:
    dicionario_pessoa = {'nome': '', 'sobrenome' : '', 'idade': 0, 'endereco_id': 0}
    dicionario_pessoa['id'] = p[0]
    dicionario_pessoa['nome'] = p[1]
    dicionario_pessoa['sobrenome'] = p[2]
    dicionario_pessoa['idade'] = p[3]
    dicionario_pessoa['endereco_id'] = p[4]
    lista_pessoa.append(dicionario_pessoa)

with open('Aula33/pessoas.txt', 'a') as arquivo:
    for p in lista_pessoa:
        arquivo.write(f"{p['id']}; {p['nome']}; {p['sobrenome']}; {p['idade']}; {p['endereco_id']}\n")

# print(lista_pessoa)




# ------------------METODO MAYKON COMENTADO --------------------



# #======= Classes
# #----- Importar biblioteca do Mysql
# import MySQLdb
# #----- Configurar a conexão
# conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
# #----- Salva o cursor da conexão em uma variável
# cursor = conexao.cursor()

# #----- Criação do comando SQL e passado para o cursor
# comando_sql_select = "SELECT * FROM 01_MDG_PESSOA"
# cursor.execute(comando_sql_select)
# #---- Pega todos os resultados da execução do comando SQL e armazena em uma variável
# resultado = cursor.fetchall()

# #cria uma lista para armazenar os dicionarios
# lista_pessoas = []
# for p in resultado:
#     #----- Criação do dicionario que representa uma pessoa
#     dicionario_pessoa = {'Id': 0, 'Nome' : '', 'Sobrenome': '', 'Idade' : 0, 'Endereco_Id': 0}
#     #--- pega cada posição da tupla e atribui a uma chave do dicionário
#     dicionario_pessoa['Id'] = p[0]
#     dicionario_pessoa['Nome'] = p[1]
#     dicionario_pessoa['Sobrenome'] = p[2]
#     dicionario_pessoa['Idade'] = p[3]
#     dicionario_pessoa['Endereco_Id'] = p[4]
#     lista_pessoas.append(dicionario_pessoa)

# #----- Cria um arquivo e atribui a uma variável 'arquivo'
# with open('33-Aula33/pessoas.txt','a') as arquivo:
#     #---- Percorre a lista de dicionário e salva no arquivo em formato pré-definido
#     for p in lista_pessoas:
#         arquivo.write(f"{p['Id']};{p['Nome']};{p['Sobrenome']};{p['Idade']};{p['Endereco_Id']}\n")