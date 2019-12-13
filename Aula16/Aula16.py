#Cadastro de playlist
#lendo musica, artista e album

from faixa import criar_faixa, salvar_faixa, ler_faixa

musica = input('Digite uma música: ')
album = input('Digite o nome do album: ')
artista = input('Digite o nome do artista: ')

faixa1 = criar_faixa(musica, album, artista)
salvar_faixa(faixa1)
lista = ler_faixa()

for faixa in lista:
    print(f'{faixa["musica"]} - {faixa["album"]} - {faixa["artista"]}')
