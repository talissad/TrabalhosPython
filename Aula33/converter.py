def converte_tabela_dicionario(lista_tuplas):
    lista_pessoas = []
    for p in lista_tuplas:
        dicionario_pessoa = {'id': 0; 'nome': '', 'sobrenome' : '', 'idade': 0, 'endereco_id': 0}
        dicionario_pessoa['id'] = p[0]
        dicionario_pessoa['nome'] = p[1]
        dicionario_pessoa['sobrenome'] = p[2]
        dicionario_pessoa['idade'] = p[3]
        dicionario_pessoa['endereco_id'] = p[4]
        lista_pessoas.append(dicionario_pessoa)
    return lista_pessoas