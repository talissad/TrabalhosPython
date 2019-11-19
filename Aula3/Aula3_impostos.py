def calculo_inss(salario):
    if salario <= 1751.81:
        inss = salario * 0.08
    elif salario >= 1751.82 and salario <= 2919.72:
        inss = salario * 0.09
    elif salario >= 2919.72 and salario <= 5839.45:
        inss = salario * 0.11
    else:
        inss = 642.3395
    return inss

def calculo_irrf(salario, inss):
    irrf = 0
    if salario >= 1903.95 and salario <= 2826.65:
        irrf = (((salario - inss) * 0.075)-142.800)
    elif (salario >= 2826.66 and salario <= 3751.05):
        irrf = (((salario - inss) * 0.15)-354.80)
    elif (salario >= 3751.06 and salario <= 4664.68):
        irrf = (((salario - inss) * 0.225)-636.13)
    elif (salario > 4664.68):
        irrf = (((salario - inss) * 0.275)-869.36)
    return irrf
