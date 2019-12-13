cadastro_banda = []
cadastro_album = []
cadastro_musica = []

print('''
Digite 1 para cadastrar uma banda
Digite 2 para cadastrar um album
Digite 3 para cadastrar uma música
e 4 para Sair
''')

while True:
    opcao = int(input('Digite a opção: '))
    if opcao == 1:
        cadastro_banda.append(input('Digite a Banda: '))
    elif opcao == 2:
        cadastro_album.append(input('Digite o Album: '))
    elif opcao == 3: 
        cadastro_musica.append(input('Digite a Musica: '))
    elif opcao == 4:
        break
    else:
        print('digite uma opção válida')

print(f'Bandas cadastradas: {cadastro_banda}\nAlbuns cadastrados: {cadastro_album}\nMúsicas cadastradas: {cadastro_musica}\n')
