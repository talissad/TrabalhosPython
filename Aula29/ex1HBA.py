passageiroTerminal = []
passageiroAviao = []

def adicionar_arquivo():
    arquivo = open("Aula29/novo_cadastro.txt", "a")
    arquivo.write(f'{passageiroAviao}')
    arquivo.close()

# def adicionarPassageiro():
#     arquivo = open("Aula29/cadastro.txt", "a")
#     retorno = 's'
#     while retorno == 's':
#         retorno = input('Gostaria de adicionar alguém a viagem? (S/N) ')
#         if retorno == 's':
#             arquivo.write('\n'+input('Digite o nome da pessoa a ser adicionada: '))
#     arquivo.close()

def ler_arquivo():
    arquivo = open("Aula29/cadastro.txt", "r")
    for pessoas in arquivo:
        pessoas = pessoas.strip()
        passageiroTerminal.append(pessoas)
    arquivo.close()

def deslocamentoAviao():

    while bool(passageiroTerminal):
        print(f"Passageiros esperando o deslocamento: {', '.join(passageiroTerminal)}")
        motorista = input('Digite o motorista: ')

        if motorista in passageiroTerminal:
            if motorista == 'piloto':
                passageiro = input('Digite o passageiro: ')
                if passageiro in ['chefe', 'oficial 1', 'oficial 2']:
                    passageiroAviao.append(passageiro)
                    passageiroAviao.append(motorista)
                    passageiroTerminal.remove(motorista)
                    passageiroTerminal.remove(passageiro)
                    print(f'Fortwo está indo ao avião com o {motorista} e o {passageiro}')
                    print(f'Fortwo chegou ao avião\nDesembarcando o {motorista} e o {passageiro}')
                else:
                    print(f'Opção inválida! {passageiro} não pode ficar sozinho com {motorista}')
                    continue

            elif motorista == 'chefe':
                passageiro = input('Digite o passageiro: ')
                if passageiro in ['piloto', 'comissaria 1', 'comissaria 2']:
                    passageiroAviao.append(passageiro)
                    passageiroAviao.append(motorista)
                    passageiroTerminal.remove(motorista)
                    passageiroTerminal.remove(passageiro)
                    print(f'Fortwo está indo ao avião com o {motorista} e o {passageiro}')
                    print(f'Fortwo chegou ao avião, desembarcando o {motorista} e o {passageiro}')

                else:
                    print(f'Opção inválida! {passageiro} não pode ficar sozinho com {motorista}')
                    continue

            elif motorista == 'policial':
                if 'chefe' in passageiroAviao or 'piloto' in passageiroAviao:
                    passageiro = 'presidiario'
                    passageiroAviao.append(motorista)
                    passageiroAviao.append(passageiro)
                    passageiroTerminal.remove(motorista)
                    passageiroTerminal.remove(passageiro)   
                    print(f'\nFortwo está indo ao avião com o {motorista} e o {passageiro}')
                    print(f'Fortwo chegou ao avião, desembarcando o {motorista} e o {passageiro}')
                else:
                    print(f'O policial não pode dirigir, pois não poderá deixar o presidiario no avião para voltar.')
                    continue
            else:
                print(f'O {motorista} não pode dirigir. Digite uma opção válida.')
                continue

            if len(passageiroTerminal) > 0:
                while True:
                    print(f"Passageiros no avião: {', '.join(passageiroAviao)}")
                    motoristaRetorno = input('\nDigite o motorista do retorno: ')
                    if motoristaRetorno in passageiroAviao:
                        if motoristaRetorno == 'chefe' or motoristaRetorno == 'piloto':
                            passageiroAviao.remove(motoristaRetorno)
                            passageiroTerminal.append(motoristaRetorno)
                            print(f'Fortran retornando ao terminal com {motoristaRetorno}\n')
                            break
                        elif motoristaRetorno == 'policial':
                            print('O policial não pode deixar o presidiario sozinho!')                
                        else:
                            print('Somente o chefe e o piloto pode retornar')
                    else:
                        print(f'O {motoristaRetorno} não está no avião, portanto não pode ser o motorista do retorno.')
        else:
            print(f'O {motorista} não está esperando o deslocamento.')

ler_arquivo()
deslocamentoAviao()
adicionar_arquivo()