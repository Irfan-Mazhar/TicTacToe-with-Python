import sys

def printboard(xState,oState):
    zero = 'X' if xState[0] else ('O' if oState[0] else 0)
    one = 'X' if xState[1] else ('O' if oState[1] else 1)
    two = 'X' if xState[2] else ('O' if oState[2] else 2)
    three = 'X' if xState[3] else ('O' if oState[3] else 3)
    four = 'X' if xState[4] else ('O' if oState[4] else 4)
    five = 'X' if xState[5] else ('O' if oState[5] else 5)
    six = 'X' if xState[6] else ('O' if oState[6] else 6)
    seven = 'X' if xState[7] else ('O' if oState[7] else 7)
    eight = 'X' if xState[8] else ('O' if oState[8] else 8)
    print(f"{zero} | {one} | {two}")
    print("--|---|---")
    print(f'{three} | {four} | {five}')
    print("--|---|---")
    print(f'{six} | {seven} | {eight}')

def sums(a,b,c):
    return a+b+c

def repeat():
    play = input("Do you want to play again?")
    if play != "y":
        sys.exit()
    else:
        global xState
        global oState
        global turn
        xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        oState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        turn = 1

def checkWin(xState,oState):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[6,4,2]]
    for win in wins:
        if (sums(xState[win[0]],xState[win[1]],xState[win[2]]))==3:
            printboard(xState, oState)
            print("X wins the Game!")
            return 1
        if(sums(oState[win[0]], oState[win[1]], oState[win[2]]))==3:
            printboard(xState, oState)
            print("O wins the Game!")
            return 0

print("Welcome to Tic Tac Toe!")
play = input('Do you want to start?')
while (play=="y"):
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    oState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    while(True):
        printboard(xState,oState)
        if turn==1:
            print("X's Turn")
            val = int(input("Enter your choice: "))
            xState[val] = 1
            turn -= 1
        else:
            print("O's Turn")
            val = int(input("Enter your choice: "))
            oState[val] = 1
            turn += 1
        cwin = checkWin(xState, oState)
        if (cwin== 0 or cwin == 1) :
           repeat()
        if sum(xState) == 5 and  sum(oState) == 4 and  (cwin!=0 or cwin!=1):
            printboard(xState, oState)
            print("Game over. DRAW")
            repeat()
