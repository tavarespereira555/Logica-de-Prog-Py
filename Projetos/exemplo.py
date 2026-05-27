import os
import time

# Cores para o terminal (Códigos ANSI)
RESET = "\033[0m"
NEON_BLUE = "\033[38;5;45m"
NEON_PINK = "\033[38;5;206m"
WHITE = "\033[97m"
GRAY = "\033[90m"
GREEN = "\033[32m"
RED = "\033[31m"


def limpar_tela():
    # Limpa o terminal no Windows ou Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_cabecalho():
    print(f"{NEON_BLUE}┌────────────────────────────────────────┐{RESET}")
    print(f"{NEON_BLUE}│ {WHITE}      🚀 PAINEL DE CONTROLE v1.0 {NEON_BLUE}      │{RESET}")
    print(f"{NEON_BLUE}└────────────────────────────────────────┘{RESET}")


def mostrar_menu():
    limpar_tela()
    mostrar_cabecalho()
    print(f"  {NEON_PINK}1{RESET} {GRAY}─{RESET} {WHITE}Visualizar Relatórios{RESET}")
    print(f"  {NEON_PINK}2{RESET} {GRAY}─{RESET} {WHITE}Gerenciar Usuários{RESET}")
    print(f"  {NEON_PINK}3{RESET} {GRAY}─{RESET} {WHITE}Configurações do Sistema{RESET}")
    print(f"  {GRAY}────────────────────────────────────────{RESET}")
    print(f"  {RED}0{RESET} {GRAY}─{RESET} {RED}Sair do Programa{RESET}")
    print(f"{NEON_BLUE}──────────────────────────────────────────{RESET}")


def aguardar_usuario():
    input(f"\n{GRAY}Pressione [Enter] para voltar ao menu...{RESET}")


def main():
    while True:
        mostrar_menu()

        try:
            opcao = input(f"{NEON_BLUE}⚡ Escolha uma opção: {RESET}").strip()

            if opcao == "1":
                limpar_tela()
                mostrar_cabecalho()
                print(f"\n{GREEN}📊 Carregando relatórios de vendas...{RESET}")
                # Seu código aqui
                aguardar_usuario()

            elif opcao == "2":
                limpar_tela()
                mostrar_cabecalho()
                print(f"\n{GREEN}👥 Acessando banco de usuários...{RESET}")
                # Seu código aqui
                aguardar_usuario()

            elif opcao == "3":
                limpar_tela()
                mostrar_cabecalho()
                print(f"\n{GREEN}⚙️ Abrindo painel de configurações...{RESET}")
                # Seu código aqui
                aguardar_usuario()

            elif opcao == "0":
                limpar_tela()
                print(f"\n{NEON_PINK}👋 Sistema encerrado. Até logo!{RESET}\n")
                break

            else:
                print(f"\n{RED}❌ Opção inválida! Tente novamente.{RESET}")
                time.sleep(1.5)

        except KeyboardInterrupt:
            print(f"\n\n{RED}➔ Programa interrompido.{RESET}\n")
            break


if __name__ == "__main__":
    main()
