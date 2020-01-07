# A HBSIS Airlines é uma empresa de aviação que opera rotas internacionais a partir de Blumenau.
# Cada voo é tripulado por seis elementos, sendo que estes se dividem em dois grupos: a tripulação
# técnica e a tripulação de cabine. A tripulação técnica é constituída pelo piloto e dois oficiais. 
# A tripulação de cabine é constituída pelo chefe de serviço de voo e duas comissárias.
# O transporte dos tripulantes entre o terminal e o avião é efetuado através de um Smart Fortwo, que
# é um veículo que leva apenas duas pessoas. Por política da empresa, apenas o piloto e o chefe de
# serviço de voo podem dirigir este veículo. É também política da empresa que nenhum dos oficiais
# pode ficar sozinho com o chefe de serviço de bordo, e nem nenhuma das comissárias pode ficar
# sozinha com o piloto.  No terminal de embarque estão os seis tripulantes e ainda um policial 
# junto com um presidiário. Estes oito elementos terão que embarcar segundo as regras descritas acima. 
# A empresa não coloca nenhum limite para o número de viagens entre o terminal e o avião.
# Por motivos de segurança o presidiário não pode ficar sozinho em momento algum com os
# tripulantes sem a presença do policial, nem no terminal e nem no avião. De forma a facilitar o
# processo, a empresa autorizou que o policial pudesse dirigir o veículo também.

# Requisitos:

# 1 - Sempre que o Fortwo se mover, apresentar no console quando ele chega no destino
# 2 - Sempre que acontecer um embarque, apresentar quais elementos estão embarcando
# 3 - Sempre que acontecer um embarque no terminal, apresentar quem está no terminal
# 4 - Sempre que acontecer um embarque no avião, apresentar quem está no avião
# 5 - Deve ser feito em Python

passageiros = []
motoristaAguardo = []

print('-'*100)

def primeiraViagem(motorista, motorista2):
    motoristaAguardo.append(motorista2)
    print(f'Fortwo está indo em direção ao terminal com o {motorista} e o {motorista2}')
    print(f'Fortwo chegou no terminal, desembarca o {motorista2}')
    print(f'Fortwo está voltando com o {motorista} \n')

def adicionarPassageiro(motorista, passageiro):
    passageiros.append(passageiro)
    print(f'Fortwo está indo em direção ao terminal com o {motorista} e o {passageiro}')
    print(f'Fortwo chegou no terminal, desembarca o {passageiro}')
    print(f"Pessoas que estão no terminal: {', '.join(passageiros)}")
    print(f'Fortwo está voltando com o {motorista} \n')

def adicionarPassageiroMotorista(motorista, passageiro):
    passageiros.append(passageiro)
    passageiros.append(motorista)
    print(f'Fortwo está indo em direção ao terminal com o {motorista} e o {passageiro}')
    print(f'Fortwo chegou no terminal, desembarca o {motorista} e o {passageiro}')
    print(f"Pessoas que estão no terminal: {', '.join(passageiros)}")

    bool (motoristaAguardo)
    if motoristaAguardo:
        print(f"Voltando o {', '.join(motoristaAguardo)}\n")
        motoristaAguardo.pop()
    else:
        print(f'\nTodos os passageiros chegaram no terminal! Pronto para partir\n')

viagem1 = primeiraViagem('chefe', 'piloto')
viagem2 = adicionarPassageiroMotorista('policial', 'presidiario')
viagem3 = adicionarPassageiro('piloto', 'oficial')
viagem4 = adicionarPassageiro('piloto', 'oficial')
viagem5 = adicionarPassageiro('chefe', 'comissaria')
viagem6 = adicionarPassageiro('chefe', 'comissaria')
viagem7 = adicionarPassageiroMotorista('piloto', 'chefe')

print(f"Embarcaram no avião: {', '.join(passageiros)}\n")
print('-'*100)