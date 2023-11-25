board = {1:'O', 2:'O', 3:'X',
         4:'X', 5:'-', 6:'O',
         7:'-', 8:'-', 9:'X'}


print("Use 'X'(for X player),'O'(for O player) and '-'(for empty slot)")
print("Enter the game state : ")
i = 1

for _ in range(3):
    row = list(map(str, input().split(" ")))
    
    for j in row:
        board[i] = j
        i = i + 1

def print_board():
    print(" {} | {} | {} ".format(board[1], board[2], board[3]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[4], board[5], board[6]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[7], board[8], board[9]))

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
        if board[key] == '-':
            return False
        
    return True

def minimax(board, isMaximum):
    if isPlayerWon('X'):
        return 100
    
    if isPlayerWon('O'):
        return -100
    
    if checkDraw():
        return 0
    
    if(isMaximum):
        bestScore = -1000
        for key in board.keys():
            if board[key] == '-':
                board[key] = 'O'
                score = minimax(board, False)
                board[key] = "-"
                bestScore = max(score, bestScore)

        return bestScore
    
    else:
        bestScore = 1000
        for key in board.keys():
            if board[key] == '-':
                board[key] = 'X'
                score = minimax(board, True)
                board[key] = "-"
                bestScore = min(score, bestScore)

        return bestScore
    
def bestMove(player):
    move = 0
    bestScore = -100

    for key in board.keys():
        if board[key] == "-":
            board[key] = player
            score = minimax(board, (player != 'X'))
            board[key] = "-"
            
            if(score > bestScore):
                bestScore = score
                move = key

    return move

if __name__ == '__main__' :
    print("\nGiven State : ")
    print_board()

    for key in board.keys():
        if board[key] != 'X' and board[key] != 'O' and board[key] != '-':
            print("\nInvalid State\nPlease use only X,O and - to represent state")
            exit()

    if isPlayerWon('X'):
        print("Player X already won the game")
        exit()
    
    if isPlayerWon('O'):
        print("Player O already won the game")
        exit()

    if checkDraw():
        print("It is draw")
        exit()

    player = input("\nEnter for which player you want best move('X' or 'O') :  ")
    while player not in ['X', 'O']:
        print('Please enter "X" or "O" ')
        player = input("\nEnter for which player you want best move('X' or 'O') :  ")

    print(f"\nThe best move for {player} in given sate is : ", bestMove(player))
