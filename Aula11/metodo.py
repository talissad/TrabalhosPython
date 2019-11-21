def iss(salario, imposto):
    return salario * (imposto/100)




def rentabilidade(valor, taxa):
    montante = valor * (1 + (taxa/100)) ** 12
    return montante




def tesouroDireto(compras, taxa, periodo):
    montante = compras * (1 + (taxa/100)) ** periodo
    return montante