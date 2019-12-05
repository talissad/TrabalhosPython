# 1 - Crie um metodo que gere e retorne uma lista com bibliotecas com os dados dos clientes
def ler_cadastro():
    arquivo = open("Aula19/cadastro.txt", "r")
    cadastro = []
    for pessoas in arquivo:
        pessoas = pessoas.strip().split(';')
        dicionario_pessoas = {'codigo':pessoas[0], 'nome':pessoas[1], 'idade':pessoas[2], 'sexo':pessoas[3], 'email':pessoas[4], 'telefone':pessoas[5]}
        cadastro.append(dicionario_pessoas)
    arquivo.close()
    return cadastro


# 2 - Com a lista do exercicio 1, separe os adultos dos menores de idade e salve em um arquivo .txt cada.
# Esta função tambem retornar uma lista com a biblioteca dos maiores de idades.
def lista_festa(lista_convidados):
    maiores_idade = []
    menores_idade = []

    for convidado in lista_convidados:
        if int(convidado['idade']) >= 18:
            maiores_idade.append(convidado)
            arquivo = open('Aula19/exercicios/maiores.txt','a')
        else:
            menores_idade.append(convidado)
            arquivo = open('Aula19/exercicios/menores.txt','a')


# 3 - Crie uma função que conte quantas mulheres e quantos homens tem na lista. Salve cada um em um arquivo diferente.
def contador_maiores(arquivo_maiores):
    arquivo_maiores = open('Aula19/exercicios/maiores.txt','r')
    contador_maiores = 0
    for quantidade in arquivo_maiores:
        contador_maiores =+ 1
    print(quantidade)

def contador_menores(arquivo_menores):
    arquivo_menores = open('Aula19/exercicios/menores.txt','r')
    contador_menores = 0
    for quantidade in arquivo_menores:
        contador_menores =+ 1
    print(quantidade)


# 4 - Faça uma função de consulta de cadastro. A função deve receber o valor do código do cliente e deve imprimir na 
# tela os dados do cliente com f-string usando a lista do exercicio 1
def consulta(lista_consulta_funcao, numero):
    for lista_consulta in lista_consulta_funcao:
      if int(lista_consulta['codigo']) == numero:

        if int(lista_consulta['idade']) <= 16:
            if lista_consulta['sexo'] == 'f':
               print(f"Olá: {lista_consulta['nome']} Você quer aproveitar nosso Tikito sabor Gloss? É uma delicia!")

        if int(lista_consulta['idade']) < 16 and (lista_consulta['idade']) <18:
            if lista_consulta['sexo'] == 'f':
                print(f"Olá: {lista_consulta['nome']}! Quer experimentar nosso refigerante sabor alegria! O seu cruch vai adorar!")
        
        if int(lista_consulta['idade']) >= 18:
            if lista_consulta['sexo'] == 'f':
                print(f"Olá: {lista_consulta['nome']}! Já experimentou nossa bebida a base de tequila? Baixo tero alcoolico com o dobro de sabor!!!")

        if int(lista_consulta['idade']) <= 16:
            if lista_consulta['sexo'] == 'm':
               print(f"Olá: {lista_consulta['nome']}! Você quer aproveitar nosso Tikito sabor Meleka? É uma delicia!")

        if int(lista_consulta['idade']) < 16 and (lista_consulta['idade']) <18:
            if lista_consulta['sexo'] == 'm':
                print(f"Olá: {lista_consulta['nome']}! Quer experimentar nosso refigerante sabor Corriga de carros! A sua amada vai adorar!")
        
        if int(lista_consulta['idade']) >= 18:
            if lista_consulta['sexo'] == 'm':
                print(f"Olá: {lista_consulta['nome']}! Já experimentou nossa cerveja? alto teor alcoolico com o dobro do amargor!!!")
        else:
            print('INVALIDO')

lista1 = ler_cadastro()
# lista_festa(lista1)

while True:
   a=int(input('Digite um numero: '))
   consulta(lista1,a)