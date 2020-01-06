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


# tripulação técnica - piloto e dois oficiais. 
# tripulação de cabine - chefe de serviço de voo e duas comissárias.
# um policial junto com um presidiário

# veículo que leva apenas duas pessoas
# piloto, chefe de serviço e policial podem dirigir.

# nenhum dos oficiais pode ficar sozinho com o chefe de serviço de bordo
# nenhuma das comissárias pode ficar sozinha com o piloto
# presidiário não pode ficar sozinho em momento algum com os tripulantes sem a presença do policia


passageiros = []

def levarPessoa(motorista, passageiro):
    print(f'Está embarcando o {motorista} e o {passageiro}')
    print(f'Fortwo chegou no destino')
    passageiros.append(passageiro)
    print(f'Voltando o {motorista}\n')

def ultimaViagem(motorista, passageiro):
    print(f'Está embarcando o {motorista} e o {passageiro}')
    print(f'Fortwo chegou no destino! Todos os passageiros estão no local, pronto para partir\n')
    passageiros.append(passageiro)
    passageiros.append(motorista)

primeiraViagem = levarPessoa('piloto', 'oficial')
segundaViagem = levarPessoa('piloto', 'oficial')
terceiraViagem = levarPessoa('chefe', 'piloto')
quartaViagem = levarPessoa('chefe', 'comissaria')
quintaViagem = levarPessoa('chefe', 'comissaria')
sextaViagem = levarPessoa('policial', 'chefe')
setimaViagem = ultimaViagem('policial', 'presidiario')

print(passageiros)