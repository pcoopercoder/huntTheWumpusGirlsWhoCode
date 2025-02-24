# Hunt the Wumpus: Portia's Code :3
# WARNING: THIS CODE ISN'T FULLY WORKING 

import random

'''
TO DO:
    Finish board update
    Finish user movement
    Notify player of hazards above, below, to the left or right of them
    Add wumpus movement
    Give Player the ability to shoot arrows
    Create a gameplay loop
'''

# Cave Board
# p represents the player
# o represents a hole
# w represents the wumpus
# _ represents an empty space
board = [["p", "_", "_", "_", "o"],
         ["_", "o", "_", "_", "_"],
         ["_", "_", "w", "o", "_"],
         ["_", "_", "_", "_", "_"],
         ["o", "_", "_", "_", "_"]]

holeLocations = [[0,4], [1,1], [2,3], [4,0]]

# Inital Player Position
userX = 0
userY = 0

# Inital Wumpus Position
wumpusX = 2
wumpusY = 2

gameOver = False

print("🦇 Welcome to Hunt the Wumpus!🦇")
print("You are in a cave with a wumpus 👹.")
print("Your goal is to find the wumpus and avoid falling into a bottomless pit 🕳️.")

while gameOver != True:
    print()
    for row in board:
        print(row)  
    
    # Get a move from the player    
    move = input("Enter a move (w=up, a=left, d=right, and s=down): ")


    # up
    if move == "w":
        board[userY][userX] = "_"
        userY -= 1
        board[userY][userX] = "p"
    # down
    elif move == "s":
        board[userY][userX] = "_"
        userY += 1
        board[userY][userX] = "p"
    # left
    elif move == "a":
        board[userY][userX] = "_"
        userX -= 1
        board[userY][userX] = "p"
    # right
    else:
        board[userY][userX] = "_"
        userX += 1
        board[userY][userX] = "p"

    for holeCoordinate in holeLocations:
        if userX == -1:
            userX = 4
        if userY == -1:
            userY = 4    
        if userX == holeCoordinate[1] and userY == holeCoordinate[0]:
            gameOver = True

    if gameOver:
        print("You Lose!!!")


    for row in board:
        print(row)
    

    # Let's update the Wumpus's position
    randomDir = random.choices(["up", "down", "left", "right"])

    # up
    if randomDir == "up":
        temp = wumpusY - 1
        dontMove = False

        for holeCoordinate in holeLocations:
            if wumpusX == -1:
                wumpusX = 4
            if wumpusY == -1:
                wumpusY = 4    
            if wumpusX == holeCoordinate[1] and wumpusY == holeCoordinate[0]:
                dontMove = True

        if wumpusY == userX and wumpusX == userY:
            dontMove = True

        if not dontMove:
            board[wumpusY][wumpusX] = "_"
            wumpusY -= 1
            board[wumpusY][wumpusX] = "w"
    # down
    elif randomDir == "down":
        temp = wumpusY + 1
        dontMove = False

        for holeCoordinate in holeLocations:
            if wumpusX == -1:
                wumpusX = 4
            if wumpusY == -1:
                wumpusY = 4    
            if wumpusX == holeCoordinate[1] and wumpusY == holeCoordinate[0]:
                dontMove = True

        if wumpusY == userX and wumpusX == userY:
            dontMove = True

        if not dontMove:
            board[wumpusY][wumpusX] = "_"
            wumpusY += 1
            board[wumpusY][wumpusX] = "w"
    # left
    elif randomDir == "left":
        temp = wumpusX - 1
        dontMove = False

        for holeCoordinate in holeLocations:
            if wumpusX == -1:
                wumpusX = 4
            if wumpusY == -1:
                wumpusY = 4    
            if wumpusX == holeCoordinate[1] and wumpusY == holeCoordinate[0]:
                dontMove = True

        if wumpusY == userX and wumpusX == userY:
            dontMove = True

        if not dontMove:
            board[wumpusY][wumpusX] = "_"
            wumpusX -= 1
            board[wumpusY][wumpusX] = "w"
    # right
    else:
        temp = wumpusX + 1
        dontMove = False

        for holeCoordinate in holeLocations:
            if wumpusX == -1:
                wumpusX = 4
            if wumpusY == -1:
                wumpusY = 4    
            if wumpusX == holeCoordinate[1] and wumpusY == holeCoordinate[0]:
                dontMove = True

        if wumpusY == userX and wumpusX == userY:
            dontMove = True

        if not dontMove:
            board[wumpusY][wumpusX] = "_"
            wumpusX += 1
            board[wumpusY][wumpusX] = "w"

    print()
    for row in board:
        print(row)

# Once we update the board, we need to let the user know 
# if they are near any harzards




