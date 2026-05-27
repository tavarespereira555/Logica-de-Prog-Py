def calcula_dobro(p_valor):
    dobro= p_valor * 2
    return dobro
if __name__ == '__main__':
    num= int(input('Digite o numero inteiro: '))
    v_retornado= calcula_dobro(num)
    print('O valor retornado pela funcao:', v_retornado)