import random

class Individuo:
    def __init__(self, cidades):
        self.cidades = cidades
        self.rota = random.sample(cidades[1:], len(cidades) - 1)
        self.rota.insert(0, cidades[0])  # Garantindo que A está na primeira posição da rota
        self.rota.append(cidades[0])  # Garantindo que A está na última posição da rota
        self.distancia = self.calcular_distancia()

    def calcular_distancia(self):
        distancia_total = 0
        for i in range(len(self.rota) - 1):
            cidade_atual = self.rota[i]
            proxima_cidade = self.rota[i + 1]
            distancia_total += cidade_atual.calcular_distancia(proxima_cidade)
        return distancia_total

class Cidade:
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y

    def calcular_distancia(self, outra_cidade):
        distancia_x = abs(self.x - outra_cidade.x)
        distancia_y = abs(self.y - outra_cidade.y)
        return (distancia_x ** 2 + distancia_y ** 2) ** 0.5

class AlgoritmoGenetico:
    def __init__(self, cidades, tamanho_populacao, taxa_mutacao, numero_geracoes):
        self.cidades = cidades
        self.tamanho_populacao = tamanho_populacao
        self.taxa_mutacao = taxa_mutacao
        self.numero_geracoes = numero_geracoes

    def executar(self):
        populacao = self.inicializar_populacao()
        for geracao in range(self.numero_geracoes):
            populacao = self.selecionar_populacao(populacao)
            populacao = self.reproduzir_populacao(populacao)
            self.mutar_populacao(populacao)

        melhor_individuo = self.obter_melhor_individuo(populacao)
        return melhor_individuo

    def inicializar_populacao(self):
        return [Individuo(self.cidades) for _ in range(self.tamanho_populacao)]

    def selecionar_populacao(self, populacao):
        return sorted(populacao, key=lambda x: x.distancia)[:self.tamanho_populacao]

    def reproduzir_populacao(self, populacao):
        filhos = []
        for _ in range(self.tamanho_populacao):
            pai = random.choice(populacao)
            mae = random.choice(populacao)
            filho = self.reproduzir_individuos(pai, mae)
            filhos.append(filho)
        return filhos

    def reproduzir_individuos(self, pai, mae):
        ponto_corte = random.randint(0, len(pai.rota) - 2)  # Evitar corte em A no início e fim da rota
        rota_filho = pai.rota[:ponto_corte] + [cidade for cidade in mae.rota if cidade not in pai.rota[:ponto_corte]]
        return Individuo(self.cidades)

    def mutar_populacao(self, populacao):
        for individuo in populacao:
            if random.random() < self.taxa_mutacao:
                self.mutar_individuo(individuo)

    def mutar_individuo(self, individuo):
        indice_1, indice_2 = random.sample(range(1, len(individuo.rota) - 1), 2)  # Evitar mutação em A
        individuo.rota[indice_1], individuo.rota[indice_2] = individuo.rota[indice_2], individuo.rota[indice_1]
        individuo.distancia = individuo.calcular_distancia()

    def obter_melhor_individuo(self, populacao):
        return min(populacao, key=lambda x: x.distancia)


# Exemplo de uso
cidades = [
    Cidade("A", 0, 0),
    Cidade("B", -2, -9),
    Cidade("C", -8, -14),
    Cidade("D", -13, -22),
    Cidade("E", -7, -21),
    Cidade("F", -2, -19),
    Cidade("G", 1, -17),
    Cidade("H", -4, -17),
    Cidade("I", 9, -8),
    Cidade("J", 15, -8),
    Cidade("K", 10, -19),
    Cidade("L", 33, -23),
    Cidade("M", 41, -21)
]

algoritmo_genetico = AlgoritmoGenetico(cidades, tamanho_populacao=50, taxa_mutacao=0.1, numero_geracoes=100)
melhor_rota = algoritmo_genetico.executar()

print(f"Melhor rota encontrada: {', '.join([cidade.nome for cidade in melhor_rota.rota])}")
print(f"Distância total: {melhor_rota.distancia}")
