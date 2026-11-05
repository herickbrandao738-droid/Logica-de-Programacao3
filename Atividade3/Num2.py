#2 - Escrever um algoritmo que leia o nome e o sexo de 56 pessoas e informe o nome e se ela é homem ou mulher. 
# No final informe total de homens e de mulheres. 
masculino = 0
feminino = 0
for contagem in range (56):
    nome = str(input("Digite o nome do ser: "))
    sexo = str(input("Digite o sexo do ser: "))
    if sexo == "M" or sexo == "m":
        masculino += 1
    else:
        feminino += 1
print ("A quantidade de homens é: " , masculino)
print ("A quantidade de mulheres é: " , feminino)