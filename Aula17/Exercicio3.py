from random import randint

# t = 1
# while True:
#     aleatorio = randint(1,50)
#     n = 50
#     if aleatorio != n:
#         print(f'Tentativa {t} = {aleatorio}, {n}')
#         t = t + 1
#     else:
#         print(f'Acertou! {aleatorio} = {n}')
#         break



aleatorio = randint(1,10)
numero = 0

while not numero == aleatorio:
    numero = int(input('Digite um número: '))
    if numero > aleatorio:
        print('O número é menor!')
        continue
    elif numero < aleatorio:
        print('O número é maior!')
        continue
    else:
        print(f'Acertou! {aleatorio} = {numero}')
    break