board = {1:' ', 2:' ', 3:' ',
         4:' ', 5:' ', 6:' ',
         7:' ', 8:' ', 9:' '}

human = 'X'
bot = 'O'

def printBoard():
    print(' {} | {} | {} '.format(board[1], board[2], board[3]))
    print('---+---+---')
    print(' {} | {} | {} '.format(board[4], board[5], board[6]))
    print('---+---+---')
    print(' {} | {} | {} '.format(board[7], board[8], board[9]))
    print('\n')

def checkWin():
    if board[1] == board[2] and board[2] == board[3] and board[3] != ' ':
        return True
    
    if board[4] == board[5] and board[5] == board[6] and board[6] != ' ':
        return True
    
    if board[7] == board[8] and board[8] == board[9] and board[9] != ' ':
        return True
    
    if board[1] == board[4] and board[4] == board[7] and board[7] != ' ':
        return True
    
    if board[5] == board[2] and board[2] == board[8] and board[8] != ' ':
        return True
    
    if board[6] == board[9] and board[9] == board[3] and board[3] != ' ':
        return True
    
    if board[1] == board[5] and board[5] == board[9] and board[9] != ' ':
        return True
    
    if board[7] == board[5] and board[5] == board[3] and board[3] != ' ':
        return True
    
    else:
        return False
    
def isPlayerWon(player):
    if board[1] == board[2] and board[2] == board[3] and board[3] == player:
        return True
    
    if board[4] == board[5] and board[5] == board[6] and board[6] == player:
        return True
    
    if board[7] == board[8] and board[8] == board[9] and board[9] == player:
        return True
    
    if board[1] == board[4] and board[4] == board[7] and board[7] == player:
        return True
    
    if board[5] == board[2] and board[2] == board[8] and board[8] == player:
        return True
    
    if board[6] == board[9] and board[9] == board[3] and board[3] == player:
        return True
    
    if board[1] == board[5] and board[5] == board[9] and board[9] == player:
        return True
    
    if board[7] == board[5] and board[5] == board[3] and board[3] == player:
        return True
    
    else:
        return False

def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
        
    return True

def insertToken(position, player):
    board[position] = player
    printBoard()

    if checkWin():
        print(f'{player} won the match')
        exit()

    elif checkDraw():
        print(f'Match is draw....')
        exit()

def humanMove():
    position = int(input('Enter position [1-9] : '))

    if position not in range(1, 10) and board[position] != ' ':
        print('Invalid position')
        humanMove()

    else:
        insertToken(position, human)

def botMove():
    position = bestMove()
    insertToken(position, bot)

def bestMove():
    move = 0
    bestScore = -1000

    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot
            score = minimax(board, False)
            board[key] = ' '

            if score > bestScore:
                bestScore = score
                move = key

    return move

def minimax(board, isMaximizing):
    if isPlayerWon(human):
        return -100
    
    elif isPlayerWon(bot):
        return 100
    
    elif checkDraw():
        return 0
    
    if isMaximizing:
        bestScore = -1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = bot
                score = minimax(board, False)
                board[key] = ' '

                bestScore = max(bestScore, score)

        return bestScore
    
    else:
        bestScore = 1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = human
                score = minimax(board, True)
                board[key] = ' '

                bestScore = min(bestScore, score)

        return bestScore

if __name__ == '__main__':
    printBoard()

    while True:
        humanMove()
        botMove()