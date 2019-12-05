cab = ['nome', 'telefone', 'email','idade']

pess = [['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
        ['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
        ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
        ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17']]

def lista_maior_18(pess, cab):
    lista = []
    for i in range(7):
        dicionario = {}
        for j in range(4):
            dicionario [ cab[j] ] =  pess[j][i]         
        lista.append(dicionario)

    lista_maiores = []
    for pessoa in lista:
        if int(pessoa['idade']) >= 18:
            lista_maiores.append(pessoa)
    return lista_maiores

lista1 = lista_maior_18(pess, cab)

for i in lista1:
    print(i)
