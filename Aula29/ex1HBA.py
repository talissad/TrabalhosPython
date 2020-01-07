# lista_motorista = ['piloto', 'chefe', 'policial']
# lista_passageiro = ['presidiario', 'oficial 1', 'oficial 2', 'comissaria 1', 'comissaria 2']

#passageiroTerminal = ['piloto', 'chefe', 'policial', 'presidiario', 'oficial 1', 'oficial 2', 'comissaria 1', 'comissaria 2']
passageiroTerminal = []
passageiroAviao = []

def adicionarPassageiro():
    retorno = 's'
    while retorno == 's':
        opcao = input('Gostaria de adicionar alguém a viagem? (S/N) ')
        if opcao == 's':
            pessoaAdicionar = input('Digite o nome da pessoa a ser adicionada: ')
            arquivo = open("Aula29/cadastro.txt", "a")
            retorno = True
        elif opcao == 'n':
            break  

def ler_arquivo():
    arquivo = open("Aula29/cadastro.txt", "r")
    for pessoas in arquivo:
        pessoas = pessoas.strip().split()
        passageiroTerminal.append(pessoas)
    arquivo.close()

def deslocamentoAviao(lista):
    bool (passageiroTerminal)
    while passageiroTerminal:
        print(f"Passageiros esperando o deslocamento: {', '.join(passageiroTerminal)}")
        motorista = input('Digite o motorista: ')
        if motorista == 'piloto':
            passageiro = input('Digite o passageiro: ')
            if passageiro == 'chefe' or 'oficial 1' or 'oficial 2':
                passageiroAviao.append(passageiro)
                passageiroAviao.append(motorista)
                passageiroTerminal.remove(motorista)
                passageiroTerminal.remove(passageiro)
                print(f'Fortwo está indo ao avião com o {motorista} e o {passageiro}')
                print(f'Fortwo chegou ao avião\nDesembarcando o {motorista} e o {passageiro}')
            else:
                print('Opção inválida')

        elif motorista == 'chefe':
            passageiro = input('Digite o passageiro: ')
            if passageiro == ('piloto' or 'comissaria 1' or 'comissaria 2'):
                passageiroAviao.append(passageiro)
                passageiroAviao.append(motorista)
                passageiroTerminal.remove(motorista)
                passageiroTerminal.remove(passageiro)
                print(f'Fortwo está indo ao avião com o {motorista} e o {passageiro}')
                print(f'Fortwo chegou ao avião, desembarcando o {motorista} e o {passageiro}')

            else:
                print('Opção inválida')

        elif motorista == 'policial':
            passageiro = 'presidiario'
            passageiroAviao.append(motorista)
            passageiroAviao.append(passageiro)
            passageiroTerminal.remove(motorista)
            passageiroTerminal.remove(passageiro)   
            print(f'\nFortwo está indo ao avião com o {motorista} e o {passageiro}')
            print(f'Fortwo chegou ao avião, desembarcando o {motorista} e o {passageiro}')

        else:
            print('Digite uma opção válida')

        motoristaRetorno = input('\nDigite o motorista do retorno: ')
        if motoristaRetorno == ('chefe' or 'piloto'):
            passageiroAviao.remove(motoristaRetorno)
            passageiroTerminal.append(motoristaRetorno)
            print(f'Fortran retornando ao terminal com {motoristaRetorno}\n')
        elif motoristaRetorno =='policial':
            print('O policial não pode deixar o presidiario sozinho!')
        elif motoristaRetorno == '0':
            break       
        else:
            print('Somente o chefe e o piloto pode retornar')

#adicionar = adicionarPassageiro()
#inicio = ler_arquivo()
opcoesUsuario = deslocamentoAviao(passageiroTerminal)