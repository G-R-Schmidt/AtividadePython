def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * (len(tabuleiro) * 3 - 1))

def verificar_vencedor(tabuleiro, jogador):
    tamanho = len(tabuleiro)

    # Verificar linhas e colunas
    for i in range(tamanho):
        if all(tabuleiro[i][j] == jogador for j in range(tamanho)) or all(tabuleiro[j][i] == jogador for j in range(tamanho)):
            return True

    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(tamanho)) or all(tabuleiro[i][tamanho - 1 - i] == jogador for i in range(tamanho)):
        return True

    return False

def jogo_da_velha():
    tamanho = int(input("Digite o tamanho do tabuleiro (NxN): "))
    tabuleiro = [[" " for _ in range(tamanho)] for _ in range(tamanho)]
    jogador = "X"
    
    for _ in range(tamanho * tamanho):
        exibir_tabuleiro(tabuleiro)
        linha = int(input(f"Jogador {jogador}, escolha a linha (1-{tamanho}): ")) - 1
        coluna = int(input(f"Jogador {jogador}, escolha a coluna (1-{tamanho}): ")) - 1

        if 0 <= linha < tamanho and 0 <= coluna < tamanho and tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador
        else:
            print("Posição inválida. Tente novamente.")
            continue

        if verificar_vencedor(tabuleiro, jogador):
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador} venceu! Parabéns!")
            break

        jogador = "O" if jogador == "X" else "X"

    else:
        exibir_tabuleiro(tabuleiro)
        print("Empate! O jogo acabou sem vencedor.")

if __name__ == "__main__":
    jogo_da_velha()
