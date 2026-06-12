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

    while True:
        print("\n===== ALBUM DE FIGURINHAS DA COPA =====")
        print("1  - Inserir figurinha")
        print("2  - Remover figurinha")
        print("3  - Consultar figurinha (por numero)")
        print("4  - Ver album completo")
        print("5  - Ver porcentagem concluida")
        print("6  - Ver repetidas (lista e quantidade)")
        print("7  - Buscar por jogador")
        print("8  - Buscar por selecao")
        print("9  - Trocar com o amigo")
        print("10 - Adicionar figurinha ao amigo (para testar a troca)")
        print("11 - Ver historico de trocas")
        print("12 - Salvar em arquivo")
        print("13 - Carregar de arquivo")
        print("0  - Sair")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            inserir_figurinha(meu_album)

        elif opcao == "2":
            id = ler_inteiro("Numero a remover: ")
            if meu_album.remover(id):
                print("Figurinha removida.")
            else:
                print("Figurinha nao encontrada.")

        elif opcao == "3":
            id = ler_inteiro("Numero a consultar: ")
            fig = meu_album.buscar(id)
            print(fig if fig is not None else "Nao encontrada.")

        elif opcao == "4":
            print("--- Seu album ---")
            meu_album.mostrar_album()

        elif opcao == "5":
            print(f"Concluido: {meu_album.porcentagem():.1f}% "
                  f"({meu_album.quantidade()}/{meu_album.total_figurinhas})")

        elif opcao == "6":
            print(f"Repetidas ({meu_album.contar_repetidas()}):")
            meu_album.mostrar_repetidas()

        elif opcao == "7":
            nome = input("Nome do jogador: ").strip()
            meu_album.buscar_por_jogador(nome)

        elif opcao == "8":
            pais = ler_selecao("Selecao: ")
            meu_album.buscar_por_selecao(pais)

        elif opcao == "9":
            efetuar_troca(meu_album, amigo_album, historico)

        elif opcao == "10":
            print("Adicionando figurinha ao album do amigo:")
            inserir_figurinha(amigo_album)

        elif opcao == "11":
            print("--- Historico de trocas ---")
            historico.listar()

        elif opcao == "12":
            nome_arq = input("Nome do arquivo (ex.: album.txt): ").strip()
            salvar_txt(meu_album, nome_arq)
            print("Album salvo!")

        elif opcao == "13":
            nome_arq = input("Nome do arquivo (ex.: album.txt): ").strip()
            try:
                meu_album = carregar_txt(nome_arq)
                print("Album carregado!")
            except FileNotFoundError:
                print("Arquivo nao encontrado.")

        elif opcao == "0":
            print("Ate mais!")
            break

        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()