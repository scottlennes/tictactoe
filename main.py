# Tic Tac Toe AI

# import numpy as np

# theBoard = [' '] * 9 

def printBoard(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('--+--+--')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('--+--+--')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def checkWin(board):
    return (board[0] == board[1] == board[2] != 0 or
        board[3] == board[4] == board[5] != 0 or
        board[6] == board[7] == board[8] != 0 or
        board[0] == board[4] == board[8] != 0 or
        board[2] == board[4] == board[6] != 0 or
        board[0] == board[3] == board[6] != 0 or
        board[1] == board[4] == board[7] != 0 or
        board[2] == board[5] == board[8] != 0)

def scottAI(board):
    
    # Convert open spaces to 0, my spaces to 1, and opp. spaces to -1
    #for i in range(9):
    #    if board[i] == ' ':
    #        board[i] = 0
    #    else:
    #        if board[i] == turn:
    #            board[i] = 1
    #        else:
    #            board[i] = -1

    # Choose move with highest minimax score
    scores = [8]*9

    for i in range(9):
        if board[i] == 0:
            board[i] = 1
            scores[i] = -minimax([-j for j in board])
            board[i] = 0
        else:
            scores[i] = 900
        print(board)
    return scores

    

def minimax(board): # Given a board, returns a score for the player based on how good it is

    # First, see if any moves will result in a win for the player. If so, return score of 1
    for i in range(9):
        if board[i] == 0:
            board[i] = 1
            if checkWin(board) == True:
                return 1
    
    # Next, find the minimax score for each move
    
    score = -2

    for i in range(9):
        if board[i] == 0:
            board[i] = 1
            if -minimax([-j for j in board]) > score:
                score = -minimax([-j for j in board])
            board[i] = 0

    return score

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
            move = scottAI(turn,theBoard)
    
        # Add move to board, check for invalid move
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("Invalid move was played. Game over!")
            break
        
        # Check for win
        if count >= 5:
            if checkWin(theBoard) == True:
                printBoard(theBoard)
                print("Game over. " & turn & " has won.")
                break

        # Check for tie
        if count == 9:
            printBoard(theBoard)
            print("Game over. It's a tie.")
            break

        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        

if __name__ == "__main__":
#    game()
    testBoard = [-1,0,-1,1,1,0,-1,-1,0]
    print(scottAI(testBoard[:]))
