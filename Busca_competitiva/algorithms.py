import random

def random_ai_move(game):
    choice = [(r, c) for r in range(3) for c in range(3) if game.board[r][c] == " "]
    return random.choice(choice)

# Função de avaliação para Minimax
def evaluate(game):
    if game.check_winner("O"):
        return 1
    if game.check_winner("X"):
        return -1
    return 0

# IA usando Minimax
def minimax(game, depth, is_maximizing):
    score = evaluate(game)

    if score != 0 or game.is_over():
        return score

    if is_maximizing:
        best_score = -float("inf")
        for r in range(3):
            for c in range(3):
                if game.board[r][c] == " ":
                    game.board[r][c] = "O"
                    score = minimax(game, depth + 1, False)
                    game.board[r][c] = " "
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for r in range(3):
            for c in range(3):
                if game.board[r][c] == " ":
                    game.board[r][c] = "X"
                    score = minimax(game, depth + 1, True)
                    game.board[r][c] = " "
                    best_score = min(best_score, score)
        return best_score

def minimax_ai_move(game):
    best_score = -float("inf")
    best_move = None
    for r in range(3):
        for c in range(3):
            if game.board[r][c] == " ":
                game.board[r][c] = "O"
                score = minimax(game, 0, False)
                game.board[r][c] = " "
                if score > best_score:
                    best_score = score
                    best_move = (r, c)
    return best_move

# IA usando Poda Alfa-Beta
def alphabeta(game, depth, alpha, beta, is_maximizing):
    score = evaluate(game)

    if score != 0 or game.is_over():
        return score

    if is_maximizing:
        best_score = -float("inf")
        for r in range(3):
            for c in range(3):
                if game.board[r][c] == " ":
                    game.board[r][c] = "O"
                    score = alphabeta(game, depth + 1, alpha, beta, False)
                    game.board[r][c] = " "
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = float("inf")
        for r in range(3):
            for c in range(3):
                if game.board[r][c] == " ":
                    game.board[r][c] = "X"
                    score = alphabeta(game, depth + 1, alpha, beta, True)
                    game.board[r][c] = " "
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

def alphabeta_ai_move(game):
    best_score = -float("inf")
    best_move = None
    alpha = -float
