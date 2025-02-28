# Hunt the Wumpus: Portia's Code :3

import random

'''
TO DO:
    Notify player of hazards above, below, to the left or right of them
    Create a gameplay loop
    Once we update the board, we need to let the user know if they are near any harzards
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

# BEGIN WHILE
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
    # down
    elif move == "s":
        board[userY][userX] = "_"
        userY += 1
    # left
    elif move == "a":
        board[userY][userX] = "_"
        userX -= 1
    # right
    else:
        board[userY][userX] = "_"
        userX += 1

    userX %= 5
    userY %= 5
         
    board[userY][userX] = "p"

    for holeCoordinate in holeLocations:
        if userX == holeCoordinate[1] and userY == holeCoordinate[0]:
            gameOver = True

    if gameOver:
        print("You Lose!!!")

    # Let's update the Wumpus's position
    randomDir = random.choice(["up", "down", "left", "right"])

    # BEGIN IF
    # up
    if randomDir == "up":
        temp = wumpusY - 1
        temp %= 5
        dontMove = False

        for holeCoordinate in holeLocations:
            if wumpusX == holeCoordinate[1] and temp == holeCoordinate[0]:
                dontMove = True

        if wumpusX == userX and temp == userY:
            dontMove = True

        if not dontMove:
            board[wumpusY][wumpusX] = "_"
            wumpusY = temp
            board[wumpusY][wumpusX] = "w"
    # down
    elif randomDir == "down":
        temp = wumpusY + 1
        temp %= 5  
        dontMove = False

        for holeCoordinate in holeLocations:
            if wumpusX == holeCoordinate[1] and temp == holeCoordinate[0]:
                dontMove = True

        if wumpusX == userX and temp == userY:
            dontMove = True

        if not dontMove:
            board[wumpusY][wumpusX] = "_"
            wumpusY = temp
            board[wumpusY][wumpusX] = "w"
    # left
    elif randomDir == "left":
        temp = wumpusX - 1
        temp %= 5
        dontMove = False

        for holeCoordinate in holeLocations:  
            if temp == holeCoordinate[1] and wumpusY == holeCoordinate[0]:
                dontMove = True

        if wumpusY == userY and temp == userX:
            dontMove = True

        if not dontMove:
            board[wumpusY][wumpusX] = "_"
            wumpusX = temp
            board[wumpusY][wumpusX] = "w"
    # right
    else:
        temp = wumpusX + 1
        temp %= 5
        dontMove = False

        for holeCoordinate in holeLocations:
            if temp == holeCoordinate[1] and wumpusY == holeCoordinate[0]:
                dontMove = True

        if wumpusY == userY and temp == userX:
            dontMove = True

        if not dontMove:
            board[wumpusY][wumpusX] = "_"
            wumpusX = temp
            board[wumpusY][wumpusX] = "w"
    # END IF
#END WHILE


