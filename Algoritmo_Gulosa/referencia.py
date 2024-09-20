# Algoritmo Gulosa para resolver o caminho mais curto em um mapa de cidades
# Autor: Augusto Daleffe
# Data: 20/09/2024
# Disciplina: Inteligência Artificial - UFSC


# O mesmo código do arquivo gulosa.py, porém agora nos usamos as cidades passadas por referência

import numpy as np

class Cidade:
    nome_cidade = None
    cidades_vizinhas = None  # Cidades vizinhas [cidade, distancia]

    def __init__(self, nome_cidade):
        self.nome_cidade = nome_cidade
        self.cidades_vizinhas = []

    def add_cidade_vizinha(self, cidade, distancia):
        if cidade not in [c[0] for c in self.cidades_vizinhas]:
            self.cidades_vizinhas.append([cidade, distancia])
        else:
            print(f"{cidade.nome_cidade} já é vizinho de {self.nome_cidade}")
            return
        if self not in [c[0] for c in cidade.cidades_vizinhas]:
            cidade.add_cidade_vizinha(self, distancia)

    def __name__(self):
        return self.nome_cidade

    def __str__(self):
        return f"Cidade: {self.nome_cidade}, Vizinhos: {self.cidades_vizinhas}"


class Mapa:
    cidades = None

    def __init__(self):
        self.cidades = []

    def add_cidade(self, cidade):
        self.cidades.append(cidade)

    def get_cidades(self):
        return self.cidades

    def get_vizinhos(self, cidade):
        for c in self.cidades:
            if c.nome_cidade == cidade.nome_cidade:
                return c.cidades_vizinhas


def expandir_todas_rotas(mapa, cidade_atual, cidade_destino, rota_atual=None, rotas_possiveis=None):
    if rota_atual is None:
        rota_atual = []
    if rotas_possiveis is None:
        rotas_possiveis = []

    rota_atual.append(cidade_atual)

    if cidade_atual.nome_cidade == cidade_destino.nome_cidade:
        rotas_possiveis.append(list(rota_atual)) 
    else:

        for vizinho, _ in cidade_atual.cidades_vizinhas:

            if vizinho.nome_cidade not in [c.nome_cidade for c in rota_atual]: 
                expandir_todas_rotas(mapa, vizinho, cidade_destino, rota_atual, rotas_possiveis)

    rota_atual.pop()
    return rotas_possiveis

def calcular_distancia_total(rota):
    distancia_total = 0
    for i in range(len(rota) - 1):  # Percorre de uma cidade até a penúltima
        cidade_atual = rota[i]
        cidade_proxima = rota[i + 1]

        for vizinho, distancia in cidade_atual.cidades_vizinhas:
            if vizinho.nome_cidade == cidade_proxima.nome_cidade:
                distancia_total += distancia
                break
    return distancia_total


def gulosa(mapa, cidade_inicial, cidade_final):

    cidades_vizitadas = []
    cidades_vizitadas.append(cidade_inicial)

    while cidades_vizitadas[-1] != cidade_final:
        cidade_atual = cidades_vizitadas[-1]
       
        rotas = expandir_todas_rotas(mapa, cidade_atual, cidade_final)
        rotas = sorted(rotas, key=calcular_distancia_total)
        cidade_mais_proxima = rotas[0][1]
        cidades_vizitadas.append(cidade_mais_proxima)

    return cidades_vizitadas


# Definindo o mapa
mapa = Mapa()

# Definindo as cidades
cidadeA = Cidade("A")
cidadeB = Cidade("B")
cidadeC = Cidade("C")
cidadeD = Cidade("D")
cidadeE = Cidade("E")
cidadeF = Cidade("F")
cidadeG = Cidade("G")

# MAPA QUE FUNCIONA ELE VAI PARA O MAIS CURTO
# Adicionando as cidades vizinhas A
cidadeA.add_cidade_vizinha(cidadeB, 10)
cidadeA.add_cidade_vizinha(cidadeC, 20)
cidadeA.add_cidade_vizinha(cidadeD, 20)

# Adicionando as cidades vizinhas B
cidadeB.add_cidade_vizinha(cidadeE, 20)
cidadeB.add_cidade_vizinha(cidadeD, 10)

# Adicionando as cidades vizinhas C
cidadeC.add_cidade_vizinha(cidadeF, 10)
cidadeC.add_cidade_vizinha(cidadeD, 5)

# Adicionando as cidades vizinhas D
cidadeD.add_cidade_vizinha(cidadeE, 10)
cidadeD.add_cidade_vizinha(cidadeF, 20)
cidadeD.add_cidade_vizinha(cidadeG, 20)

# Adicionando as cidades vizinhas E
cidadeE.add_cidade_vizinha(cidadeG, 10)
cidadeE.add_cidade_vizinha(cidadeF, 5)

# Adicionando as cidades vizinhas F
cidadeF.add_cidade_vizinha(cidadeG, 5)


# Adicionando as cidades ao mapa
mapa.add_cidade(cidadeA)
mapa.add_cidade(cidadeB)
mapa.add_cidade(cidadeC)
mapa.add_cidade(cidadeD)
mapa.add_cidade(cidadeE)
mapa.add_cidade(cidadeF)
mapa.add_cidade(cidadeG)

rotas = expandir_todas_rotas(mapa, cidadeA, cidadeG)

print("\n\nRotas possíveis de A para G:")
for rota in rotas:
    print(" -> ".join(rota.nome_cidade for rota in rota))


rota_gulosa = gulosa(mapa, cidadeA, cidadeG)
print("\nRota escolhida pelo gulosa de A para G:")
print(" -> ".join([cidade.nome_cidade for cidade in rota_gulosa]))
