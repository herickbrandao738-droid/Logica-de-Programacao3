# 11- Uma pesquisa de satisfação foi realizada com 40 clientes de uma loja, 
# pedindo que avaliassem o atendimento como: péssimo = 1, regular = 2, bom = 3, excelente = 4. 
# Faça um programa que leia a avaliação e a idade dos clientes e exiba:
# ●     A média de idade dos clientes que avaliaram como "excelente".
# ●     O total de clientes que avaliaram como "péssimo".
# ●     A porcentagem de clientes que avaliaram como "bom" em relação ao total.

clientes = 0
totalPessoas = 0

idadeTotal = 0
mediaIdadeExcelente = 0
qtdExcelente = 0

qtdPessimo = 0

qtdBom = 0
porcentagemBom = 0

while clientes < 40:
    idade = int(input("Digite sua idade: "))
    opiniao = int(input("(péssimo = 1)\n(regular = 2)\n(bom = 3)\n(excelente = 4)\nDigite sua opinião em código: "))

    if opiniao != 1 and opiniao != 2 and opiniao != 3 and opiniao != 4:
        print ("código inválido")
        continue

    if opiniao == 4:
        idadeTotal += idade
        qtdExcelente += 1
        mediaIdadeExcelente = idadeTotal/qtdExcelente

    elif opiniao == 1:
        qtdPessimo += 1

    elif opiniao == 3:
        qtdBom += 1
        totalPessoas = qtdExcelente + qtdPessimo + qtdBom
        porcentagemBom = (qtdBom / totalPessoas)*100

    clientes += 1

print ("A média das idades que responderam Excelente é: " , mediaIdadeExcelente)
print ("A quantidade de pessoas que responderam Péssimo é: " , qtdPessimo)
print ("A porcentagem de pessoas que responderam Bom é: " , porcentagemBom , "%")