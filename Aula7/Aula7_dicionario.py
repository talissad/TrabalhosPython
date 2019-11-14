# Dicionarios
# dicionario = {CHAVE:VALOR, CHAVE:VALOR}

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