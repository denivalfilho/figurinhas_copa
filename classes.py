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

class Fila:

    def __init__(self):
        self._inicio = None 
        self._fim = None
        self._tamanho = 0

    def esta_vazia(self):
        return self._inicio is None

    def enqueue(self, item):
        novo = NodoFila(item)
        if self.esta_vazia():
            self._inicio = novo
            self._fim = novo
        else:
            self._fim.proximo = novo
            self._fim = novo
        self._tamanho += 1

    def dequeue(self):
        if self.esta_vazia():
            return None
        removido = self._inicio
        self._inicio = self._inicio.proximo
        if self._inicio is None:
            self._fim = None
        self._tamanho -= 1
        return removido.item

    def peek(self):
        if self.esta_vazia():
            return None
        return self._inicio.item

    def limpar(self):
        self._inicio = None
        self._fim = None
        self._tamanho = 0

    def tamanho(self):
        return self._tamanho

class Historico(Fila):

    def registrar(self, descricao):
        self.enqueue(descricao)