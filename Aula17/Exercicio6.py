def cadastro_clientes(numero_funcao):
    dados_cliente = ['codigo_clinte', 'cpf', 'nome_completo', 'nascimento', 'estado', 'cidade', 'cep', 'bairro', 'rua', 'numero_casa', 'complemento']

    lista = []
    for j in range(numero_funcao):
        dicionario = {}
        for i in dados_cliente:
            dicionario[i]=input(f'Digite {i}: ')
        lista.append(dicionario)
    return lista

numero = int(input('Digite o número de cadastros: '))

lista_cadastro = cadastro_clientes(numero)


arquivo = open("Aula17/clientes.txt", 'a')
for cliente in lista_cadastro:
    cliente_chaves = list(cliente.keys())
    for chaves in cliente_chaves:
        salva = (f'{cliente[chaves]}')
        print(salva)