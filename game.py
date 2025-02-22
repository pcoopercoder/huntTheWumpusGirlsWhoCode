# Hunt the Wumpus: Portia's Code :3

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

print("🦇 Welcome to Hunt the Wumpus!🦇")
print("You are in a cave with a wumpus 👹.")
print("Your goal is to find the wumpus and avoid falling into a bottomless pit 🕳️.")
   
   
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
    board[userY][userX] = "p"
    userX += 1
    board[userY][userX] = "p"


for row in board:
    print(row)
 

# Let's update the Wumpus's position
  
# Once we update the board, we need to let the user know 
# if they are near any harzards




