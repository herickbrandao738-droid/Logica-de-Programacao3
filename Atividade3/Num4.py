#Uma loja utiliza o código 1 para transação à vista e 2 para transação a prazo. 
# Faça um programa que receba o código e o valor de 15 transações. Calcule e mostre: 
#O valor total das compras à vista
#O valor total as compras a prazo
#O valor total das compras efetuadas
#O valor da primeira prestação das compras a prazo, sabendo se que essas serão pagas em três vezes

valorItem = 0
compras = 0
valorTotal = 0
compraVista = 0
compraPrazo = 0

while compras < 3:
    pagamento = int(input("(transação a vista = 1)\n(transação a prazo = 2) \nDigite o código de tipo de transação: "))

    if pagamento != 1 and pagamento != 2:
        print("Código inválido! Digite 1 ou 2.")
        continue

    valorItem = float(input("Digite o valor do item: "))
    valorTotal += valorItem
    compras += 1

    if pagamento == 1:
        compraVista += valorItem
        print ("O valor da compra é: " , compraVista + compraPrazo)

    elif pagamento == 2:
        compraPrazo += valorItem
        print ("O valor da compra é: " , (compraPrazo + compraVista)/3)

    valorTotal = compraPrazo + compraVista

print ("O valor total da compra é: " , valorTotal)
print ("O valor total das compras a vista: " , compraVista)
print ("O valor total das compras a prazo: " , compraPrazo)
print ("O valor da primeira prestação é: " , (compraPrazo)/3)