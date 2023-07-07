import math


class Cidade:
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y


def calcular_distancia(cidade1, cidade2):
    return math.sqrt((cidade1.x - cidade2.x)**2 + (cidade1.y - cidade2.y)**2)


def busca_gulosa(origem, destinos):
    caminho = [origem]
    distancia_total = 0

    while destinos:
        melhor_cidade = None
        melhor_distancia = float('inf')

        for cidade in destinos:
            distancia = calcular_distancia(caminho[-1], cidade)
            if distancia < melhor_distancia:
                melhor_cidade = cidade
                melhor_distancia = distancia

        caminho.append(melhor_cidade)
        distancia_total += melhor_distancia
        destinos.remove(melhor_cidade)

    return caminho, distancia_total


# Criação das cidades
cidade_A = Cidade("A", 0, 0)
cidade_B = Cidade("B", -2, -9)
cidade_C = Cidade("C", -8, -14)
cidade_D = Cidade("D", -13, -22)
cidade_E = Cidade("E", -7, -21)
cidade_F = Cidade("F", -2, -19)
cidade_G = Cidade("G", 1, -17)
cidade_H = Cidade("H", -4, -17)
cidade_I = Cidade("I", 9, -8)
cidade_J = Cidade("J", 15, -8)
cidade_K = Cidade("K", 10, -19)
cidade_L = Cidade("L", 33, -23)
cidade_M = Cidade("M", 41, -21)

# Definição das conexões entre as cidades
cidade_A.conexoes = [cidade_B]
cidade_B.conexoes = [cidade_A, cidade_C]
cidade_C.conexoes = [cidade_B, cidade_D, cidade_E, cidade_H]
cidade_D.conexoes = [cidade_C, cidade_E]
cidade_E.conexoes = [cidade_D, cidade_H, cidade_F]
cidade_F.conexoes = [cidade_E, cidade_H, cidade_G, cidade_K]
cidade_G.conexoes = [cidade_H, cidade_F]
cidade_H.conexoes = [cidade_C, cidade_E, cidade_F, cidade_G]
cidade_I.conexoes = [cidade_A, cidade_J]
cidade_J.conexoes = [cidade_I, cidade_L, cidade_M, cidade_K]
cidade_K.conexoes = [cidade_D, cidade_F, cidade_J, cidade_L]
cidade_L.conexoes = [cidade_K, cidade_M]
cidade_M.conexoes = [cidade_L]

# Ponto de partida
origem = cidade_A

# Lista de destinos
destinos = [cidade_B, cidade_C, cidade_D, cidade_E, cidade_F,
            cidade_G, cidade_H, cidade_I, cidade_J, cidade_K, cidade_L, cidade_M]

# Execução da busca gulosa
caminho, distancia_total = busca_gulosa(origem, destinos)

# Exibição do resultado
print("Caminho percorrido:")
for cidade in caminho:
    print(cidade.nome)

print("Distância total percorrida:", distancia_total)
