from aaaa import contmenos5

soma= 0
m= 0
cont= 0
cont5= 0
contmenor5= 5
for i in range(1,6,1):
    cont= cont + 1
    nota= float(input('Digite o valor da {} nota: '.format(i)))
    soma= soma + nota
    if nota > 5:
        cont5 += 1
    else:
        contmenor5 += 1
m= soma / cont
print('A media dos alunos sera de:', m)