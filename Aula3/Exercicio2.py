nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
nascimento = int(input('Digite o ano de seu nascimento: '))
ano = 2019

nascimento = ano - nascimento

print ('\nSeja bem vindx {} {}!\ns'.format (nome, sobrenome))


if nascimento < 18:
  print ('Produtos não alcoolicos \nSair')

else:
  print ('Produtos alcoolicos \nProdutos não alcoolicos \nSair')