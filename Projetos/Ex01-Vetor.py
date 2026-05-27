lista= []
while True:
    numero = int(input('Digite algum numero (ou 0 para sair:) '))
    if numero == 0:
        break
    lista.append(numero)
print(lista)
for item in lista:
    print(item)
qnt= len(lista)
soma= sum(lista)
m= max(lista)
menor= min(lista)
print(f'Quantidade {qnt}')
print(f'Soma {soma}')
print(f'Maior {m}')
print(f'Menor {menor}')
pesquisa= int(input('Qual numero vc deseja pesquisar??? '))
if pesquisa in lista:
    print('Valor encontrado na lista.')
    print('O index da lista', lista.index(pesquisa))
else:
    print('Valor n encontrado na lista')
print('Ordenacao Lista')
lista.sort()
print(lista)



