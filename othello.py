import math, copy, random, string, time
import Strategy, StrategyMed
#################################################
# Term Project: Othello
#
# Your name: Sree Revoori   
# Your andrew id: srevoori
# Section: D1
#################################################
from cmu_112_graphics import *
from tkinter import *
from collections import OrderedDict 
#Driver file; takes care of UI and runs everything
def appStarted(app):
    app.rows = 10
    app.cols = 10
    app.gamePage = True
    app.isPaused = False
    app.gameOver = False
    app.pvpMode = False
    app.spectateMode = False
    app.aiOneMode = False
    app.aiTwoMode = False
    app.aiThreeMode = False
    app.timerDelay = 1500
    app.margin = 10
    app.moves = [(3, 4), (4, 3), (5, 6), (6, 5)]
    app.cellSize = app.width / app.rows
    app.buttonWidth = (app.width - 2 * app.margin - 8*app.margin)/5
    app.buttonHeight = (app.height/3)/7 
    app.buttonY = (app.height/3) + (3/7) * (app.height/3)
    app.pvpX = app.margin
    app.spectateX = app.pvpX + 2 * app.margin + app.buttonWidth
    app.aiOneX = app.spectateX + 2 * app.margin + app.buttonWidth
    app.aiTwoX = app.aiOneX + 2 * app.margin + app.buttonWidth
    app.aiThreeX = app.aiTwoX + 2 * app.margin + app.buttonWidth
    app.board = "???????????........??........??........??........??........??........??........??........???????????"
    app.matrix = [ (["."] * app.cols) for row in range(app.rows) ]
    app.board = place(app.board, 44, "o")
    app.board = place(app.board, 54, "@")
    app.board = place(app.board, 55, "o")
    app.board = place(app.board, 45, "@")
    app.score1 = 2
    app.score2 = 2
    app.playerSymbol = "@"
    app.click = (-1, -1)
    app.turnSwap = False
    app.blackMoves = app.moves
    app.whiteMoves = []
    app.moveAssist = (-1, -1)

def resetApp(app):
    app.gamePage = True
    app.isPaused = False
    app.gameOver = False
    app.pvpMode = False
    app.spectateMode = False
    app.aiOneMode = False
    app.aiTwoMode = False
    app.aiThreeMode = False
    app.timerDelay = 1500
    app.moves = [(3, 4), (4, 3), (5, 6), (6, 5)]
    app.blackMoves = app.moves
    app.whiteMoves = []
    app.board = "???????????........??........??........??........??........??........??........??........???????????"
    app.matrix = [ (["."] * app.cols) for row in range(app.rows) ]
    app.board = place(app.board, 44, "o")
    app.board = place(app.board, 54, "@")
    app.board = place(app.board, 55, "o")
    app.board = place(app.board, 45, "@")
    app.score1 = 2
    app.score2 = 2
    app.playerSymbol = "@"
    app.click = (-1, -1)
    app.turnSwap = False
    app.moveAssist = (-1, -1)

def redrawAll(app, canvas):
    if app.gamePage == True:
        drawOthello(app, canvas)
    else:    
        drawBoard(app, canvas)
        drawScore(app, canvas)
        drawTurn(app, canvas)
        drawMoveAssist(app, canvas)
        drawGameOver(app, canvas)
def drawMoveAssist(app, canvas):
    if app.gamePage == False:
        if not app.spectateMode:
            if not app.pvpMode:
                canvas.create_rectangle(app.width-2*app.cellSize+4, app.height-60, app.width-app.cellSize-2, app.height-10, fill = "white")
                canvas.create_text((app.width-2*app.cellSize+4+app.width-app.cellSize-2)/2, app.height-35, text = "Hint!", font='Garamond 10 bold')
                drawCell(app, canvas, app.moveAssist[0], app.moveAssist[1], "help")
