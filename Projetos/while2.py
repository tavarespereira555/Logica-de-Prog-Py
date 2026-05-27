menorv= 99999999
maiorv= -999999999999
cont= 0
soma= 0
m= 0
cont10= 0
while True:
    valor = int(input('Digite o numero (ou digite 0 para sair): '))
    if valor == 0 or valor == 99999999 or valor == -999999999999:
        break
    if valor < menorv:
        menorv = valor
    if valor > maiorv:
        maiorv= valor
    cont= cont + 1
    if valor > 10:
        cont10= cont10 + 1


    soma= soma + valor
    m = soma / cont
if cont > 0:
    print('O menor valor digitado sera de:', menorv)
    print('A quantidade de valores digitados e:', cont)
    print('A soma dos valores digitados sera de:',soma)
    print('A media aritimetica dos valores sera:',m)
    print('O maior valor digitado sera:', maiorv)
    print('OS valores digitador maiores que 10 e:',cont10)
else:
    print('Nenhum numero foi digitado')