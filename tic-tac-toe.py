import random

board = ['-' for _ in range(9)]

def print_board():
    print(' {} | {} | {}'.format(board[0], board[1], board[2]))
    print("------------")
    print(' {} | {} | {}'.format(board[3], board[4], board[5]))
    print("------------")
    print(' {} | {} | {}'.format(board[6], board[7], board[8]))

def check_win_draw():
    if board[0] == board[1] == board[2] and board[0] != '-' or \
        board[3] == board[4] == board[5] and board[3] != '-' or \
        board[6] == board[7] == board[8] and board[6] != '-' or \
        board[0] == board[3] == board[6] and board[0] != '-' or \
        board[1] == board[4] == board[7] and board[1] != '-' or \
        board[2] == board[5] == board[8] and board[2] != '-' or \
        board[0] == board[4] == board[8] and board[0] != '-' or \
        board[2] == board[4] == board[6] and board[2] != '-':
        return 'win'
    
    elif '-' not in board:
        return 'draw'
    
def take_input(turn):
    position = int(input('Enter the position(1 -9) : '))

    while position not in range(1, 10):
        print('Invalid position...')
        position = int(input('Enter the position(1 -9) : '))

    while board[position - 1] != '-':
        print('selected position is not empty...')
        position = int(input('Enter the position(1 -9) : '))

    board[position - 1] = turn
        

if __name__ == "__main__":
    print_board()
    gameOver = False
    player = 'X'

    while not gameOver:
        print(f'\n{player}\'s turn')
        take_input(player)
        print_board()
        
        res = check_win_draw()

        if res == 'win':
            print(f'{player} won the game')
            exit()

        elif res == 'draw':
            print('match draw')
            exit()

        if player == 'X':
            player = 'O'

        else:
            player = 'X'