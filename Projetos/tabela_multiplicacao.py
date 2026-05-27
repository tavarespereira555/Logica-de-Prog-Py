contador= 0
print("-=-=-=-=-=-= Tabela de tabuada -=-=-=-=-=-=")
while True:
    num = int(input("Digite o numero para ver sua tabuada: "))
    opc = str(input("Vc quer a tabuada de multiplicacao ou soma??? [S/M] ")).strip().upper()
    contador = contador + 1
    if opc == "M":

        for i in range(1, 10 + 1, 1):
            print(f"{num} x {i:2} = {i*num:2}")
    elif opc == "S":
        for i in range(1, 10 + 1, 1):
            print(f"{num} + {i:2} = {i+num:2}")
    else:
        print("Opcao invalida")
    cont= int(input('0 para encerar ou 1 para continuar: '))
    if cont == 0:
        break
print('A quantidade de numeros digitados foi:', contador)

#<img href='link'></img>