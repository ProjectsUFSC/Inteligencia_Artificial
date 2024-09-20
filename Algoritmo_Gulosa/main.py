import numpy as np


class Cidade:
    nome_cidade = None
    cidades_vizinhas = None  # Cidades vizinhas [cidade, distancia]

    def __init__(self, nome_cidade):
        self.nome_cidade = nome_cidade
        self.cidades_vizinhas = []

    def add_cidade_vizinha(self, cidade, distancia):
        self.cidades_vizinhas.append([cidade, distancia])

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

    def get_cidade(self, nome_cidade):
        # Corrigido: renomeamos a variável de iteração para evitar conflitos
        for c in self.cidades:
            if c.nome_cidade == nome_cidade:
                return c
        return None

    def get_vizinhos(self, nome_cidade):
        cidade = self.get_cidade(nome_cidade)
        if cidade:
            return cidade.cidades_vizinhas
        return None


def expandir_todas_rotas(mapa, cidade_atual, cidade_destino, rota_atual=None, rotas_possiveis=None):
    if rota_atual is None:
        rota_atual = []
    if rotas_possiveis is None:
        rotas_possiveis = []

    # Adicionar a cidade atual na rota
    rota_atual.append(cidade_atual.nome_cidade)

    # Se a cidade atual for o destino, a rota está completa
    if cidade_atual.nome_cidade == cidade_destino.nome_cidade:
        rotas_possiveis.append(list(rota_atual))  # Armazenar a rota completa
    else:
        # Explorar todos os vizinhos
        for vizinho, _ in cidade_atual.cidades_vizinhas:
            proxima_cidade = mapa.get_cidade(vizinho)
            if proxima_cidade and vizinho not in rota_atual:  # Evitar ciclos
                expandir_todas_rotas(mapa, proxima_cidade, cidade_destino, rota_atual, rotas_possiveis)

    # Backtrack: remover a cidade atual para explorar outras possibilidades
    rota_atual.pop()

    return rotas_possiveis

def gulosa(mapa, cidade_inicial, cidade_final):

    cidades_vizitadas = []
    cidades_vizitadas.append(cidade_inicial)

    while cidades_vizitadas[-1] != cidade_final:
        cidade_atual = cidades_vizitadas[-1]
       
        rotas = expandir_todas_rotas(mapa, cidade_atual, cidade_final)
        rotas = sorted(rotas, key=lambda x: x[2])
        cidade_mais_proxima = rotas[0][1]
        cidades_vizitadas.append(cidade_mais_proxima)
        print(cidades_vizitadas)
        print(rotas)
        print("\n\n")

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

# Adicionando Vizinhos de A
cidadeA.add_cidade_vizinha("B", 30)
cidadeA.add_cidade_vizinha("C", 20)
cidadeA.add_cidade_vizinha("D", 20)

# Adicionando Vizinhos de B
cidadeB.add_cidade_vizinha("E", 25)
cidadeB.add_cidade_vizinha("D", 10)

# Adicionando Vizinhos de C
cidadeC.add_cidade_vizinha("F", 15)
cidadeC.add_cidade_vizinha("D", 10)

# Adicionando Vizinhos de D
cidadeD.add_cidade_vizinha("F", 20)
cidadeD.add_cidade_vizinha("G", 25)

# Adicionando Vizinhos de E
cidadeE.add_cidade_vizinha("G", 10)
cidadeE.add_cidade_vizinha("F", 5)

# Adicionando Vizinhos de F
cidadeF.add_cidade_vizinha("G", 5)
cidadeF.add_cidade_vizinha("B", 15)

# Adicionando as cidades ao mapa
mapa.add_cidade(cidadeA)
mapa.add_cidade(cidadeB)
mapa.add_cidade(cidadeC)
mapa.add_cidade(cidadeD)
mapa.add_cidade(cidadeE)
mapa.add_cidade(cidadeF)
mapa.add_cidade(cidadeG)

rotas = expandir_todas_rotas(mapa, cidadeA, cidadeG)

print("Rotas possíveis de A para G:")
for rota in rotas:
    print(" -> ".join(rota))

print("\n\n*************************")

rota_gulosa = gulosa(mapa, cidadeA, cidadeG)
print("\nRota gulosa de A para G:")
print(" -> ".join(rota_gulosa))
