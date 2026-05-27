
cont= 0
m= 0
contMaior10= 0
soma= 0
valorFinal= int(input('Digite o valor final: '))
ordem= str(input('Vc quer na ordem crescente ou descrecente??? [C/D] ')).strip().upper()
if ordem == 'C':
    for i in range(0, valorFinal + 1, 1):
        print(i, '-', 2 * i)
        cont = cont + 1
        soma = soma + i
        m = soma / cont
        if i > 10:
            contMaior10 = contMaior10 + 1
if ordem == 'D':
    for i in range(valorFinal, 0 - 1, 1):
        print(i, '-', 2 * i)
        cont = cont + 1
        soma = soma + i
        m = soma / cont
    if i > 10:
        contMaior10= contMaior10 + 1
print('A quatidade de valores sera:', cont)
print('A media dos valores sera de:', m)
print('A quantidade de valor mais q 10 sera de:', contMaior10)
