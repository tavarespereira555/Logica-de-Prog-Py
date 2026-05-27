cont= 0
maior= -9999999999999
menor= 99999999999999
contm= 0
contf= 0
m= 0
print('[0] para sair do progama na opcao de altura')
while True:
    altura= float(input('Digite sua altura: '))
    if altura == 0:
        break
    gener= str(input('Qual e o seu genero? [F/M]: ')).strip().upper()
    if altura > maior:
        maior= altura
    if altura < menor:
        menor= altura
    if gener == 'F':
        contm= contm + 1
    if gener == 'M':
        contf= contf + 1
    cont= cont + 1
m= altura / cont
print('A maior altura digitada e:',maior)
print('A menor altura digitada sera de:',menor)
print('A quantidade total de mulheres e:', contf)
print('A quantidade total de homens e:', contm)