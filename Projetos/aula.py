num= int(input('Digite um numero: '))
num_r= num % 2
if num % 2 == 0:
    print('Esse numero e \033[31mPAR\033[m')
else:
    print('Esse numero e \033[33mIMPAR\033[m')
print('O numero digitado e {} e o numero do resto da divisao sera de {}'.format(num,num_r))
if num  % 5 == 0:
    print('Esse numero e divisivel por 5')
else:
    print('Esse numero n e divisivel por 5')
