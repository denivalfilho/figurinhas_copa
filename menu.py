from classes import (
    Figurinha, Album, Historico, SELECOES_VALIDAS,
    efetuar_troca, salvar_txt, carregar_txt,
)

def ler_inteiro(mensagem):

    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor invalido! Digite um numero inteiro.")

def ler_selecao(mensagem):

    while True:
        codigo = input(mensagem).strip().upper()
        if codigo in SELECOES_VALIDAS:
            return codigo
        print("Selecao invalida! Use um destes codigos:")
        print(" ", ", ".join(SELECOES_VALIDAS))

def inserir_figurinha(album):

    id = ler_inteiro("Numero da figurinha: ")
    if id <= 0:
        print("Numero invalido! Deve ser positivo.")
        return
    nome = input("Nome do jogador: ").strip()
    if nome == "":
        print("O nome nao pode ser vazio.")
        return
    pais = ler_selecao("Selecao (ex.: BRA): ")
    posicao = input("Posicao: ").strip()
    raridade = input("Raridade (comum/rara/lendaria): ").strip()

    fig = Figurinha(id, nome, pais, posicao, raridade)
    resultado = album.adicionar(fig)
    if resultado == "repetida":
        print("Voce ja tinha essa! Foi para as repetidas.")
    else:
        print("Figurinha adicionada ao album!")

def main():

    meu_album = Album("Voce", total_figurinhas=20)     # mude o total se quiser
    amigo_album = Album("Amigo", total_figurinhas=20)
    historico = Historico()

