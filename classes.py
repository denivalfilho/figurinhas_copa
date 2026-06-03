SELECOES_VALIDAS = (
    "BRA", "ARG", "FRA", "ESP", "ALE", "ING",
    "POR", "ITA", "URU", "MEX", "EUA", "JAP",
    "HOL", "BEL", "CRO", "MAR",
)

class Figurinha:

    def __init__(self, id, nome, pais, posicao, raridade):
        self.id = id
        self.nome = nome
        self.pais = pais
        self.posicao = posicao
        self.raridade = raridade

    def __str__(self):
        return f"#{self.id} - {self.nome} ({self.pais}) | {self.posicao} | {self.raridade}"

class NodoLista:

    def __init__(self, figurinha):
        self.figurinha = figurinha
        self.proximo = None

class NodoFila:

    def __init__(self, item):
        self.item = item
        self.proximo = None