from platform import python_branch

board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

def displayBoard():
    for row in board:
        for space in row:
            print(space, end = "")
        print()

class Player:


    def __init__(self, playerOrder, marker, columnChoices = [1, 2, 3], rowChoices = [1, 2, 3], markerCoordinates = [1,1]):
        self.marker = marker
        self.playerOrder = playerOrder
        self.columnChoices = columnChoices
        self.rowChoices = rowChoices
        self.markerCoordinates = markerCoordinates


    def __repr__(self):
        return "Player {playerOrder} will use the {marker} marker.".format(playerOrder = self.playerOrder, marker = self.marker)


    def stateColumn(self):
        self.columnChoice = print(input("Column: "))
        if self.columnChoice in self.columnChoices: # marker coords loaded with choice - 1 (1-1 = 0, the corresponding index)
            self.markerCoordinates[0] = self.columnChoice - 1
        else:
            print("Column {} does not exist. Please try again.".format(self.columnChoice))


    def stateRow(self):
        self.rowChoice = print(input("Row: "))
        if self.rowChoice in self.rowChoices: # marker coords loaded with choice - 1 (1-1 = 0, the corresponding index)
            self.markerCoordinates[1] = self.rowChoice - 1
        else:
            print("Row {} does not exist. Please try again.".format(self.rowChoice))

    
    def placeMarker(self):
        if board[self.markerCoordinates[1]][self.markerCoordinates[0]] == "-":
            board[self.markerCoordinates[1]][self.markerCoordinates[0]] = self.marker
            print("Turn completed!")
        else:
            print("You can't place a marker there!")


    def takeTurn(self):
        print(displayBoard())
        print(Player.stateColumn(self))
        print(Player.stateRow(self))
        print(Player.placeMarker(self))
        


turnCounter = 1

playerX = Player(1, "X")

playerO = Player(2, "O")

#  Carrying out the game:

#  Explain game:
gameDescription = """
This program allows for a game of two-player Tic-Tac-Toe. 
Each player will try to match three of their marker in a row. 
Victories may occur vertically, horizontally, or diagonally. 
If neither player matches three in a row, the game is pronounced a draw.
To place a marker, enter the column (increasing left to right),
then the row (increasing top down).
Good luck!
"""
print(gameDescription)

#  Print __repr__:
print(playerX)

print(playerO)

# Take Turns:
if turnCounter % 2 == 1:
    print(Player.takeTurn(playerX))
else:
    print(Player.takeTurn(playerO))






    
