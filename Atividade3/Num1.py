#1-Ler 80 números e ao final informar quantos número(s) est(á)ão 
# no intervalo entre 10 (inclusive) e 150 (inclusive) 
numTotal = 0 
for num in range (1, 81):
    num = int(input("Digite um número: "))
    if num >=10 and num <=150:
        numTotal += 1
print (numTotal)