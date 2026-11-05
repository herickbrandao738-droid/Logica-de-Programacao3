# 5- Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e a sua opinião 
#em relação ao filme: ótimo=3, bom=2, regular=1. Faça um programa que receba a idade e a opinião de 
#15 espectadores e que calcule e mostre: (2 pontos)
#A média das idades das pessoas que responderam ótimo
#A quantidade de pessoas que respondeu regular
#A percentagem de pessoas que respondeu bom entre todos os espectadores analisados

espectadores = 0
totalPessoas = 0
idadeTotalOtimo = 0
mediaIdadeOtimo = 0
qtdOtimo = 0
qtdRegular = 0
qtdBom = 0
porcentagemBom = 0

while espectadores < 4:
    idade = int(input("Digite sua idade: "))
    opiniao = int(input("(ótimo = 3)\n(bom = 2)\n(regular = 1)\nDigite sua opinião em código: "))

    if opiniao != 1 and opiniao != 2 and opiniao != 3:
        print ("código inválido, digite o valor conforme a tabela.")
        continue

    if opiniao == 3:
        idadeTotalOtimo += idade
        qtdOtimo += 1
        mediaIdadeOtimo = idadeTotalOtimo/qtdOtimo

    elif opiniao == 1:
        qtdRegular += 1

    else:
        qtdBom += 1
        totalPessoas = qtdOtimo + qtdRegular + qtdBom
        porcentagemBom = (qtdBom / totalPessoas)*100

    espectadores += 1

print ("A média das idades que responderam ótimo é: " , mediaIdadeOtimo)
print ("A quantidade de pessoas que responderam regular é: " , qtdRegular)
print ("A porcentagem de pessoas que responderam Bom é: " , porcentagemBom , "%")