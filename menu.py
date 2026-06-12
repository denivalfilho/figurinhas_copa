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
