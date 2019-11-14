#Exercicio 1 - Dicionario
# escreva programa que leia os dados de cerveja
#cerveja: Marca, Tipo, IBU, ABV, EBC, Volume

lista = ['Marca', 'Tipo', 'IBU', 'ABV', 'EBC', 'Volume']
cerveja = {}

for i in lista:
    cerveja[i]=input(f'Digite {i}: ')
    
for i in lista:
    print(f'{i}: {cerveja[i]}')

'''Modo 2

cerveja = {}
cerveja ['Marca'] = (input('Digite a marca:'))
cerveja ['Tipo'] = (input('Digite o tipo:'))
cerveja ['IBU'] = (input('Digite o IBU:'))
cerveja ['ABV'] = (input('Digite o ABV:'))
cerveja ['ECB'] = (input('Digite o ECB:'))
cerveja ['Volume'] = (input('Digite o Volume:'))

print(f"Marca: {cerveja['Marca']} - Tipo: {cerveja['Tipo']} - IBU: {cerveja['IBU']} - ABV: {cerveja['ABV']} - ECB: {cerveja['ECB']} - Volume: {cerveja['Volume']}")'''