def drawOthello(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height/3, fill = "black")
    canvas.create_rectangle(0, app.height/3, app.width, app.height*(2/3), fill = "black")
    canvas.create_rectangle(0, app.height*(2/3), app.width, app.height, fill = "black")
    canvas.create_text(app.width/2, app.height/6, fill = "#17a2b8", text = "Othello", font='Garamond 50 bold')
    canvas.create_text(app.width/2, app.height/6 + 50, fill = "white", text = "A Game By Sree Revoori", font='Garamond 20 bold')
    canvas.create_rectangle(app.pvpX, app.buttonY, app.pvpX + app.buttonWidth, app.buttonY + app.buttonHeight, fill = "white")
    canvas.create_rectangle(app.spectateX, app.buttonY, app.spectateX + app.buttonWidth, app.buttonY + app.buttonHeight, fill = "white")
    canvas.create_rectangle(app.aiOneX, app.buttonY, app.aiOneX + app.buttonWidth, app.buttonY + app.buttonHeight, fill = "white")
    canvas.create_rectangle(app.aiTwoX, app.buttonY, app.aiTwoX + app.buttonWidth, app.buttonY + app.buttonHeight, fill = "white")
    canvas.create_rectangle(app.aiThreeX, app.buttonY, app.aiThreeX + app.buttonWidth, app.buttonY + app.buttonHeight, fill = "white")
    canvas.create_text(app.pvpX + (app.buttonWidth/2), app.buttonY + (app.buttonHeight/2), text = "Player vs. Player", fill = "black", font="Garamond 12" )
    canvas.create_text(app.spectateX + (app.buttonWidth/2), app.buttonY + (app.buttonHeight/2), text = "Spectate Game", fill = "black", font="Garamond 12" )
    canvas.create_text(app.aiOneX + (app.buttonWidth/2), app.buttonY + (app.buttonHeight/2), text = "Easy AI Mode", fill = "black", font="Garamond 12" )
    canvas.create_text(app.aiTwoX + (app.buttonWidth/2), app.buttonY + (app.buttonHeight/2), text = "Medium AI Mode", fill = "black", font="Garamond 11")
    canvas.create_text(app.aiThreeX + (app.buttonWidth/2), app.buttonY + (app.buttonHeight/2), text = "Hard AI Mode", fill = "black", font="Garamond 12")

def drawGameOver(app, canvas):
    if app.gameOver == True:
        canvas.create_rectangle(app.width/2 - 100, app.height/2 - 50, app.width/2 + 100, app.height/2 + 100, fill = "black", outline= "white")
        canvas.create_text(app.width/2, app.height/2, text = "Game Over!", font='Garamond 20 bold', fill = "red")
        if app.score1 > app.score2:
            canvas.create_text(app.width/2, 50 + app.height/2, text = "Black Wins!", font='Garamond 20 bold', fill = "gold")
        elif app.score2 > app.score1:
            canvas.create_text(app.width/2, 50 + app.height/2, text = "White Wins!", font='Garamond 20 bold', fill = "gold")
        else:
            canvas.create_text(app.width/2, 50 + app.height/2, text = "Draw!", font='Garamond 20 bold', fill = "gold")

def drawTurn(app, canvas):
    turn = ""
    if app.playerSymbol == "@":
        turn = "Black's"
    else:
        turn = "White's"
    if not app.gamePage:
        if not app.spectateMode:
            if not app.gameOver:
                if app.pvpMode:
                    canvas.create_text(app.width/2, app.height-52, text = f"{turn} turn" , font='Garamond 13 bold', fill = "pink")
                else:
                    if turn == "Black's":
                        canvas.create_text(app.width/2, app.height-52, text = "Your turn" , font='Garamond 13 bold', fill = "pink")
                    else:
                        canvas.create_text(app.width/2, app.height-52, text = "Thinking..." , font='Garamond 13 bold', fill = "pink")

def drawBoard(app, canvas):
    symbol = ""
    for row in range(app.rows):
        for col in range(app.cols):
            symbol = app.matrix[row][col]
            drawCell(app, canvas, row, col, symbol)

def drawScore(app, canvas):
    canvas.create_text(app.width/2, app.height-20, text = "Black: " + str(app.score1) + " White: " + str(app.score2), font='Garamond 15 bold', fill = "gold")

def createMatrix(app):
    count = 0
    for i in range(len(app.matrix)):
        for j in range(len(app.matrix[0])):
            app.matrix[i][j] = app.board[count]
            count+=1
    for i in app.moves:
        app.matrix[i[0]][i[1]] = "g"

def createPvPMatrix(app):
    count = 0
    for i in range(len(app.matrix)):
        for j in range(len(app.matrix[0])):
            app.matrix[i][j] = app.board[count]
            count+=1
    if app.playerSymbol == "@":
        for i in app.blackMoves:
            app.matrix[i[0]][i[1]] = "g"
    elif app.playerSymbol == "o":
        for i in app.whiteMoves:
            app.matrix[i[0]][i[1]] = "g"

