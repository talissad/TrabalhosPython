def lista_cervejas(cerveja):
    arquivo = open('atividadeAula15.txt','a')
    arquivo.write(f"{cerveja['marca']};{cerveja['tipo']};{cerveja['teor']}\n")
    arquivo.close()

def lerCerveja():
    lista = []
    arquivo = open('atividadeAula15.txt','r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        cerveja = {'marca':lista_linha[0], 'tipo':lista_linha[1], 'teor':lista_linha[2]}
        lista.append(cerveja)
    arquivo.close()
    return lista

marca  = input('Digite o nome da Cerveja: ')
tipo = input('Digite o tipo: ')
teor = input('Digite o teor: ')

cerveja = {'marca':marca, 'teor':teor, 'tipo':tipo}
lista_cervejas(cerveja)

for p in lerCerveja():
    print(f"{p['marca']} - {p['tipo']} - {p['teor']}")
