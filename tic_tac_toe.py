
def  printBoard(xState,zState):
  print(" 0 | 1 | 2 ")
  print("---|---|---")
  print(" 3 | 4 | 5 ")
  print("---|---|---")
  print(" 6 | 7 | 8 ")

xState=[0,0,0,0,0,0,0,0]
zState=[0,0,0,0,0,0,0,0]

turn=1 
print("Below is the tic tac toe Python program")
print("x's Chance")

while(True):
  printBoard(xState,zState)
  if (turn==1):
    print("X's Chance")
    value=int(input("please enter value: "))
    zState[value]=1
  else:
    print("O's Chance")
    value=int(input("please enter value: "))
    xState[value]=1
  break