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
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    def enqueue(self, item):
        novo = NodoFila(item)
        if self.esta_vazia():
            self.inicio = novo
        else:
            self.fim.proximo = novo
        self.fim = novo
        self.tamanho += 1

    def dequeue(self):
        if self.esta_vazia():
            return None
        item = self.inicio.item
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self.tamanho -= 1
        return item

    def mostrar(self):
        if self.esta_vazia():
            print("  (vazia)")
            return
        atual = self.inicio
        while atual is not None:
            print(" -", atual.item)
            atual = atual.proximo


class Historico(Fila):
    def registrar(self, descricao):
        self.enqueue(descricao)


class Album:
    def __init__(self, dono, total):
        self.dono = dono
        self.total = total
        self.cabeca = None
        self.tamanho = 0
        self.repetidas = Fila()

    def buscar(self, id):
        atual = self.cabeca
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
        novo.proximo = self.cabeca
        self.cabeca = novo
        self.tamanho += 1
        return "adicionada"

    def remover(self, id):
        atual = self.cabeca
        anterior = None
        while atual is not None:
            if atual.figurinha.id == id:
                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.tamanho -= 1
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def mostrar(self):
        if self.cabeca is None:
            print("  (album vazio)")
            return
        atual = self.cabeca
        while atual is not None:
            print(" ", atual.figurinha)
            atual = atual.proximo

    def porcentagem(self):
        if self.total == 0:
            return 0.0
        return (self.tamanho / self.total) * 100

    def mostrar_repetidas(self):
        self.repetidas.mostrar()

    def contar_repetidas(self):
        return self.repetidas.tamanho

    def buscar_por_jogador(self, nome):
        achou = False
        atual = self.cabeca
        while atual is not None:
            if nome.lower() in atual.figurinha.nome.lower():
                print(" ", atual.figurinha)
                achou = True
            atual = atual.proximo
        if not achou:
            print("  (nenhum jogador encontrado)")

    def buscar_por_selecao(self, pais):
        achou = False
        atual = self.cabeca
        while atual is not None:
            if atual.figurinha.pais.upper() == pais.upper():
                print(" ", atual.figurinha)
                achou = True
            atual = atual.proximo
        if not achou:
            print("  (nenhuma figurinha dessa selecao)")


def efetuar_troca(album_a, album_b, historico):
    if album_a.repetidas.esta_vazia() or album_b.repetidas.esta_vazia():
        print("Troca nao realizada: os dois precisam ter repetidas.")
        return False

    fig_a = album_a.repetidas.dequeue()
    fig_b = album_b.repetidas.dequeue()

    album_b.adicionar(fig_a)
    album_a.adicionar(fig_b)

    descricao = f"{album_a.dono} deu {fig_a.nome} e recebeu {fig_b.nome} de {album_b.dono}"
    historico.registrar(descricao)
    print("Troca realizada:", descricao)
    return True


def salvar_txt(album, nome_arquivo):
    arq = open(nome_arquivo, "w", encoding="utf-8")
    arq.write(f"{album.dono};{album.total}\n")

    atual = album.cabeca
    while atual is not None:
        f = atual.figurinha
        arq.write(f"A;{f.id};{f.nome};{f.pais};{f.posicao};{f.raridade}\n")
        atual = atual.proximo

    atual = album.repetidas.inicio
    while atual is not None:
        f = atual.item
        arq.write(f"R;{f.id};{f.nome};{f.pais};{f.posicao};{f.raridade}\n")
        atual = atual.proximo

    arq.close()


def carregar_txt(nome_arquivo):
    arq = open(nome_arquivo, "r", encoding="utf-8")

    cabecalho = arq.readline().strip().split(";")
    dono = cabecalho[0]
    total = int(cabecalho[1])
    album = Album(dono, total)

    for linha in arq:
        partes = linha.strip().split(";")
        if len(partes) != 6:
            continue
        tipo = partes[0]
        fig = Figurinha(int(partes[1]), partes[2], partes[3], partes[4], partes[5])
        if tipo == "A":
            album.adicionar(fig)
        else:
            album.repetidas.enqueue(fig)

    arq.close()
    return album
