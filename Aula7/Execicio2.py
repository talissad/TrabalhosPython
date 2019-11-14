lista_jogadores = []


    dicionario_jogador = {}
    dicionario_jogador['Nome'] = input('Digite o nome: ')
    dicionario_jogador['Posicao'] = input('Digite a posicao: ')
    dicionario_jogador['Numero'] = input('Digite o número: ')
    dicionario_jogador['PernaBoa'] = input('Digite a perna boa: ')
    lista_jogadores.append(dicionario_jogador)

for j in lista_jogadores:
    print(f"Nome do Jogador: {j['Nome']} posição: {j['Posicao']} Numero: {j['Numero']} Perna boa: {j['PernaBoa']}")
    
    

'''
lista_jogadores = []
for i in range(1,3):
    nome=input('digite um nome:')
    posicao=input('digite a posição:')
    numero=input('digite o numero:')
    PernaBoa=input('digite a perna boa:')
    
dicionario = {'Nome':nome, 'Posicao':posicao, 'Numero':numero, 'Perna Boa':PernaBoa}

lista_jogadores.append(dicionario)

for dicionario in lista_jogadores:
    print(f"Nome={dicionario['nome']} - posição={dicionario['posicao']}") Numero: {dicionario['numero']} Perna boa: {dicionario['PernaBoa']
'''



'''Adiciona somente um jogador:

lista = ['Nome', 'Posicao', 'Numero', 'PernaBoa']
jogador = {}

for i in lista:
    jogador[i]=input(f'Digite {i}: ')
    
for i in lista:
    print(f'{i}: {jogador[i]}') '''