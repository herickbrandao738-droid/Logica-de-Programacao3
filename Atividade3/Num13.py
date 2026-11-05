#  13-Simulação de Crescimento Populacional com Evento Crítico
# Duas populações A e B crescem anualmente:
# A cresce 3% ao ano
# B cresce 1,5% ao ano
# A cada 5 anos ocorre uma crise que reduz ambas em 7%.
# Determine em quantos anos A ultrapassa B, considerando valores iniciais informados pelo usuário.

ano = 0
popA3 = 0
popB15 = 0
popA = 0
popB = 0

popA = int(input("Digite a quantiade de habitantes A: "))
popB = int(input("Digite a quantiade de habitantes B: "))

while True:
    popA3 = popA * 1.03
    popB15 = popB * 1.015
    ano += 1

    if ano % 5 == 0:
        popA3 = popA3 * 0.93
        popB15 = popB15 * 0.93

    popA = popA3
    popB = popB15

    if popA3 > popB15:
        print ("A quantiade de anos que levou para a população A passar a população B foi: " , ano)
        break