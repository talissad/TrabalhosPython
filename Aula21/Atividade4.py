# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Faça um programa que abra um arquivo.txt
# 2 - Trate para que não tenha ao abrir o arquivo
# 3 - Caso não haja erro apareça a mensagem de "Arquivo aberto"
# 4 - Se houver erro, apareça a mensagem 
# "Envidando dados para função tratar_dados() "

# Ao finalizar, obrigar o fechamento do arquivo

# dica: linha 204 do arquivo execoes.py

try:
    arquivo = open('Aula21/Explicação_Try_Except_Teste.txt', 'r')

except OSError:
    print('Envidando dados para função tratar_dados() ')

finally:
    if 'arquivo' in dir():
	    print('Tudo certo, fechando arquivo!')
	    arquivo.close()