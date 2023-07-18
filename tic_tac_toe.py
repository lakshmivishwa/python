import random
board=["--","--","--",
      "--","--","--",
      "--","--","--"]
currentPlayer=" X "
winner=None
gameRunning=True

#print board
def printBoard(board):
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("--------")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("--------")
    print(board[6]+"|"+board[7]+"|"+board[8])

#take player input
def playerInput(board):
    inp= int(input("enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1]== "--":
        board[inp-1]=currentPlayer
    else:
        print("Oops player is already on the spot")
        
#check for win or tie
def checkHorizontal(board):
    global winner
    if board[0]==board[1]==board[2] and board[0]!="--":
        winner= board[0]
        return True
    elif board[3]==board[4]==board[5]and board[3]!="--":
        winner=board[3]
        return True
    
    elif board[6]==board[7]==board[8] and board[6]!="--":
        winner=board[6]
        return True

def row(board):
    global winner
    if board[0]==board[3]==board[6]:
        winner= board[0]
        return True
    elif board[1]==board[4]==board[7]:
        winner=board[1]
        return True
    
    elif board[2]==board[5]==board[8]:
        winner=board[2]
        return True
    
def checkDiag(board):
        global winner
        if board[0]==board[4]==board[8]:
         winner= board[0]
         return True
        elif board[2]==board[4]==board[6]:
         winner= board[2]
         return True
        
def checkTie(board):   
        if "--" not in board:
          printBoard(board)  
          print("it is tie") 
          gameRunning(False)

def checkWin():  
        if checkHorizontal(board) or checkDiag(board) or checkTie(board) :
            print(f"the winner is {winner}")
            

#switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer=="X":
        currentPlayer="O"
    else:
        currentPlayer="X"    

def computer(board):
    while currentPlayer=="O":
        position= random.randint(0,8)
        if board[position]=="--":
            board[position]=="O"
            switchPlayer()

#check again for win or tie

while gameRunning:
     printBoard(board)
     playerInput(board)
     checkWin()
     checkTie(board)
     switchPlayer()
     computer(board)
     checkWin()
     checkTie(board)