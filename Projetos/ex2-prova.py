cont= 0
soma= 0
m= 0
menor= 9999999999
maior= -999999999
contApro= 0
contRepro= 0
while True:
    nota= float(input('Digite o valor da sua nota: '))
    soma= soma + nota
    cont = cont + 1
    if nota < menor:
        menor= nota
    if nota > maior:
        maior= nota
    if nota >= 5:
        contapro= contApro + 1
    else:
        contrepro= contRepro + 1
    conti = str(input('Deseja continuar?? [S/N] ')).upper().strip()
    if conti == 'N':
        break
m= soma / cont
print('A quantidade de alunos da turma e:', cont)
print('A soma das notas das turmas sera:', soma)
print('A media dos alunos das turma sera de:', m)
print('A menor nota da turma vai ser:', menor)
print('A maior nota sera:', maior)

