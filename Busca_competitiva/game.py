class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
    
    def print_board(self):
        positions = [str(i) if self.board[i // 3][i % 3] == " " else self.board[i // 3][i % 3] for i in range(9)]
        for i in range(3):
            print(f"{positions[i * 3]} | {positions[i * 3 + 1]} | {positions[i * 3 + 2]}")
            if i < 2:
                print("--+---+--")

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
