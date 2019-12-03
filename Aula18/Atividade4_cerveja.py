cerveja = (('marca', 'tipo', 'ibu','preco'),
           ('Skol','IPA','ultra-leve',3.50),
           ('Brahma','lager','leve/media',3.45),
           ('Kaiser','Americam Larger','leve',2.35),
           ('Sol','larger mão','agua',1.19))

cabecalho = cerveja[0]
marcas = cerveja[1:]

for dados_cerveja in marcas:
    print(f"{cabecalho[0]}: {dados_cerveja[0]}")
    print(f"{cabecalho[1]}: {dados_cerveja[1]}")
    print(f"{cabecalho[2]}: {dados_cerveja[2]}")
    print(f"{cabecalho[3]}: {dados_cerveja[3]}\n")