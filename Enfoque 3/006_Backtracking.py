
def is_safe(board, row, col):
    # Comprobar la columna
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Comprobar la diagonal superior izquierda
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Comprobar la diagonal superior derecha
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row):
    if row >= len(board):
        return True
    
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1  # Colocar la reina
            
            if solve_n_queens(board, row + 1):
                return True
            
            board[row][col] = 0  # Retirar la reina (backtrack)

    return False

def print_board(board):
    for row in board:
        print(' '.join('Q' if x == 1 else '.' for x in row))

# Tamaño del tablero
n = 4
board = [[0] * n for _ in range(n)]

if solve_n_queens(board, 0):
    print("Solución encontrada:")
    print_board(board)
else:
    print("No hay solución.")
