def time(hr, minu):
    hora= hr * 60
    v_conver= hora + minu
    return v_conver
if __name__ == '__main__':
    """for i in range(1,3):
        horas = int(input('Digite o valor da hora: '))
        minutos = int(input('Digite o valor dos minutos: '))
        v_retornado = time(horas, minutos)
        contadorNum= contadorNum + v_retornado"""
    horas = int(input('Digite o valor da hora: '))
    minutos = int(input('Digite o valor dos minutos: '))
    v_retornado = time(horas, minutos)
    horas2 = int(input('Digite o valor da hora: '))
    minutos2 = int(input('Digite o valor dos minutos: '))
    v_retornado2 = time(horas2, minutos2)
    diferenca= v_retornado - v_retornado2
    if v_retornado > v_retornado2:
        print('O primeiro horario e maior')
    elif v_retornado2 > v_retornado:
        print('O segundo horario e maior')
    else:
        print('Os horarios são iguais')
    #print(f'O valor total das horas convertidas em minutos sera: {v_retornado2}')
    print(f'A diferenca entres os valores convertidos em minutos sera de: {diferenca}')