def createSpectatorMatrix(app):
    count = 0
    for i in range(len(app.matrix)):
        for j in range(len(app.matrix[0])):
            app.matrix[i][j] = app.board[count]
            count+=1

def mousePressed(app, event):
    if app.gamePage == True:         
        if ((app.pvpX <= event.x <= app.pvpX+app.buttonWidth) and
            (app.buttonY <= event.y <= app.buttonY + app.buttonHeight)):
            app.pvpMode = True
            createMatrix(app)
            app.timerDelay = 0
            app.gamePage = False
        elif ((app.spectateX <= event.x <= app.spectateX+app.buttonWidth) and
            (app.buttonY <= event.y <= app.buttonY + app.buttonHeight)):
            app.spectateMode = True
            app.timerDelay = 0
            createSpectatorMatrix(app)
            app.gamePage = False
        elif ((app.aiOneX <= event.x <= app.aiOneX+app.buttonWidth) and
            (app.buttonY <= event.y <= app.buttonY + app.buttonHeight)):
            app.aiOneMode = True
            createMatrix(app)
            app.gamePage = False
        elif ((app.aiTwoX <= event.x <= app.aiTwoX+app.buttonWidth) and
            (app.buttonY <= event.y <= app.buttonY + app.buttonHeight)):
            app.aiTwoMode = True
            createMatrix(app)
            app.gamePage = False
        elif ((app.aiThreeX <= event.x <= app.aiThreeX+app.buttonWidth) and
            (app.buttonY <= event.y <= app.buttonY + app.buttonHeight)):
            app.aiThreeMode = True
            createMatrix(app)
            app.gamePage = False
    elif app.aiOneMode or app.aiThreeMode or app.aiTwoMode or app.pvpMode:
        row, col = event.y // app.cellSize, event.x // app.cellSize
        app.click = int(row), int(col)
        if not app.pvpMode:
            if not app.gameOver:
                if app.width-2*app.cellSize+4 <= event.x <= app.width-app.cellSize-2 and app.height-60 <= event.y <= app.height-10:
                    s = Strategy.Strategy()
                    helperMove = s.best_strategy(app.board, app.playerSymbol)
                    helperBoard = move(app.board, app.playerSymbol, helperMove)
                    for i in range(len(app.board)):
                        if helperBoard[i] != app.board[i]:                    
                            app.moveAssist = (i//10, i%10)
                            if app.moveAssist in app.moves:
                                break
    elif app.spectateMode:
        resetApp(app)
        app.spectateMode = True
        app.timerDelay = 0
        createSpectatorMatrix(app)
        app.gamePage = False

#finds cell bounds and draws cell
def drawCell(app, canvas, row, col, symbol):
    tLeftX = (col) * app.cellSize
    tLeftY = (row) * app.cellSize
    bRightX = tLeftX + app.cellSize
    bRightY = tLeftY + app.cellSize
    canvas.create_rectangle(tLeftX, tLeftY, bRightX, bRightY, width = 7, fill = "green")
    if symbol == "o":
        canvas.create_oval(tLeftX+8, tLeftY+8, bRightX-8, bRightY-8, fill = "white")
    elif symbol == "@":
        canvas.create_oval(tLeftX+8, tLeftY+8, bRightX-8, bRightY-8, fill = "black")
    elif symbol == "?":
        canvas.create_rectangle(tLeftX, tLeftY, bRightX, bRightY, fill = "black")
        if row == 0 and col != 9:
            if 0 < col < 9:
                canvas.create_text(tLeftX + (app.cellSize/2), tLeftY + (app.cellSize/2), text = f"{chr(col+64)}", font = "Garamond 15 bold", fill = "white")
        elif col == 0 and row != 9:
            if 0 < row < 9:
                canvas.create_text(tLeftX + (app.cellSize/2), tLeftY + (app.cellSize/2), text = f"{row}", font = "Garamond 15 bold", fill = "white")
        elif row == 9:
            canvas.create_rectangle(tLeftX, tLeftY, bRightX, bRightY, fill = "black")
        elif col == 9:
            canvas.create_rectangle(tLeftX, tLeftY, bRightX, bRightY, fill = "black")
    elif symbol == "g":
        canvas.create_rectangle(tLeftX, tLeftY, bRightX, bRightY, fill = "#9ffbe0")
    elif symbol == "help":
        canvas.create_rectangle(tLeftX, tLeftY, bRightX, bRightY, fill = "red")

def keyPressed(app, event):
    if event.key == "p":
        app.isPaused = not app.isPaused
    if event.key == "r":
        resetApp(app)

def timerFired(app):
    if app.isPaused == False and app.gameOver == False and app.gamePage == False:
        if app.spectateMode == True:
            s = Strategy.Strategy()
            s2 = StrategyMed.Strategy()
            if "." in app.board:
                if len(possibleMoves(app.board, app.playerSymbol)) == 0:
                    createSpectatorMatrix(app)
                else:
                    if app.playerSymbol == "@":
                        cpu_move = s.best_strategy(app.board, app.playerSymbol)
                        app.board = move(app.board, app.playerSymbol, cpu_move)
                        score(app)
                        createSpectatorMatrix(app)
                    else:
                        app.board, index = randommove(app.board, app.playerSymbol)
                        score(app)
                        createSpectatorMatrix(app)
                app.playerSymbol = "o" if app.playerSymbol == "@" else "@"
            elif "." not in app.board:
                score(app)
                app.gameOver = True

        elif app.aiOneMode == True:
            if "." in app.board:
                if len(possibleMoves(app.board, app.playerSymbol)) == 0:
                    app.turnSwap = True
                    app.moveAssist = (-1, -1)
                    createMatrix(app)
                else:
                    if app.playerSymbol == "@":
                        #player's turn
                        moves = possibleMoves(app.board, app.playerSymbol)
                        player_move = app.click
                        
                        if player_move in app.moves:
                            app.turnSwap = True
                            app.moveAssist = (-1, -1)
                            app.board = move(app.board, app.playerSymbol, (player_move[0]*10) + player_move[1])
                            app.moves.clear()
                            score(app)
                            createMatrix(app)
                    elif app.playerSymbol == "o":
                        #ai's turn
                        app.board, index = randommove(app.board, app.playerSymbol)
                        app.moves.clear()
                        moves = possibleMoves(app.board, "@")
                        for i in range(len(moves)):
                            app.moves.append((moves[i]//10, moves[i]%10))
                        createMatrix(app)
                        app.turnSwap = True
                        app.moveAssist = (-1, -1)
                        score(app)
                if app.turnSwap:
                    app.playerSymbol = "o" if app.playerSymbol == "@" else "@"
                    app.turnSwap = False
            elif "." not in app.board:
                score(app)
                app.gameOver = True

        elif app.aiTwoMode:
            s = StrategyMed.Strategy()
            if "." in app.board:
                if len(possibleMoves(app.board, app.playerSymbol)) == 0:
                    app.turnSwap = True
                    app.moveAssist = (-1, -1)
                    createMatrix(app)
                else:
                    if app.playerSymbol == "@":
                        moves = possibleMoves(app.board, app.playerSymbol)
                        player_move = app.click
                        if player_move in app.moves:
                            app.turnSwap = True
                            app.board = move(app.board, app.playerSymbol, (player_move[0]*10) + player_move[1])
                            app.moveAssist = (-1, -1)
                            app.moves.clear()
                            score(app)
                            createMatrix(app)
                    if app.playerSymbol == "o":
                        cpu_move = s.best_strategy(app.board, app.playerSymbol)
                        app.board = move(app.board, app.playerSymbol, cpu_move)
                        app.moves.clear()
                        moves = possibleMoves(app.board, "@")
                        for i in range(len(moves)):
                            app.moves.append((moves[i]//10, moves[i]%10))
                        createMatrix(app)
                        app.turnSwap = True
                        app.moveAssist = (-1, -1)
                        score(app)
                if app.turnSwap:
                    app.playerSymbol = "o" if app.playerSymbol == "@" else "@"
                    app.turnSwap = False
            elif "." not in app.board:
                score(app)
                app.gameOver = True

        elif app.aiThreeMode:
            s = Strategy.Strategy()
            if "." in app.board:
                if len(possibleMoves(app.board, app.playerSymbol)) == 0:
                    app.turnSwap = True
                    app.moveAssist = (-1, -1)
                    createMatrix(app)
                else:
                    if app.playerSymbol == "@":
                        moves = possibleMoves(app.board, app.playerSymbol)
                        player_move = app.click
                        if player_move in app.moves:
                            app.turnSwap = True
                            app.board = move(app.board, app.playerSymbol, (player_move[0]*10) + player_move[1])
                            app.moveAssist = (-1, -1)
                            app.moves.clear()
                            score(app)
                            createMatrix(app)
                    if app.playerSymbol == "o":
                        cpu_move = s.best_strategy(app.board, app.playerSymbol)
                        app.board = move(app.board, app.playerSymbol, cpu_move)
                        app.moves.clear()
                        moves = possibleMoves(app.board, "@")
                        for i in range(len(moves)):
                            app.moves.append((moves[i]//10, moves[i]%10))
                        createMatrix(app)
                        app.turnSwap = True
                        app.moveAssist = (-1, -1)
                        score(app)
                if app.turnSwap:
                    app.playerSymbol = "o" if app.playerSymbol == "@" else "@"
                    app.turnSwap = False
            elif "." not in app.board:
                score(app)
                app.gameOver = True

        elif app.pvpMode:
            if "." in app.board:
                if len(possibleMoves(app.board, app.playerSymbol)) == 0:
                    #equivalent to passing if no legal moves
                    app.turnSwap = True
                    createMatrix(app)
                else:
                    if app.playerSymbol == "@":
                    #p1's (black) turn
                        player_move = app.click
                        if player_move in app.blackMoves:
                            app.turnSwap = True
                            app.board = move(app.board, app.playerSymbol, (player_move[0]*10) + player_move[1])
                            score(app)
                        app.whiteMoves.clear()
                        whiteMoves = possibleMoves(app.board, "o")
                        for i in range(len(whiteMoves)):
                            #clear previous white legal moves and calculate future white legal moves
                            app.whiteMoves.append((whiteMoves[i]//10, whiteMoves[i]%10))
                    elif app.playerSymbol == "o":
                    #p2's (white) turn
                        player_move = app.click
                        if player_move in app.whiteMoves:
                            app.turnSwap = True
                            app.board = move(app.board, app.playerSymbol, (player_move[0]*10) + player_move[1])
                            score(app)
                        app.blackMoves.clear()
                        blackMoves = possibleMoves(app.board, "@")
                        for i in range(len(blackMoves)):
                            #clear previous black legal moves and calculate future black legal moves
                            app.blackMoves.append((blackMoves[i]//10, blackMoves[i]%10))
                if app.turnSwap:
                    #swaps turns
                    if app.playerSymbol == "@":
                        app.playerSymbol = "o"
                    elif app.playerSymbol == "o":
                        app.playerSymbol = "@"
                    app.turnSwap = False
                    createPvPMatrix(app)
            elif "." not in app.board:
                #if no more spots
                score(app)
                app.gameOver = True


            
            

'''Lets user input dimensions of the game. NOT IN USE'''
def gameDimensions():
    xLen = input("Enter Width (Pixels): ")
    yLen = input("Enter Height (Pixels): ")
    return int(xLen), int(yLen)

'''Is able to use dimensions from user input to start game'''
def playOthello():
    #dim = gameDimensions()
    runApp(width = 650, height = 650)



"""Prints the board, formatted nicely."""
def print_board(b):
    count = 0
    for i in range(0, 100):
        if count % 10 == 0:
            print()
        print(b[i] + " ", end='')
        count += 1
    print()

"""Given a position index on the board, and a player piece, places that piece on the board."""
def place(b, index, symbol):
    copy = b
    copy = copy[0:index] + symbol + copy[index + 1:]
    return copy



"""Returns a list of the positions of all possible moves for a given player and board."""
def possibleMoves(copy, symbol):
    board = copy[:]
    if symbol == "o":
        enemysymbol = "@"
    else:
        enemysymbol = "o"
    pmove = []
    for x in range(10, 89):
        if board[x] != ".":
            continue
        if board[x - 1] is enemysymbol:
            loop = 1
            # check right rows
            while board[x - loop] is enemysymbol:
                loop += 1
            if board[x - loop] is symbol:
                pmove.append(x)

        if board[x + 1] is enemysymbol:
            loop = 1
            # check ten rows down
            while board[x + loop] is enemysymbol:
                loop += 1
            if board[x + loop] is symbol:
                pmove.append(x)

        if board[x - 10] is enemysymbol:
            loop = 10
            # check ten rows up
            while board[x - loop] is enemysymbol:
                loop += 10
            if board[x - loop] is symbol:
                pmove.append(x)

        if board[x + 10] is enemysymbol:
            loop = 10
            # check ten rows left
            while board[x + loop] is enemysymbol:
                loop += 10
            if board[x + loop] is symbol:
                pmove.append(x)

        if board[x - 9] is enemysymbol:
            loop = 9
            while board[x - loop] is enemysymbol:
                loop += 9
            if board[x - loop] is symbol:
                pmove.append(x)

        if board[x + 9] is enemysymbol:
            loop = 9
            # check ten rows back
            while board[x + loop] is enemysymbol:
                loop += 9
            if board[x + loop] is symbol:
                pmove.append(x)

        if board[x - 11] is enemysymbol:
            loop = 11
            # check ten rows diagonal
            while board[x - loop] is enemysymbol:
                loop += 11
            if board[x - loop] is symbol:
                pmove.append(x)

        if board[x + 11] is enemysymbol:
            loop = 11
            # check left rows
            while board[x + loop] is enemysymbol:
                loop += 11
            if board[x + loop] is symbol:
                pmove.append(x)

    k = set(pmove)
    pmove = list(k)
    return pmove

"""Places a piece on the board, given an index, and updates the board accordingly."""
def move(copy, symbol, index):
    board = copy[:]
    board = board[0:index] + symbol + board[index + 1:]
    temp = []
    x = index

    if symbol == "o":
        enemysymbol = "@"
    else:
        enemysymbol = "o"

    if board[x - 1] is enemysymbol:
        loop = 1
        while board[x - loop] is enemysymbol:
            temp.append(x - loop)
            loop += 1
        if board[x - loop] is symbol:
            for each in temp:
                board = board[0: each] + symbol + board[each + 1:]
    temp = []

    if board[x + 1] is enemysymbol:
        loop = 1
        while board[x + loop] is enemysymbol:
            temp.append(x + loop)
            loop += 1
        if board[x + loop] is symbol:
            for each in temp:
                board = board[0: each] + symbol + board[each + 1:]
    temp = []

    if board[x - 10] is enemysymbol:
        loop = 10
        temp.append(x - loop)
        loop = 10
        while board[x - loop] is enemysymbol:
            temp.append(x - loop)
            loop += 10
        if board[x - loop] is symbol:
            for each in temp:
                board = board[0: each] + symbol + board[each + 1:]
    temp = []

    if board[x + 10] is enemysymbol:

        loop = 10
        while board[x + loop] is enemysymbol:
            temp.append(x + loop)
            loop += 10
        if board[x + loop] is symbol:
            for each in temp:
                board = board[0: each] + symbol + board[each + 1:]
    temp = []

    if board[x - 9] is enemysymbol:
        loop = 9
        while board[x - loop] is enemysymbol:
            temp.append(x - loop)
            loop += 9
        if board[x - loop] is symbol:
            for each in temp:
                board = board[0: each] + symbol + board[each + 1:]
    temp = []

    if board[x + 9] is enemysymbol:
        loop = 9
        while board[x + loop] is enemysymbol:
            temp.append(x + loop)
            loop += 9
        if board[x + loop] is symbol:
            for each in temp:
                board = board[0: each] + symbol + board[each + 1:]
    temp = []

    if board[x - 11] is enemysymbol:
        loop = 11
        while board[x - loop] is enemysymbol:
            temp.append(x - loop)
            loop += 11
        if board[x - loop] is symbol:
            for each in temp:
                board = board[0: each] + symbol + board[each + 1:]
    temp = []

    if board[x + 11] is enemysymbol:
        loop = 11
        while board[x + loop] is enemysymbol:
            temp.append(x + loop)
            loop += 11
        if board[x + loop] is symbol:
            for each in temp:
                board = board[0: each] + symbol + board[each + 1:]
    temp = []

    return board

"""Given a board and a player, returns a new board updated with a random move by that player"""
def randommove(board, symbol):
    moves = possibleMoves(board, symbol)
    moves = sorted(moves)
    index = random.choice(moves)
    board = move(board, symbol, index)
    return board, index

"""Prints score of the board for each player, black and white, as a percentage of spots controlled."""
def score(app):
    countBlack = 0
    countWhite = 0
    for each in app.board:
        if each == "@":
            countBlack += 1
        if each == "o":
            countWhite += 1
    app.score1, app.score2 = countBlack, countWhite    

playOthello()
