#define the number of cells on the board
board =[' ' for x in range(10)]

#function to insert the letter on the board
def insertLetter(letter,pos):
    board[pos] = letter

#cheks whether the space is free
def spacIsfree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |   |')
    print(' '+board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   |')
    print('------------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   |')
    print('------------')
    print('   |   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   |')


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def isWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))


def playerMove():
    run =True
    while run:
        move = input("Please select a position to enter the X between 1 and 9: ")
        try:
            move = int(move)
            if move  > 0 and  move < 10 :
                if spacIsfree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is not available')
            else:
                print('Please enter a number between 1 and 9 !')
        except:
            print('PLease enter a number !')


def computerMove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in['O', 'X']:
        for  i in possibleMoves:
            board_copy = board[:]
            board_copy[i] = let
            if isWinner(board_copy,let):
                move = i
                return move
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5  in possibleMoves:
        move = 5
        return move
    edgesOpen =[]
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]


def main():
    print("Welcome to our tic tac toe")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board,'O')):
            playerMove()
            printBoard(board)
        else:
            print('You lost the game!!!')
            break
        if not(isWinner(board,'X')):
            move = computerMove()
            if move == 0:
                print('Tie game')
            else:
                insertLetter('O',move)
                print('Computer played on position' , move,':' )
                printBoard(board)
        else:
            print('Congratulations,you have won!!!')

    if isBoardFull(board):
        print("You won the game")



while True:
    x = input("Do you want to continue ? (y/n): ")
    if x.lower() == 'y':
        board =[ ' ' for x in range(10)]
        print("------------------------")
        main()
    else:
        break


