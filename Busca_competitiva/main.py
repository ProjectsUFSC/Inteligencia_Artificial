from game import TicTacToe
from algorithms import random_ai_move, minimax_ai_move, alphabeta_ai_move

def main():
    print("Bem-vindo ao Jogo da Velha!")
    print("Escolha o modo de jogo:")
    print("1 - Contra IA Aleatória")
    print("2 - Contra IA com Minimax")
    print("3 - Contra IA com Poda Alfa-Beta")

    choice = int(input("Digite sua escolha (1, 2 ou 3): "))

    game = TicTacToe()
    
    if choice == 1:
        ai_move = random_ai_move
    elif choice == 2:
        ai_move = minimax_ai_move
    elif choice == 3:
        ai_move = alphabeta_ai_move
    else:
        print("Escolha inválida!")
        return

    # Loop do jogo
    while not game.is_over():
        game.print_board()

        # Movimento do jogador
        row = int(input("Digite a linha (0, 1 ou 2): "))
        col = int(input("Digite a coluna (0, 1 ou 2): "))

        if not game.make_move(row, col, "X"):
            print("Movimento inválido. Tente novamente.")
            continue

        # Verifica se o jogador venceu
        if game.check_winner("X"):
            print("Você venceu!")
            game.print_board()
            break

        # Movimento da IA
        ai_row, ai_col = ai_move(game)
        game.make_move(ai_row, ai_col, "O")
        print(f"IA jogou na linha {ai_row}, coluna {ai_col}")

        # Verifica se a IA venceu
        if game.check_winner("O"):
            print("A IA venceu!")
            game.print_board()
            break

    if not game.check_winner("X") and not game.check_winner("O"):
        print("Empate!")
    game.print_board()

if __name__ == "__main__":
    main()
