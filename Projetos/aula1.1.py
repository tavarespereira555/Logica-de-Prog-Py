num1= float(input('Digite um valor: '))
num2= float(input('Digite outro valor: '))
if num2 > num1:
    print('O numero {} e maior que {}'.format(num2,num1))
elif num1 > num2:
    print('O numero {} e maior que o numero {}'.format(num1,num2))
else:
    print('Os  numeros {} e {} sao iguais'.format(num2,num1))