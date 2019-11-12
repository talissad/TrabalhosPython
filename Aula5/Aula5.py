print('\n')
numero1 = float(input('digite a primeira nota: '))
numero2 = float(input('digite a segunda nota: '))
numero3 = float(input('digite a terceira nota: '))
numero4 = float(input('digite a quarta nota: '))

media = ((numero1 + numero2 + numero3 + numero4) / 4)

print('\n')

#Imprime a maior nota
'''if numero1 > numero2 and numero1 > numero3 and numero1 > numero4:
    print ('A maior nota é a primeira:', numero1)
elif  numero2 > numero3 and numero2 > numero4:
    print ('A maior nota é a segunda:', numero2)
elif numero3 > numero4:
    print ('A maior nota é a terceira:', numero3)
else:
    print ('A maior nota é a quarta:', numero4)'''

lista = [numero1, numero2, numero3, numero4]
print ('A maior nota foi:', max(lista))

#Imprime a menor nota
'''if numero1 < numero2 and numero1 < numero3 and numero1 < numero4:
    print ('A menor nota é a primeira:', numero1)
elif  numero2 < numero3 and numero2 < numero4:
    print ('A menor nota é a segunda:', numero2)
elif numero3 < numero4:
    print ('A menor nota é a terceira:', numero3)
else:
    print ('A menor nota é a quarta:', numero4)'''

lista = [numero1, numero2, numero3, numero4]
print ('A menor nota foi:', min(lista))

print ('\nA média é:', media )

# Verifica a situação do Aluno
if media >= 7:
    print('Aprovado \n')
else:
    print("Reprovado \n")