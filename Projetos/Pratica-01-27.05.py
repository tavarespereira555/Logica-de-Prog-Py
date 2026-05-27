RESET = "\033[0m"
NEON_BLUE = "\033[38;5;45m"
NEON_PINK = "\033[38;5;206m"
WHITE = "\033[97m"
GRAY = "\033[90m"
GREEN = "\033[32m"
RED = "\033[31m"
lista= []
def create():
    while True:
        nome=str(input('Digite o nome: '))
        if not nome:
            break
        lista.append(nome)


def read():
        print('Valores da lista ->')
        len(lista)
        if len(lista) > 0:
            for item in lista:
                print(f' ->{item}')
        else:
            print('Lista vazia')


def update():
    novo_nome= str(input('Digite o novo nome: '))
    indice= int(input('Digite o indice (posicao): '))
    lista[indice]= novo_nome
    print(lista)


def delet():
    remover= str(input('Qual nome vc quer remover da lista: '))
    lista.remove(remover)
    print(lista)


def mostrar_cabecalho():
    print(f"{NEON_BLUE}┌────────────────────────────────────────┐{RESET}")
    print(f"{NEON_BLUE}│ {WHITE}      🚀 CRUD  v1.0 {NEON_BLUE}                   │{RESET}")
    print(f"{NEON_BLUE}└────────────────────────────────────────┘{RESET}")


def mostrar_menu():
    print(f"  {NEON_PINK}C{RESET} {GRAY}─{RESET} {WHITE}Create{RESET}")
    print(f"  {NEON_PINK}R{RESET} {GRAY}─{RESET} {WHITE}Read{RESET}")
    print(f"  {NEON_PINK}U{RESET} {GRAY}─{RESET} {WHITE}Update{RESET}")
    print(f"  {NEON_PINK}D{RESET} {GRAY}─{RESET} {WHITE}Delete{RESET}")
    print(f"  {GRAY}────────────────────────────────────────{RESET}")
    print(f"  {RED}E{RESET} {GRAY}─{RESET} {RED}Sair do Programa{RESET}")
    print(f"{NEON_BLUE}──────────────────────────────────────────{RESET}")



if __name__ == '__main__':
    while True:
        mostrar_cabecalho()
        mostrar_menu()
        opcao_ini= str(input('Opcao: ')).upper().strip()
        if opcao_ini == 'E':
            break
        if not opcao_ini:
            continue
        if opcao_ini == 'C':
            create()
        elif opcao_ini == 'R':
            read()
        elif opcao_ini == 'U':
            update()
        elif opcao_ini == 'D':
            delet()
        else:
            print('OPCAO INVALIDA')

