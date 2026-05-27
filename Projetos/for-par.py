inici= int(input('Digite o valor inicial: '))
final= int(input('Digite o valor final: '))
if inici < final:
    for num in range(inici, final + 1, 1):
        print(num)
else:
    for num in range(inici, final - 1, -1):
        print(num)