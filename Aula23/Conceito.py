# dias_mes = {
#     1: 31,
#     2: 28,
#     3: 31,
#     4: 30,
#     5: 31,
#     6: 30,
#     7: 31,
#     8: 31,
#     9: 30,
#     10: 31,
#     11: 30,
#     12: 31
#     }

########### METODO 1
# qual_mes = int(input('Digite o número do mês: '))

# print(f'O mês {qual_mes} tem {dias_mes[qual_mes]} dias')
# print(sum(list(dias_mes.values())[qual_mes-1:]))


########## METODO 2
# qual_mes = int(input('Digite o número do mês: '))

# total = 0
# for mes in range(qual_mes, 12+1):
#     total += dias_mes[mes]
# print(total)


########## METODO INTERAR EM DICIONARIO
# for chave in dias_mes:
#     print(f'Tenho uma chave nessa linha {chave}\nSe tenho uma chave, tenho o valor {dias_mes[chave]}\n')

# for chave, valor in dias_mes.items():
#     print(f'Para a chave {chave} o valor {valor}')




############# TUPLAS
# tupla = ('Texto', 1, 2, 3, 'Texto2', int, str, list)
# tupla2 = ('Texto', 'texto2', 'texto3', 'texto4')

# for isto in tupla:
#     print(type(isto))

# for isto in tupla2:
#     print(type(isto))
#     print(isto)