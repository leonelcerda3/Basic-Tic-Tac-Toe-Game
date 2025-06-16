import random

currentPlayer = "X"
gameRunning = True      
winner = None
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " ",]

def printBoard(board):
    print(board[0]+ " | "+ board[1]+ " | "+board[2])
    print("--+---+--")
    print(board[3]+ " | "+ board[4]+ " | "+board[5])
    print("--+---+--")
    print(board[6]+ " | "+ board[7]+ " | "+board[8])

def clearBoard():
    print()
    printBoard(board)
    print()
    
    


def winConditions(board):
   global winner
    if board[0] == board[1] == board[2] and board[0] != " ":
       winner = board[1]
       return True 
    elif board[0] == board[3] == board[6] and board[0] != " ":
        winner = board[0]
        return True 
    elif board[0] == board[4] == board[8] and board[0] != " ":
        winner = board[4]
        return True 
    elif board[1] == board[4] == board[7] and board[1] != " ":
        rwinner = board[1]
        return True 
    elif board[3] == board[4] == board[5] and board[3] != " ":
        winner = board[3]
        return True 
    elif board[6] == board[7] == board[8] and board[6] != " ":
        winner = board[7]
        return True 
    elif board[2] == board[4] == board[6] and board[2] != " ":
        winner = board[6]
        return True 
    elif board[2] == board[5] == board[8] and board[2] != " ":
        winner = board[2]
        return True 
    
def checkWin():
    global gameRunning
    if winConditions(board):
        
        print(f"The winner of the game is {winner}. Congratulations!!")
        gameRunning = False

def checkTie():
    global gameRunning
    if " " not in board:
        
        print("It is a tie!")
        gameRunning = False
    



def moves(board):
    move =int(input("Please select a number 1-9: "))
    if move >= 1 and move <= 9 and board[move-1] == " ":
        board[move-1] = currentPlayer
    else:
        print("That square has already been selected. Please choose another: ")

def turns(board):
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else: 
        currentPlayer = "X"

print("Welcome to Tic Tac Toe!")

clearBoard()
while gameRunning:
    moves(board)
    printBoard(board)
    turns(board)
    checkWin()
    checkTie()

    
