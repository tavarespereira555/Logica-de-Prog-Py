def opera(m):
    if m > 0:
        print('Valor positivo')
    elif m == 0:
        print('Valor nulo')
    else:
        print('Valor negativo')
if __name__ == '__main__':
    num= float(input('Digite o numero: '))
    opera(num)