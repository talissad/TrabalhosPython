def exportar_txt(lista_pessoa):
    with open('Aula33/pessoas.txt', 'a') as arquivo:
        for p in lista_pessoa:
            arquivo.write(f"{p['id']}; {p['nome']}; {p['sobrenome']}; {p['idade']}; {p['endereco_id']}\n")


lpt = listar_todos()
lpd = converte_tabela_dicionario(lpt)
exportar_txt(lpd)
