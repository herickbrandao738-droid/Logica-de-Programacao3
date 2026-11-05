# 7 - O cardápio de uma lanchonete é o seguinte:
# Especificação      Código     Preço
# Cachorro Quente     100      R$ 1,20
# Bauru Simples       101      R$ 1,30
# Bauru com ovo       102      R$ 1,50
# Hambúrguer          103      R$ 1,20
# Cheeseburguer       104      R$ 1,30
# Refrigerante        105      R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
# Calcule e mostre o valor a ser pago por item (preço *quantidade) e o total geral do pedido. 
# Considere que o cliente deve informar quando o pedido deve ser encerrado.

pagamentoTotal = 0
pagamentoCQ = 0
pagamentoBS = 0
pagamentoBCO = 0
pagamentoH = 0
pagamentoC = 0
pagamentoR = 0


while True:
    cod = int(input("Digite 0 para encerrar entrada do pedido\nDigite o código do item: "))
    qtd = int(input("Digite a quantidade de itens que você deseja: "))

    if cod == 100:
        pagamentoCQ += qtd * 1.20
        print ("O valor a ser pago no item = Cachorro Quente é: " , pagamentoCQ)
        pagamentoTotal += pagamentoCQ

    elif cod == 101:
        pagamentoBS += qtd * 1.30
        print ("O valor a ser pago no item = Bauru Simples é: " , pagamentoBS)
        pagamentoTotal += pagamentoBS

    elif cod == 102:
        pagamentoBCO += qtd * 1.50
        print ("O valor a ser pago no item = Bauru com ovo é: " , pagamentoBCO)
        pagamentoTotal += pagamentoBCO

    elif cod == 103:
        pagamentoH += qtd * 1.20
        print ("O valor a ser pago no item = Hambúrguer é: " , pagamentoH)
        pagamentoTotal += pagamentoH

    elif cod == 104:
        pagamentoC += qtd * 1.30
        print ("O valor a ser pago no item = Cheeseburguer é: " , pagamentoC)
        pagamentoTotal += pagamentoC

    elif cod == 105:
        pagamentoR += qtd * 1.00
        print ("O valor a ser pago no item = Refrigerante é: " , pagamentoR)
        pagamentoTotal += pagamentoR

    elif cod == 0:
        break

    else:
        print ("Código inválido!")

print ("O valor total a ser pago nessa compra é: " , pagamentoTotal)
print ("O valor a ser pago no item = Cachorro Quente é: " , pagamentoCQ)
print ("O valor a ser pago no item = Bauru Simples é: " , pagamentoBS)
print ("O valor a ser pago no item = Bauru com ovo é: " , pagamentoBCO)
print ("O valor a ser pago no item = Hambúrguer é: " , pagamentoH)
print ("O valor a ser pago no item = Cheeseburguer é: " , pagamentoC)
print ("O valor a ser pago no item = Refrigerante é: " , pagamentoR)