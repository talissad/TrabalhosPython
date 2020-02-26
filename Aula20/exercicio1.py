lista = [['codigo','produto','valor','quantidade'],
         [1,'Cevada',15.00,10],
         [2,'Lupulo',150.50,200],
         [3,'Malte',57.80,5000],
         [4,'Levedura 1',10.65,500],
         [5,'Extrato de Levedura',15.00,60],
         [6,'Levedura 2',15.50,87]]

# 2.1 - Faça uma função que pegue esta lista e retorne uma lista com biblioteca.

# 2.2 - Faça outra função para consultar o preço através do código passado
# por parametro. Esta função deve printar o nome do produto, a quantidade
# e o preço.
# Execute esta função dentro do while e quando digitar qualquer código que 
# não tenha produto cadastrado o programa se encerra.

for i in lista:
    lista_produtos = []
    for j in i:
        dicionario_produtos = {'codigo':lista[0], 'produto':lista[1], 'valor':lista[2], 'quantidade':lista[3]}
        lista_produtos.append(dicionario_produtos)


def consultar_produto():
    iniciar = True
    while iniciar:
        cod_consultar = int(input('Digite o código do produto: '))
        if cod_consultar == lista[1][0]:
            print(f' Produto: {lista[1][1]} \nValor: {lista[1][2]}\nQuantidade: {lista[1][3]}')
        elif cod_consultar == lista[2][0]:
            print(f' Produto: {lista[2][1]} \nValor: {lista[2][2]}\nQuantidade: {lista[2][3]}')
        elif cod_consultar == lista[3][0]:
            print(f' Produto: {lista[3][1]} \nValor: {lista[3][2]}\nQuantidade: {lista[3][3]}')
        elif cod_consultar == lista[4][0]:
            print(f' Produto: {lista[4][1]} \nValor: {lista[4][2]}\nQuantidade: {lista[4][3]}')
        elif cod_consultar == lista[5][0]:
            print(f' Produto: {lista[5][1]} \nValor: {lista[5][2]}\nQuantidade: {lista[5][3]}')
        elif cod_consultar == lista[6][0]:
            print(f' Produto: {lista[6][1]} \nValor: {lista[6][2]}\nQuantidade: {lista[6][3]}')
        else:
            print('Não existe o produto')
            break

consultar_produto()