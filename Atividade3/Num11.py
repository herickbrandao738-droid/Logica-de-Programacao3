# 12- Uma sequência de 50 números será informada pelo usuário. Escreva um programa que:
# ●     Conte quantos desses números são múltiplos de 3.
# ●     Exiba a soma de todos os números pare

for i in range (50):
    num = int(input("Digite um número: "))

    if num % 3 == 0:
        mulTRES += 1
    if num % 2 == 0:
        numPAR += num

print ("A quantidade de números multiplos de 3 é: " , mulTRES)
print ("A soma dos números pares é: " , numPAR)