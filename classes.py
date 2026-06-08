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

    def listar(self):
        if self.esta_vazia():
            print(" (nenhuma troca registrada)")
            return
        atual = self._inicio
        while atual is not None:
            print(" -", atual.item)
            atual = atual.proximo

class Album:

    def __init__(self, dono, total_figurinhas):
        self.dono = dono
        self._cabeca = None
        self._tamanho = 0
        self.total_figurinhas = total_figurinhas
        self.repetidas = Fila()

    def quantidade(self):
        return self._tamanho

    def buscar(self, id):
        atual = self._cabeca
        while atual is not None:
            if atual.figurinha.id == id:
                return atual.figurinha
            atual = atual.proximo
        return None

    def adicionar(self, figurinha):
        if self.buscar(figurinha.id) is not None:
            self.repetidas.enqueue(figurinha)
            return "repetida"
        novo = NodoLista(figurinha)
        novo.proximo = self._cabeca
        self._cabeca = novo
        self._tamanho += 1
        return "adicionada"

    def remover(self, id):
        atual = self._cabeca
        anterior = None
        while atual is not None:
            if atual.figurinha.id == id:
                if anterior is None:
                    self._cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self._tamanho -= 1
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def mostrar_album(self):
        if self._cabeca is None:
            print(" (album vazio)")
            return
        atual = self._cabeca
        while atual is not None:
            print(" ", atual.figurinha)
            atual = atual.proximo

    def porcentagem(self):
        if self.total_figurinhas == 0:
            return 0.0
        return (self._tamanho / self.total_figurinhas) * 100

    def mostrar_repetidas(self):
        if self.repetidas.esta_vazia():
            print(" (nenhuma repetida)")
            return
        atual = self.repetidas._inicio
        while atual is not None:
            print(" ", atual.item)
            atual = atual.proximo