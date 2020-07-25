# Tic Tac Toe AI

theBoard = [' '] * 9 

def printBoard(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('--+--+--')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('--+--+--')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def isWinner(board):
    return (board[0] == board[1] == board[2] != ' ' or
        board[3] == board[4] == board[5] != ' ' or
        board[6] == board[7] == board[8] != ' ' or
        board[0] == board[4] == board[8] != ' ' or
        board[2] == board[4] == board[6] != ' ' or
        board[0] == board[3] == board[6] != ' ' or
        board[1] == board[4] == board[7] != ' ' or
        board[2] == board[5] == board[8] != ' ')

def opp(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'

def scottAI(board, player):

    bestMove = -1
    bestScore = -2

    for i in range(9):
        if board[i] == ' ':
            dummyBoard = board[:]
            dummyBoard[i] = player
            if isWinner(dummyBoard):
                bestMove = i
                bestScore = 1
            else:
                if -minimax(dummyBoard, opp(player)) > bestScore:
                    bestMove = i
                    bestScore = -minimax(dummyBoard, opp(player))

    return bestMove

def minimax(board, player): # Given a board, returns 1, -1, or 0

    # Check if board is full; if so, return 0
    if len([i for i in board if i==' '])==0:
        return 0
    
    bestScore = -2

    for i in range(9):
        if board[i] == ' ':
            dummyBoard = board[:]
            dummyBoard[i] = player

            # First, check if any moves will result in a win for the player; if so, return score of 1
            if isWinner(dummyBoard) == True:
                bestScore = 1
            
            # Otherwise, find the minimax score of opponent
            else:
                if -minimax(dummyBoard, opp(player)) > bestScore:
                    bestScore = -minimax(dummyBoard, opp(player))
    
    return bestScore

def game():

    turn = 'X'
    count = 0

    print("Would you like to be X or O?")
    user = input()

    while True:

        if turn == user:
            printBoard(theBoard)
            print("It's your turn, " + turn + ". Move to which place?")
            move = int(input())
        else:
            move = scottAI(theBoard, turn)
    
        # Add move to board, check for invalid move
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("Invalid move was played. Try again!")
            continue
        
        # Check for win
        if count >= 5:
            if isWinner(theBoard):
                printBoard(theBoard)
                print("Game over. " + turn + " has won.")
                break

        # Check for tie
        if count == 9:
            printBoard(theBoard)
            print("Game over. It's a tie.")
            break

        turn = opp(turn)       

if __name__ == "__main__":
    game()