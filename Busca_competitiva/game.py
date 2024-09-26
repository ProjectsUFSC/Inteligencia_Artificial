class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [" " for _ in range(9)]
    
    def mostrar_tabuleiro(self):
        print(f"{self.tabuleiro[0]} | {self.tabuleiro[1]} | {self.tabuleiro[2]}")
        print("--+---+--")
        print(f"{self.tabuleiro[3]} | {self.tabuleiro[4]} | {self.tabuleiro[5]}")
        print("--+---+--")
        print(f"{self.tabuleiro[6]} | {self.tabuleiro[7]} | {self.tabuleiro[8]}")

    def fazer_jogada(self, posicao, jogador):
        if self.tabuleiro[posicao] == " ":
            self.tabuleiro[posicao] = jogador
            return True
        return False

    def verificar_vencedor(self, jogador):
        vitoria = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
            [0, 4, 8], [2, 4, 6]              # Diagonais
        ]
        return any(all(self.tabuleiro[pos] == jogador for pos in linha) for linha in vitoria)

    def jogo_terminado(self):
        return all(campo != " " for campo in self.tabuleiro)
