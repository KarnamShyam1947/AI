print('NAME : KARNAM SHYAM\t\t\tREG. NO. : 21MIC7182\n')
n = int(input('Enter the number of queen : '))

board = [[0 for i in range(n)] for j in range(n)]

def print_board(board):
    for row in board:
        for position in row:
            if position == 1:
                print('Q', end =' ')
            
            else:
                print('-', end = ' ')

        print('')   

def check_row_column(board, row, col):
    for i in range(n):
        if board[row][i] == 1:
            return False
        
    for i in range(n):
        if board[i][col] == 1:
            return False
        
    return True

def check_diagonal(board, row, col):
    for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
        
    for i,j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False 
        
    for i,j in zip(range(row, 4), range(col, 4)):
        if board[i][j] == 1:
            return False
        
    for i,j in zip(range(row, 4), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nQueen(board, row):
    if row == n:
        return True
    
    for i in range(n):
        if check_row_column(board, row, i) and check_diagonal(board, row, i):
            board[row][i] = 1
            if(solve_nQueen(board, row+1)):
                return True
            
            board[row][i] = 0

    return False


solve_nQueen(board, 0)

print_board(board)
