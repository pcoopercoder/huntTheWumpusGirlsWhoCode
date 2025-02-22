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

holeLocations = []

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
    userY += 1
# left
elif move == "a":
    userX -= 1
# right
else:
    userX += 1
 

# Let's update the Wumpus's position
  
# Once we update the board, we need to let the user know 
# if they are near any harzards




