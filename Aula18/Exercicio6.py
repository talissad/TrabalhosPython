def ler_cadastro():
    arquivo.open("Aula18/cadastro.txt", 'r')                                                        #abre o arquivo
    lista = []                                                                                      #abre a lista vazia
    for pessoa in arquivo:                                                                          #for quebra bastante vezes
        pessoas = pessoas.strip().split(';')                                                        #slipt ';' quebra o texto de acordo com a string colocada entre aspas
        dicionario = {'codigo':pessoas[0],'nome':pessoas[1],'sexo':pessoas[2], 'idade':pessoas[3]}  #coloca as informações dentro do dicionário
        lista.append(dicionario)                                                                    #adiciona
    arquivo.close()                                                                                 #fecha
    return lista                                                                                    #retorna a lista []
# print(ler_cadastro)

def lista_festa(lista_de_entradas):
    lista_homens = []
    lista_mulheres = [] 
    for pessoa in lista_de_entradas:
        if int(pessoa['idade']) >= 18:
            if pessoa[sexo] == 'f':
                lista_mulheres.append(pessoa)
            else:
                lista_homens.append(pessoa)
        salvar(lista_homens, 'homens')
        salvar(lista_mulheres, 'mulheres')

def salvar(lista, nome):
    arquivo = open(f'Aula18/exercicios/{nome}.txt','a')
    for pessoa in lista:
    #    texto = (f'{pessoas['codigo']}; {pessoas['nome']}; {pessoas['sexo']}; {pessoas['idade']}\n')
        arquivo.write(texto)
    arquivo.close()

def consultar(lista_consulta):
    for lista_consulta in lista_consulta_funcao:
        if int(lista_consulta['codigo']) == numero:
            if int(lista_consulta['idade']) >= 18:
                if lista_consulta['sexo'] == 'f':
                    print(f"Nome: {lista_consulta['nome']}: valor ingresso: R$ 15,00")
                else:
                    print(f"Nome: {lista_consulta['nome']}: valor ingresso: R$ 35,00")
            else:
                print('Não pode entrar!')

lista1 = ler_cadastro()
lista_festa(lista1)

while True:
    a = int(input('Digite um código: '))
    consulta(lista1, a)