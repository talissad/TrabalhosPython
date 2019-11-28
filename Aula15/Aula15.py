# aula 15 
# Manipulaçao de arquivos


# arquivo = open('aula15.txt', 'w')
# arquivo.write('Voltolini Turismo\n')
# arquivo.close()

# arquivo = open('aula15.txt', 'r')
# arquivo = open('aula15.txt', 'a')
# arquivo.write(f" {input('Digite nome: ')}\n")
# arquivo.close()

# for linha in arquivo:
#     print(linha)
# arquivo.close()

# arquivo = open('atividadeAula15.txt', 'w')
# for nome in range(0,3):
#     nome = input('digite um nome: ')
#     arquivo.write(nome)
#     arquivo.write('\n')
# arquivo.close

def salvar_pessoa(pessoa_dicionario):
    arquivo = open('aula15.txt','a')
    arquivo.write(f"{pessoa_dicionario['nome']};{pessoa_dicionario['sobrenome']};{pessoa_dicionario['idade']}\n")
    arquivo.close()

def ler():
    lista = []
    arquivo = open('aula15.txt','r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        pessoa = {'nome':lista_linha[0], 'sobrenome':lista_linha[1], 'idade':lista_linha[2]}
        lista.append(pessoa)
    arquivo.close()
    return lista

# nome  = input('Digite nome : ')
# sobrenome = input('Digite o sobrenome : ')
# idade = int(input('Digite a idade : '))

# pessoa = {'nome':nome, 'sobrenome':sobrenome, 'idade':idade}
# salvar_pessoa(pessoa)

for p in ler():
    print(f"{p['nome']} - {p['sobrenome']} - {p['idade']}")