import datetime
atual= datetime.date.today().year
ano= int(input('Digite o ano em que vc nasceu: '))
nom= str(input('Digite seu nome: '))
ida= atual - ano
print('Sua idade sera {} e o ano de nascimento e {} e seu nome e {}'.format(ida,ano,nom))
if ida > 16 and ida > 18:
    print('Pode votar, Pode CNH')
elif ida >= 16 and ida < 18:
    print('Pode votar, n pode ter CNH')
else:
    print('Nao pode votar, n pode ter CNH')