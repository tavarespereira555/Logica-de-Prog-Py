cont= 0
contAni= 0
print('DADO')
for i in range(1,6 +1,1):
    print('DADO 1')
    for i2 in range(1, 6 + 1,1):
        print(i, '-', i2, '', end='')
        contAni += 1
    cont= cont + 1
print('A quantidade de numeros digitaos sera:', cont)
print('A quantidade de numeros digitaos aninhados sera:', contAni)
