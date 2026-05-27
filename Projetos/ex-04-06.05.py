def absoluto(n):
    if n < 0:
        n= n * -1
    return n
if __name__ == '__main__':
    num= float(input('Digite o numero: '))
    v_retornado= absoluto(num)
    print(f'O valor absoluto de {num} sera: {v_retornado} ')