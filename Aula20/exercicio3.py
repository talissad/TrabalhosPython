def ler_cadastro():
    arquivo = open('Aula20/cadastro.txt', 'r')
    cadastro = []
    for pessoas in arquivo:
        pessoas = pessoas.strip().split(';')
        dicionario_pessoas = {'codigo':pessoas[0], 'nome':pessoas[1], 'idade':pessoas[2], 'sexo':pessoas[3], 'email':pessoas[4], 'telefone':pessoas[5]}
        cadastro.append(dicionario_pessoas)
    arquivo.close()
    return cadastro

def lista(lista_email):
   lista_homens = []
   lista_mulheres = []

   for pessoa in lista_email:
    if int(pessoa['idade']) >= 20:
        if pessoa['sexo'] == 'f':
            lista_mulheres.append(pessoa)
        else:
            lista_homens.append(pessoa)    

   salvar(lista_homens,'homens')
   salvar(lista_mulheres,"mulheres")

def salvar(lista,nome):
   arquivo = open(f'Aula19/{nome}.txt','a')
   for pessoa in lista:
      texto = f"{pessoa['codigo']};{pessoa['nome']};{pessoa['idade']};{pessoa['sexo']};{pessoa['email']};{pessoa['telefone']}\n"
      arquivo.write(texto)
   arquivo.close()

def consulta(lista_consulta_funcao,numero):
   for lista_consulta in lista_consulta_funcao:
        if int(lista_consulta['codigo']) == numero:
            print(f"{lista_consulta['codigo']}\n{lista_consulta['nome']}\n{lista_consulta['idade']}\n{lista_consulta['sexo']}\n{lista_consulta['email']}\n{lista_consulta['telefone']}")
        elif numero == 's':
            numero = False
        else:
            print('código não encontrado!')

ler_cadastro()
lista_email(lista1)

while True:
   a=int(input('Digite um numero: '))
   consulta(lista1,a)
