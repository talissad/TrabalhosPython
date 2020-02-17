def ler_arquivo(pessoa):
    arquivo = open('pessoas.txt', 'r')
    arquivo.write(f"{pessoa['nome']};{pessoa['sobrenome']}\n")
    arquivo.close()

def ler_lista():
    lista = []
    arquivo = open('pessoas.txt.txt', 'r')
    for pessoa in arquivo:
        pessoa = pessoa.strip()
        lista_linha = pessoa.split(';')
        pessoa = {'nome': lista_linha[0], 'sobrenome': lista_linha[1]}
        lista.append(pessoa)
    arquivo.close()
    return lista


resposta = 'sim'
while resposta != 'N':
    resposta = input('Gostaria de adicionar pessoas em sua rede de contatos? (N/S)')
    resposta.upper()

