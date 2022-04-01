import random

def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


# PLAYER SELECTS WHAT THEY WANT TO USE
def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print("Do you want to be X or O")
        letter = input().upper()

        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

# RANDOMLY CHOSSES A PLAYER TO GO FIRST
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter
    
# SETS RULES ON HOW TO WIN
def isWinner(bo, le): # BO = BORED | LE = LETTER
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # TOP ROW
            (bo[4] == le and bo[5] == le and bo[6] == le) or # MIDDLE ROW
            (bo[1] == le and bo[2] == le and bo[3] == le) or # BOTTOM ROW
            (bo[7] == le and bo[4] == le and bo[1] == le) or # DOWN LEFT SIDE
            (bo[8] == le and bo[5] == le and bo[2] == le) or # DOWN MIDDLE
            (bo[9] == le and bo[6] == le and bo[3] == le) or # DOWN RIGHT SIDE
            (bo[7] == le and bo[5] == le and bo[3] == le) or # TOP LEFT TO BOTTOM RIGHT DIAGONAL
            (bo[9] == le and bo[5] == le and bo[1] == le)) # TOP TIGHT TO BOTTOM LEFT DIAGONAL

# MAKES A COPY OF THE BOARD LIST AND RETURNS IT
def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    return board[move] == ' '

# LETS THE PLAYER ENTER THERE MOVE
def getPlayerMove(board):
    move = ' ' 
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print("What is your next more? (1-9)")
        move = input()
    return int(move)    

# RETURNS A VALID MOVE FROM THE PASSED LIST ON THE PASSED BOARD
# RETURNS NONE IF THERE IS NO VALID MOVES
def chooseRandomMoveFromList(board, moveList):
    possibleMove = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMove.append(i)
    if len(possibleMove) != 0:
        return random.choice(possibleMove)
    else:
        return None
#------------------------------------------------------------------------------------------

# COMPUTER CHOOSES WHERE TO MOVE
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # FIRST, CHECK IF COMPUTER CAN WIN IN THE NEXT MOVE
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
    
    # CHECK IS PLAYER COULD WIN ON THERE NEXT MOVE OR BLOCK THEM
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
    
    # TRY TO TAKE ONE OF THE CORNERS IF THEY ARE FREE
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # TRY TO TAKE THE CENTER IF FREE
    if isSpaceFree(board, 5):
        return 5

    # MOVE ON ONE OF THE SIDES
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

#  RETURNS TRUE IF EVERY SPACE ON THE BOARD HAS BEEN TAKEN OTHERWISE RETURN FALSE
def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print("Welcome to Tic-Tac-Toe!")

while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print(f"The {turn} will go first.")
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("Hooray! You have won the game!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    turn = 'computer'

        else:
            # COMPUTERS TURN
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("The computer has beaten you! You lose :(")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    turn = 'player'
                



    


    