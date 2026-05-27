contmeio= 0  #o contmeio nesse caso seria porque esta na faixa entre 5 salarios e 10 salarios, se referindo que ele esta no meio
som= 0
salario= 0
contmenos5= 0
contmais= 0
total_folha= 0
print('======================================================================================================')
print('\033[31mVale salientar que esse progama e referente ao valor do salario minimo do  mes de marco no ano de 2026\033[m ')
print('======================================================================================================')
print('Se deseja um progama mais personalizado com suas necessidades entre em contato\natraves dos meus canais de atendimento\nWhatsApp: 61999368700\nEmail: Tavarespereira555@gmail.com')
while True:
    num= float(input('Qual o valor do seu salario??? R$').replace('.', '').replace(',', '.'))
    continuar= str(input('Deseja continuar?? [S/N] ')).strip().upper()
    salario= num / 1621.00
    if salario < 5:
        contmenos5= contmenos5 + 1
    elif 5 <= salario <= 10:
        contmeio= contmeio + 1
    else:
        contmais= contmais + 1
    total_folha= total_folha + num
    if continuar == 'N':
        break
print('A quantidade de funcionarios que recebem menos de 5 salarios minimos e {}'.format(contmenos5))
print('A quantidade de funcionarios que recebem entre 5 e 10  salarios minimos sera de:', contmeio)
print('A quantidade de funcionarios que recebem mais de 10 salarios mininos sera:', contmais)
print('A folha de pagamento em relacao aos funcionarios mencionados e igual a:', total_folha)