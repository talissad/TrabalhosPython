lista_alunos = []
lista_notas = []

n1 = 0
n2 = 1
n3 = 2
n4 = 3

for i in range (0,1):
    lista_alunos.append(input(f'Digite o nome do aluno: {i+1}: '))
    for n in range (0,4):
        lista_notas.append(float(input(f'Digite a nota {n+1}: ')))

for aluno in lista_alunos:
    media = (lista_notas[n1] + lista_notas[n2] + lista_notas[n3] + lista_notas[n4])/4
    resultado = 'Reprovado'
    if media >= 7:
        resultado = "Aprovado"

    print(f'Aluno: {aluno} - média = {media} - Resultado: {resultado}')

n1 += 4
n2 += 4
n3 += 4
n4 += 4