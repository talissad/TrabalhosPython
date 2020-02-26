def trocar_posicao(qnt_vezes):
    lista = [1,2,3,4,5,6,7,8,9,10]

    print(f'\nLista original: {lista}\n')

    for i in range(1,qnt_vezes+1):
        lista.insert(0, lista[-1])
        del lista[-1]
        print(f'Rodada {i}: {lista}')

trocar_posicao(int(input('Digite a quantidade de vezes: ')))