# 8 - Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, 
# valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Qtd parcelas	% Juros sobre o valor inicial da dívida
# 1	                        0
# 3	                        10
# 6	                        15
# 9	                        20
# 12	                    25
# Saída do programa
# Valor da Dívida - Valor dos Juros - Qtd de Parcelas - Valor da Parcela R$ 1.000 0 1 R$ 1.000,00 R$ 1.100 100 3 
# R$ 366,00 R$ 1.150 150 6 R$ 191,67

divida = float(input("Digite o valor da dívida: "))
print("Qtd parcelas	% Juros sobre o valor inicial da dívida"
 "\n1	                        0"
 "\n3	                        10"
 "\n6	                        15"
 "\n9	                        20"
 "\n12	                        25")

while True:
    parcela = int(input("Digite a quantidade de parcelas: "))

    if parcela != 1 and parcela != 3 and parcela != 6 and parcela != 9 and parcela != 12:
        print ("Valor inválido!")
        continue
    elif parcela == 1:
        print ("O valor da dívda é: " , divida , "R$")
        print("O valor do juros aplicado: 0,00 R$")
        print ("Valor da parcela: 0,00R$")
        break
    elif parcela == 3:
        print ("O valor da dívida é: " , divida , "R$")
        print("O valor do juros aplicado: " , (divida * 1.1)-divida, "R$")
        print ("Valor da parcela: " , (divida * 1.1)/3, "R$")
        break
    elif parcela == 6:
        print ("O valor da dívida é: " , divida , "R$")
        print("O valor do juros aplicado: " , (divida * 1.15)-divida, "R$")
        print ("Valor da parcela: " , (divida * 1.15)/6, "R$")
        break
    elif parcela == 9:
        print ("O valor da dívida é: " , divida , "R$")
        print("O valor do juros aplicado: " , (divida * 1.2)-divida, "R$")
        print ("Valor da parcela: " , (divida * 1.2)/9, "R$")
        break
    else:
        print ("O valor da dívida é: " , divida , "R$")
        print("O valor do juros aplicado: " , (divida * 1.25)-divida, "R$")
        print ("Valor da parcela: " , (divida * 1.25)/12, "R$")
        break