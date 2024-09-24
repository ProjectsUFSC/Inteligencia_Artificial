# Algoritmo A* para resolver o quebra-cabeça de 8 peças
# Autor: Augusto Daleffe
# Data: 17/09/2024
# Disciplina: Inteligência Artificial - UFSC

import numpy as np

initial_state = np.array([
    [1, 2, 4], 
    [7, 5, 3], 
    [8, 0, 6]
    ])

final_state = np.array([
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 0]
    ])

def h(state):
    return np.sum(state != final_state) - 1  # -1 para desconsiderar o zero

def g(moves):
    return moves

def f(state, moves):
    return g(moves) + h(state)

def expand(state):
    n = state.shape[0]  # Coleta o número de linhas
    i, j = np.where(state == 0)  # Coleta a posição do zero como tupla
    i, j = i[0], j[0]  # Coleta o primeiro e único elemento da tupla
    states = []
    if i > 0: # Movimento para cima
        new_state = state.copy()
        new_state[i, j], new_state[i - 1, j] = new_state[i - 1, j], new_state[i, j]
        states.append(new_state)
    if i < n - 1: # Movimento para baixo
        new_state = state.copy()
        new_state[i, j], new_state[i + 1, j] = new_state[i + 1, j], new_state[i, j]
        states.append(new_state)
    if j > 0: # Movimento para a esquerda
        new_state = state.copy()
        new_state[i, j], new_state[i, j - 1] = new_state[i, j - 1], new_state[i, j]
        states.append(new_state)
    if j < n - 1: # Movimento para a direita
        new_state = state.copy()
        new_state[i, j], new_state[i, j + 1] = new_state[i, j + 1], new_state[i, j]
        states.append(new_state)
    return states

def A_star(initial_state):
    openeds = [(f(initial_state, 0), initial_state, 0, [])]  # (cost, state, moves, path)
    closeds = set()
    steps = 0
    while openeds:
        openeds = sorted(openeds, key=lambda x: x[0]) 
        cost, state, moves, path = openeds.pop(0) 
        if np.array_equal(state, final_state): 
            return path + [state], steps
        
        closeds.add(tuple(state.ravel()))
        steps += 1
        for new_state in expand(state):
            if tuple(new_state.ravel()) not in closeds:
                openeds.append((f(new_state, moves + 1), new_state, moves + 1, path + [state])) 
    return None

def is_solvable(state):
    state = state.ravel()
    state = [x for x in state if x != 0]
    inversions = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] > state[j]:
                inversions += 1
    return inversions % 2 == 0

if __name__ == "__main__":

    if is_solvable(initial_state):
        path, comparisons = A_star(initial_state)
        if path:
            print("\nCaminho para a solução:\n")
            for step in path:
                print(step)
                print()
            print(f"\nO estado final foi alcançado em {len(path) - 1} movimentos.")
            print(f"\nNúmero total de comparações: {comparisons}\n")
        else:
            raise ValueError("O estado final não foi alcançado")
    else:
        raise ValueError("O estado inicial não é solucionável")
