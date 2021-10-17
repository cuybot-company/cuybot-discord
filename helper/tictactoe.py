board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
position = 0
player = "O"
bot = "X"
wins = ""
draw = False

# control in chat

def setPosition(pos):
    global position
    position = pos

def clearGame():
    global position
    global letter
    global board
    global wins

    position = 0
    wins = ""
    letter = ""
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def setWins(win):
    global wins
    wins = win

def getWins():
    global wins
    return wins

# end control

def printBoard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])
    print("\n")


def checkIsDraw():
    for key in range(0, 9):
        if board[key] == ' ':
            return False

    return True

def checkForWin():
    if (board[0] == board[1] and board[0] == board[2] and board[0] != ' '):
        return True
    elif (board[3] == board[4] and board[3] == board[5] and board[3] != ' '):
        return True
    elif (board[6] == board[7] and board[6] == board[8] and board[6] != ' '):
        return True
    elif (board[0] == board[3] and board[0] == board[6] and board[0] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[0] == board[4] and board[0] == board[8] and board[0] != ' '):
        return True
    elif (board[6] == board[4] and board[6] == board[2] and board[6] != ' '):
        return True
    else:
        return False

def checkPotentialWon(mark):
    if (board[0] == board[1] and board[0] == board[2] and board[0] == mark):
        return True
    elif (board[3] == board[4] and board[3] == board[5] and board[3] == mark):
        return True
    elif (board[6] == board[7] and board[6] == board[8] and board[6] == mark):
        return True
    elif (board[0] == board[3] and board[0] == board[6] and board[0] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[0] == board[4] and board[0] == board[8] and board[0] == mark):
        return True
    elif (board[6] == board[4] and board[6] == board[2] and board[6] == mark):
        return True
    else:
        return False

def spaceIsFree(position):
    return not bool(board[position].strip())

def insertTheLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)

        if(checkIsDraw()):
            print("draw")
            # clearGame()
            setWins("draw")
        
        if checkForWin():
            if letter == "X":
                print("Bot Wins!")                
                # clearGame()
                setWins("bot")
            else:
                print("Player Wins!")
                # clearGame()
                setWins("player")

        return
    else:
        print("can't insert there")
        return

def playerMove():
    global player
    global position

    insertTheLetter(player, position)

def computerMove():
    global bot
    global position

    bestScore = -1000
    bestMove = 0

    for key in range(0, 9):
        if(board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key

    insertTheLetter(bot, bestMove)
    return bestMove

def minimax(board, depth, isMaximizing):

    if checkPotentialWon(bot):
        return 100

    elif checkPotentialWon(player):
        return -100
    
    elif checkIsDraw():
        return 0

    if isMaximizing:
        bestScore = -1000

        for key in range(0, 9):
            if(board[key] == ' '):
                board[key] = bot
                score = minimax(board, 0, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score

        return bestScore
    
    else:
        bestScore = 1000

        for key in range(0, 9):
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore



# setPosition(0)
# playerMove()

# computerMove()

# setPosition(1)
# playerMove()

# computerMove()

# setPosition(6)
# playerMove()

# computerMove()

# setPosition(5)
# playerMove()

# computerMove()

# setPosition(8)
# playerMove()