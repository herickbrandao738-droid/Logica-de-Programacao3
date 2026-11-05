#3-Faça um algoritmo que receba um número e mostre uma mensagem caso este número seja  maior que 80, 
# menor que 25 ou igual a 40. 

num = int(input("Digite um número: "))

if num < 25:
    print ("Este número é menor que 25.")
elif num == 40:
    print ("Este número é igual a 40.")
elif num > 80:
    print ("Este número é maior que 80.")