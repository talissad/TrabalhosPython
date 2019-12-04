cerveja = (('marca', 'tipo', 'ibu','preço'),
           ('Skol','IPA','ultra-leve',3.50),
           ('Brahma','lager','leve/media',3.45),
           ('Kaiser','Americam Larger','leve',2.35),
           ('Sol','larger mão','agua',1.19)
          )

cabe = cerveja[0] 
dados = cerveja[1:]


def recebe(cerveja):
    cabe = cerveja[0] # Separar o cabeçalho da tuplua
    dados = cerveja[1:] # Separar os dados da tupla
    lista_cerva = [] # Iniciar uma lista para receber os dados
    for dados_cerveja in dados: # For para quebrar os dados
        # Gerando o dicionário para armazenar os dados
        dicionario = {cabe[0]:dados_cerveja[0],cabe[1]:dados_cerveja[1],
                      cabe[2]:dados_cerveja[2],cabe[3]:dados_cerveja[3]}

        lista_cerva.append(dicionario) # Adicionando o dicionario na lista
    return lista_cerva #Retornando a lista para o programa.

print(recebe(cerveja))








# MINHA RESOLUÇÂO
# cerveja = (('marca', 'tipo', 'ibu','preco'),
#            ('Skol','IPA','ultra-leve',3.50),
#            ('Brahma','lager','leve/media',3.45),
#            ('Kaiser','Americam Larger','leve',2.35),
#            ('Sol','larger mão','agua',1.19))

# cabecalho = cerveja[0]
# marcas = cerveja[1:]

# for dados_cerveja in marcas:
#     print(f"{cabecalho[0]}: {dados_cerveja[0]}")
#     print(f"{cabecalho[1]}: {dados_cerveja[1]}")
#     print(f"{cabecalho[2]}: {dados_cerveja[2]}")
#     print(f"{cabecalho[3]}: {dados_cerveja[3]}\n")



