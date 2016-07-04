# Hello tic tac toe game players! let's code the game yoyo :p
import random
import sys
name=raw_input("What's your name? ")
sys.stderr.write("\x1b[2J\x1b[H")
board=[0,1,2,3,4,5,6,7,8]
def show():
    print board[0],'|',board[1],'|',board[2]
    print "--+---+--"
    print board[3],'|',board[4],'|',board[5]
    print "--+---+--"
    print board[6],'|',board[7],'|',board[8]
show()
def checkforallpositions(char):
    if checkforwin(char,0,1,2):
        return True
    if checkforwin(char,1,4,7):
        return True
    if checkforwin(char,2,5,8):
        return True
    if checkforwin(char,6,7,8):
        return True
    if checkforwin(char,3,4,5):
        return True
    if checkforwin(char,2,4,6):
        return True
    if checkforwin(char,0,3,6):
        return True
    if checkforwin(char,0,4,8):
        return True

def checkforwin(char,spot1,spot2,spot3):
    if board[spot1]==char and board[spot2]==char and board[spot3]==char:
        return True
def draw():
    flag=True
    for i in range(0,9):
        if board[i]!='O' and board[i]!='X':
            flag=False
    return flag

def minimax(char):
    if char=='X':
          if checkforallpositions('X'):
            return 1
    else:
          if checkforallpositions('O'):
            return 1
    move=-1
    score=-2
    for i in range(0,9):
        if board[i]!='O' and board[i]!='X':
            board[i]=char
            if char=='X':
                thisscore=-minimax('O')
            else:
                thisscore=-minimax('X')
            if thisscore>score:
                score=thisscore
                move=i
            board[i]=i
    if move==-1:
        return 0
    return score


def computer_move():
    move=-1
    score=-2
    for i in range(0,9):
        if board[i]!='O' and board[i]!='X':
            board[i]='O'
            tempscore=-minimax('X')
            board[i]=i
            if tempscore > score:
                score=tempscore
                move=i
    return move
def game_loop():      
    while True:
        input=raw_input("Select a spot ")
        input=int(input)
        if board[input]!='O' and board[input]!='X':
            board[input]='X'
            #check for winner
            if checkforallpositions('X'):
                sys.stderr.write("\x1b[2J\x1b[H")
                show()
                print "%s Wins!!!!"%(name)
                break;
            if draw():
                sys.stderr.write("\x1b[2J\x1b[H")
                show()
                print "It is a draw!!!"
                break;
            opponent=computer_move()

            board[opponent]='O'
            if checkforallpositions('O'):   
                sys.stderr.write("\x1b[2J\x1b[H")
                show()
                print "Computer wins!!!!"
                break;
            sys.stderr.write("\x1b[2J\x1b[H")
            show()
        else:
            print "The position is already taken! "
game_loop()
'''reply=raw_input("Wanna Play again? (y/n) ").lower()
while reply=='y':
    sys.stderr.write("\x1b[2J\x1b[H")
    for i in range(0,9):
        board[i]=i
    show()
    game_loop()
    reply=raw_input("Wanna Play again? (y/n) ").lower()'''
