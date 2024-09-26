import random

def movimento_aleatorio(jogo):
    while True:
        posicao = random.randint(0, 8) 
        if jogo.tabuleiro[posicao] == " ":
            return posicao // 3, posicao % 3 

def minimax(jogo, jogador):
    if jogo.verificar_vencedor("O"):
        return 1  # Vencedor O
    elif jogo.verificar_vencedor("X"):
        return -1  # Vencedor X
    elif jogo.jogo_terminado():
        return 0  # Empate

    melhor_valor = -float('inf') if jogador == "O" else float('inf')

    for i in range(9):
        if jogo.tabuleiro[i] == " ":
            jogo.fazer_jogada(i, jogador)
            valor = minimax(jogo, "X" if jogador == "O" else "O")
            jogo.tabuleiro[i] = " "

            if jogador == "O":
                if valor > melhor_valor:
                    melhor_valor = valor
            else:
                if valor < melhor_valor:
                    melhor_valor = valor

    return melhor_valor

def movimento_minimax(jogo):
    melhor_valor = -float('inf')
    melhor_posicao = None

    for i in range(9):
        if jogo.tabuleiro[i] == " ":
            jogo.fazer_jogada(i, "O")
            valor = minimax(jogo, "X")
            jogo.tabuleiro[i] = " "
            if valor > melhor_valor:
                melhor_valor = valor
                melhor_posicao = i

    print(f"A IA jogou na posição {melhor_posicao} (Minimax)")
    return melhor_posicao // 3, melhor_posicao % 3

def alphabeta(jogo, profundidade, alpha, beta, jogador):
    if jogo.verificar_vencedor("O"):
        return 1  # Vencedor O
    elif jogo.verificar_vencedor("X"):
        return -1  # Vencedor X
    elif jogo.jogo_terminado():
        return 0  # Empate

    if jogador == "O":
        melhor_valor = -float('inf')
        for i in range(9):
            if jogo.tabuleiro[i] == " ":
                jogo.fazer_jogada(i, jogador)
                valor = alphabeta(jogo, profundidade + 1, alpha, beta, "X")
                jogo.tabuleiro[i] = " "
                melhor_valor = max(melhor_valor, valor)
                alpha = max(alpha, valor)
                if beta <= alpha:
                    break
        return melhor_valor
    else:
        melhor_valor = float('inf')
        for i in range(9):
            if jogo.tabuleiro[i] == " ":
                jogo.fazer_jogada(i, jogador)
                valor = alphabeta(jogo, profundidade + 1, alpha, beta, "O")
                jogo.tabuleiro[i] = " "
                melhor_valor = min(melhor_valor, valor)
                beta = min(beta, valor)
                if beta <= alpha:
                    break
        return melhor_valor

def movimento_alphabeta(jogo):
    melhor_valor = -float('inf')
    melhor_posicao = None

    for i in range(9):
        if jogo.tabuleiro[i] == " ":
            jogo.fazer_jogada(i, "O")
            valor = alphabeta(jogo, 0, -float('inf'), float('inf'), "X")
            jogo.tabuleiro[i] = " "
            if valor > melhor_valor:
                melhor_valor = valor
                melhor_posicao = i

    print(f"A IA jogou na posição {melhor_posicao} (Poda Alfa-Beta)")  # Impressão do movimento da IA
    return melhor_posicao // 3, melhor_posicao % 3
