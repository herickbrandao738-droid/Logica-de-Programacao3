# 9- Uma empresa utiliza os códigos 1 para funcionários do setor administrativo e 2 para os funcionários do 
# setor operacional. Faça um programa que receba o código e o salário de 20 funcionários. Calcule e mostre:
# ●     A média salarial do setor administrativo.
# ●     A média salarial do setor operacional.
# ●     O total de salários pagos pela empresa.
# ●     A quantidade de funcionários em cada setor.

funcionarioADM = 0
funcionarioOP = 0
salarioADM = 0
salarioOP = 0
qtdADM = 0
qtdOP = 0
i = 0

while i < 5:
    cod = int(input("(Cod 1 = funcionários do setor ADM)\n(Cod 2 = funcionários do setor OP)\nDigite o código do funcionário: "))

    if cod != 1 and cod != 2:
        print ("Código inválido!")
        continue
    elif cod == 1:
        salario1 = float(input("Digite o salário do funcionário: "))
        salarioADM += salario1
        qtdADM += 1
        mediaADM = salarioADM / qtdADM
        i += 1

    else:
        salario2 = float(input("Digite o salário do funcionário: "))
        salarioOP += salario2
        qtdOP += 1
        mediaOP = salarioOP / qtdOP
        i += 1

print ("O total de salários pago pela empresa é: " , salarioADM + salarioOP)
print ("O total de funcionários no setor ADM é: " , qtdADM)
print ("O total de funcionários no setor OP é: " , qtdOP)
print ("A média salarial do setor ADM é: " , mediaADM)
print ("A média salarial do setor OP é: " , mediaOP)