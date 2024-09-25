class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
    
    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)
    
    def make_move(self, row, col, player):
        if self.board[row][col] == " ":
            self.board[row][col] = player
            return True
        return False

    def check_winner(self, player):
        # Checa linhas, colunas e diagonais
        for row in range(3):
            if all([self.board[row][col] == player for col in range(3)]):
                return True

        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                return True

        if all([self.board[i][i] == player for i in range(3)]) or all([self.board[i][2 - i] == player for i in range(3)]):
            return True

        return False

    def is_over(self):
        return all([self.board[row][col] != " " for row in range(3) for col in range(3)])
