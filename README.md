# Album de Figurinhas da Copa

Terceiro projeto de **Estrutura de Dados** — FATEC Rio Claro.

Sistema de album de figurinhas implementado com **lista encadeada** e **fila FIFO** proprias, sem usar `list` ou `deque`.

## Como executar

```bash
python menu.py
```

## Arquivos

- `classes.py` — todas as classes (`Figurinha`, `NodoLista`, `NodoFila`, `Fila`, `Historico`, `Album`) e as funcoes de troca e persistencia.
- `menu.py` — menu interativo no terminal.

## Estruturas usadas

| Estrutura | Onde |
|-----------|------|
| Lista encadeada | figurinhas do album |
| Fila FIFO | repetidas e historico de trocas |

## Funcionalidades

- Inserir, remover e consultar figurinhas
- Ver album completo e porcentagem concluida
- Armazenar, listar e contar repetidas
- Buscar por numero, jogador ou selecao
- Trocar figurinhas entre dois albuns (usa as repetidas)
- Salvar e carregar album em arquivo TXT
