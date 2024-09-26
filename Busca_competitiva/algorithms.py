import random

def random_ai_move(game):
    empty_positions = [(row, col) for row in range(3) for col in range(3) if game.board[row][col] == " "]
    return random.choice(empty_positions) if empty_positions else (None, None)

def minimax_ai_move(game):
    # Implementação do Minimax (você pode adaptar conforme sua lógica)
    pass  # Adicione sua lógica aqui

def alphabeta_ai_move(game):
    def alphabeta(node, depth, alpha, beta, maximizing_player):
        if game.check_winner("X"):
            return -1  # jogador ganhou
        elif game.check_winner("O"):
            return 1  # IA ganhou
        elif game.is_over():
            return 0  # empate

        if maximizing_player:
            max_eval = -float('inf')
            for row in range(3):
                for col in range(3):
                    if node[row][col] == " ":
                        node[row][col] = "O"  # IA joga
                        eval = alphabeta(node, depth + 1, alpha, beta, False)
                        node[row][col] = " "  # desfeita movimento
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = float('inf')
            for row in range(3):
                for col in range(3):
                    if node[row][col] == " ":
                        node[row][col] = "X"  # jogador joga
                        eval = alphabeta(node, depth + 1, alpha, beta, True)
                        node[row][col] = " "  # desfeita movimento
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval

    best_move = None
    best_value = -float('inf')
    for row in range(3):
        for col in range(3):
            if game.board[row][col] == " ":
                game.board[row][col] = "O"  # IA joga
                move_value = alphabeta(game.board, 0, -float('inf'), float('inf'), False)
                game.board[row][col] = " "  # desfeita movimento
                if move_value > best_value:
                    best_value = move_value
                    best_move = (row, col)

    return best_move if best_move else (None, None)

