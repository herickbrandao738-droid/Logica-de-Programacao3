# Entrada contínua de temperaturas.
# Regras:
# Ignorar valores < -50 ou > 150
# Encerrar com 999
# Contar temperaturas:
# Entre 20 e 80
# Múltiplas de 5
# Que não sejam divisíveis por 10
# Exibir:
# Quantidade válida
# Maior temperatura válida
# Percentual válido sobre total digitado

total = 0
qtdValida = 0
entre20e80 = 0
multiplos5 = 0
naoDiv10 = 0
maior = -51

while True:
    temperatura = float(input("Digite a temperatura (999 para encerrar): "))

    if temperatura == 999:
        break

    total += 1

    if temperatura < -50 or temperatura > 150:
        print("Temperatura invalida!")
        continue

    qtdValida += 1

    if temperatura > maior:
        maior = temperatura

    if temperatura >= 20 and temperatura <= 80:
        entre20e80 += 1

    if temperatura % 5 == 0:
        multiplos5 += 1

    if temperatura % 10 != 0:
        naoDiv10 += 1

print("Quantidade valida:", qtdValida)
print("Temperaturas entre 20 e 80:", entre20e80)
print("Temperaturas multiplas de 5:", multiplos5)
print("Temperaturas nao divisiveis por 10:", naoDiv10)

if qtdValida > 0:
    print("Maior temperatura valida:", maior)
else:
    print("Nenhuma temperatura valida!")

if total > 0:
    percentual = qtdValida / total * 100
else:
    percentual = 0

print("Percentual de temperaturas validas:", percentual, "%")