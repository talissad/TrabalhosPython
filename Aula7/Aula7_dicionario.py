# Dicionarios
# dicionario = {CHAVE:VALOR, CHAVE:VALOR}
'''
lista = []
dicionario = {'Nome':'Talissa', 'Sobrenome':'Dahlke'}
print(dicionario)
print(dicionario['Sobrenome'])

nome = 'Mirella'
lista_notas = [10,20,50,70]
media = sum(lista_notas) / len(lista_notas)

situacao = 'Reprovado'
if media >= 7:
    situacao = 'Aprovado'

dicionario_alunos = {'Nome':nome, 'Lista_Notas': lista_notas, 'Media':media , 'Situacao':situacao}

print(f"{dicionario_alunos['Nome']} - {dicionario_alunos['Situacao']}")


dicionario_bandas = {'Nome': ''}
dicionario_bandas['Nome'] = 'Calipso'
dicionario_bandas['Nome'] = 'Dejavu'

print (dicionario_bandas)

dicionario = {'Nome':'Talissa', 'Sobrenome':'Dahlke'}
dicionario['Sobrenome'] = 'Rauen'
dicionario['CPF'] = '080.989.484-70'

print(dicionario) '''


dicionario_pessoa = {'Nome':'', 'Sobrenome':'', 'CPF': '', 'RG':''}
lista_pessoas = []

for i in range(1,4):
    dicionario_pessoa['Nome'] = input('Digite o nome: ')
    dicionario_pessoa['Sobrenome'] = input('Digite o sobrenome: ')
    dicionario_pessoa['CPF'] = input('Digite o CPF: ')
    dicionario_pessoa['RG'] = input('Digite o RG: ')
    lista_pessoas.append(dicionario_pessoa)

print (lista_pessoas)