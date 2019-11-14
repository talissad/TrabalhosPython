aluno = []
nota1 = []
nota2 = []
nota3 = []
nota4 = []

for i in range (0,10):
    aluno.append(input("Digite o nome do aluno: "))
    nota1.append(int(input("Digite a primeira nota: ")))
    nota2.append(int(input("Digite a segunda nota: ")))
    nota3.append(int(input("Digite a terceira nota: ")))
    nota4.append(int(input("Digite a quarta nota: ")))

for i in range (0,10):
    print ('\nNome do Aluno:', aluno[i],'\nNotas:', nota1[i], nota2[i], nota3[i], nota4[i])
    media = ((nota1[i] + nota2[i] + nota3[i] + nota4[i])/4)
    print ('A media foi de: ', media)

    if media >= 7:
        print('Status: Aprovado')

    else:
        print('Status: Reprovado')