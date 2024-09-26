from game import JogoDaVelha
from algorithms import movimento_aleatorio, movimento_minimax, movimento_alphabeta

def main():
    while True:
        print("Escolha o modo de jogo:")
        print("1. Contra IA Aleatória")
        print("2. Contra IA Minimax")
        print("3. Contra IA Poda Alfa-Beta")
        modo = input("Escolha um modo (1-3): ")

        jogo = JogoDaVelha()
        jogador = "X"

        while True:
            jogo.mostrar_tabuleiro()
            if jogador == "X":
                posicao = int(input("Sua vez! Escolha uma posição (0-8): "))
                while not jogo.fazer_jogada(posicao, jogador):
                    print("Posição inválida! Tente novamente.")
                    posicao = int(input("Escolha uma posição válida (0-8): "))
            else:
                if modo == "1":
                    linha, coluna = movimento_aleatorio(jogo)
                elif modo == "2":
                    linha, coluna = movimento_minimax(jogo)
                elif modo == "3":
                    linha, coluna = movimento_alphabeta(jogo)
                jogo.fazer_jogada(linha * 3 + coluna, jogador)

            if jogo.verificar_vencedor(jogador):
                jogo.mostrar_tabuleiro()
                print(f"Jogador {jogador} venceu!")
                break
            elif jogo.jogo_terminado():
                jogo.mostrar_tabuleiro()
                print("Empate!")
                break

            jogador = "O" if jogador == "X" else "X"

        if input("Deseja jogar novamente? (s/n): ").lower() != "s":
            break

if __name__ == "__main__":
    main()
