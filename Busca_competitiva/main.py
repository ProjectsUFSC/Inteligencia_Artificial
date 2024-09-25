from game import TicTacToe
from algorithms import random_ai_move, minimax_ai_move, alphabeta_ai_move

def position_to_coordinates(position):
    return position // 3, position % 3

def get_user_choice():
    while True:
        try:
            choice = int(input("Digite sua escolha (1, 2 ou 3): "))
            if choice in [1, 2, 3]:
                return choice
            print("Escolha inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida, digite um número.")

def get_user_position(game):
    while True:
        try:
            pos = int(input("Escolha uma posição (0-8): "))
            if 0 <= pos <= 8:
                row, col = position_to_coordinates(pos)
                if game.board[row][col] == " ":
                    return row, col
                else:
                    print("Essa posição já está ocupada. Tente novamente.")
            else:
                print("Escolha uma posição válida entre 0 e 8.")
        except ValueError:
            print("Entrada inválida, digite um número.")

def main():
    while True:
        print("Bem-vindo ao Jogo da Velha!")
        print("Escolha o modo de jogo:")
        print("1 - Contra IA Aleatória")
        print("2 - Contra IA com Minimax")
        print("3 - Contra IA com Poda Alfa-Beta")

        choice = get_user_choice()

        game = TicTacToe()
        
        if choice == 1:
            ai_move = random_ai_move
        elif choice == 2:
            ai_move = minimax_ai_move
        elif choice == 3:
            ai_move = alphabeta_ai_move

        # Loop do jogo
        while not game.is_over():
            game.print_board()

            # Movimento do jogador
            print("Sua vez! Escolha uma posição de 0 a 8:")
            row, col = get_user_position(game)
            game.make_move(row, col, "X")

            # Verifica se o jogador venceu
            if game.check_winner("X"):
                print("Você venceu!")
                game.print_board()
                break

            # Verifica se o jogo acabou antes do movimento da IA
            if game.is_over():
                break

            # Movimento da IA
            ai_row, ai_col = ai_move(game)
            if ai_row is not None and ai_col is not None:  # Verifica se a IA encontrou um movimento
                game.make_move(ai_row, ai_col, "O")
                print(f"IA jogou na posição {ai_row * 3 + ai_col}")

                # Verifica se a IA venceu
                if game.check_winner("O"):
                    print("A IA venceu!")
                    game.print_board()
                    break

        if not game.check_winner("X") and not game.check_winner("O"):
            print("Empate!")
        game.print_board()

        # Pergunta se o usuário quer jogar novamente
        play_again = input("Deseja jogar novamente? (s/n): ").lower()
        if play_again != 's':
            print("Obrigado por jogar!")
            break

if __name__ == "__main__":
    main()
