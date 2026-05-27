ven= float(input('Digite o valor da venda: '))
com= float(input('Digite o valor da compra: '))
nom= str(input('Digite o nome do produto: '))
v_lucro= ven - com
v_preju= com - ven
if ven > com:
    print('Teve lucro e foi no valor de {}'.format(v_lucro))
elif com > ven:
    print('Teve prejuizo e foi no valor de {}'.format(v_preju))
else:
    print('Os valores sao iguais')
print('O valor do preco de compra foi de {} e o valor do preco de venda foi de {} sendo que o nome do produto e {}'.format(com,ven,nom))