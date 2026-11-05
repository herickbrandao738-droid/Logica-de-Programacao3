# 10- Um professor registrou as notas de 35 alunos em uma prova. Faça um algoritmo que:
# ●     Leia o nome e a nota de cada aluno.
# ●     Informe a média geral da turma.
# ●     Conte quantos alunos tiveram nota acima de 7.

i = 0
mediaG = 0
Aluno7 = 0

while i < 35:
    nome = str(input("Digite o nome do aluno: "))
    nota = float(input("Digite a nota do aluno: "))
    notaG += nota
    mediaG = notaG / 35
    i += 1

    if nota >= 7:
        aluno7 += 1

print ("média da turma é: " , mediaG)
print (aluno7 , " Ficaram com a nota acima de 7")