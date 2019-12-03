lista = [['frutas','verduras','legumes','preço'],
         ['mamão','abacaxi','laranja','uva','pera','maçã','vergamota'],
         ['alface crespa', 'alface lisa','rucula','almerão','repolho','salsinha',],
         ['feijão', 'erviha', 'lentilha','vagem','feijão branco','gão de bico','soja'],
         [[10.00, 2.56, 5.25, 9.5, 10.05, 15, 5.75], 
         [2.99, 2.95, 3.5, 3.25, 5.89, 2.9, 2.5],
         [9.0, 5.0, 7.5, 1.75, 10.9, 5.99, 3.55]]
        ]

# Será solicitado o preço de alguns produtos. para imprimir deve ser por f-string refrenciando o nome com o preço 
# da seguinte forma: "O preço do {} é R$ {}"

print('-'*50, '\n'*2)

# 1: valor do abacaxi
print(f'O preço do {lista[1][1]} é R$ {lista[4][0][1]}')

# 2: valor da rucula
print(f'O preço do {lista[2][2]} é R$ {lista[4][1][2]}')

# 3: valor da laranja
print(f'O preço do {lista[1][2]} é R$ {lista[4][0][2]}')

# 4: o valor do repolho
print(f'O preço do {lista[2][4]} é R$ {lista[4][1][4]}')

# 5: o valor do feijão
print(f'O preço do {lista[3][0]} é R$ {lista[4][2][0]}')

# 6: o valor do feijão branco
print(f'O preço do {lista[3][4]} é R$ {lista[4][2][4]}')

# 7: o valor da vergamota
print(f'O preço do {lista[1][6]} é R$ {lista[4][0][6]}')

# 8: o valor da alface lisa
print(f'O preço do {lista[2][1]} é R$ {lista[4][1][1]}')

# 9: o valor do mamão
print(f'O preço do {lista[1][0]} é R$ {lista[4][0][0]}')

# 10: o valor da soja
print(f'O preço do {lista[3][6]} é R$ {lista[4][2][0]}')

# 11:  o valor da lentilha
print(f'O preço do {lista[3][2]} é R$ {lista[4][2][6]}')

# 12:  o valor da uva
print(f'O preço do {lista[1][3]} é R$ {lista[4][0][2]}')

# 13:  o valor da vagem
print(f'O preço do {lista[3][3]} é R$ {lista[4][2][3]}')

# 14:  o valor do almerão
print(f'O preço do {lista[2][3]} é R$ {lista[4][1][3]}')

# 15:  o valor da ervilha
print(f'O preço do {lista[3][1]} é R$ {lista[4][2][1]}')

# 16:  o valor da maçã
print(f'O preço do {lista[1][5]} é R$ {lista[4][0][5]}')

print( '\n'*2, '-'*50)