# Função para imprimir o tabuleiro
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 13)

# Função para verificar o estado do jogo
def check_winner(board, player):
    # Verifique linhas e colunas
    for i in range(4):
        if all(board[i][j] == player for j in range(4)) or all(board[j][i] == player for j in range(4)):
            return True

    # Verifique diagonais
    if all(board[i][i] == player for i in range(4)) or all(board[i][3 - i] == player for i in range(4)):
        return True

    return False

# Função principal
def main():
    board = [[" " for _ in range(4)] for _ in range(4)]
    player = "X"
    moves = 0

    while True:
        print_board(board)
        row = int(input(f"Jogador {player}, escolha a linha (1-4): ")) - 1
        col = int(input(f"Jogador {player}, escolha a coluna (1-4): ")) - 1

        if board[row][col] == " ":
            board[row][col] = player
            moves += 1
        else:
            print("Essa posição já está ocupada. Tente novamente.")
            continue

        if check_winner(board, player):
            print_board(board)
            print(f"Jogador {player} venceu! Parabéns!")
            break

        if moves == 16:
            print_board(board)
            print("Empate! O jogo acabou sem vencedor.")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    main()
