def sub(valor1, valor2):
    subtracao= valor1 - valor2
    return subtracao
def calculo(valor1, valor2):
    #soma= valor1 + valor2
    return  valor1+ valor2
if __name__ == '__main__':
    num1= int(input('Digite o valor: '))
    num2 = int(input('Digite o valor: '))
    ope= int(input('[1]  Somar\n[2] Subtracao\nOpcao: '))
    if ope == 1:
        print('Valor retornado soma:', calculo(num1, num2))
    #v_retornado= calculo(num1, num2)
    #v_retorn_sub= sub(num1, num2)
    elif ope == 2 :
        print('Valor retornado subtracao:', sub(num1, num2))
    else:
        print('Opcao invalida')
