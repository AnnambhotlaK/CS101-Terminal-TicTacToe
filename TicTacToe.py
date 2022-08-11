from platform import python_branch

class Board:

    def __init__(self, board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]], win = False):
        self.board = board
        self.win = win


    def __repr__(self):
        print("Board:")
        for row in self.board:
            for space in row:
                print(space, end = "")
            print()
        print("")


    def winCheck(self, player):

        tempMarkerList = []
        for list in self.board:
            for marker in list:
                tempMarkerList.append(marker)
        
        # Rows:
        if tempMarkerList[0:3] == [player.marker, player.marker, player.marker]:
            self.win = True
        elif tempMarkerList[3:6] == [player.marker, player.marker, player.marker]:
            self.win = True
        elif tempMarkerList[6:9] == [player.marker, player.marker, player.marker]:
            self.win = True
        
        # Columns:
        elif tempMarkerList[0] + tempMarkerList[3] + tempMarkerList[6] == player.marker + player.marker + player.marker:
            self.win = True
        elif tempMarkerList[1] + tempMarkerList[4] + tempMarkerList[7] == player.marker + player.marker + player.marker:
            self.win = True
        elif tempMarkerList[2] + tempMarkerList[5] + tempMarkerList[8] == player.marker + player.marker + player.marker:
            self.win = True
        
        # Diagonals:
        elif tempMarkerList[0] + tempMarkerList[4] + tempMarkerList[8] == player.marker + player.marker + player.marker:
            self.win = True
        elif tempMarkerList[2] + tempMarkerList[4] + tempMarkerList[6] == player.marker + player.marker + player.marker:
            self.win = True
        else:
            self.win = False
        
        return self.win



class Player:

    def __init__(player, playerOrder, marker, columnChoices = [1, 2, 3], rowChoices = [1, 2, 3], markerCoordinates = [1,1]):
        player.marker = marker
        player.playerOrder = playerOrder
        player.columnChoices = columnChoices
        player.rowChoices = rowChoices
        player.markerCoordinates = markerCoordinates


    def __repr__(player):
        return "Player {playerOrder} will use the {marker} marker.".format(playerOrder = player.playerOrder, marker = player.marker)


    def stateColumn(player):
        columnChoice = int(input("Column: "))
        while columnChoice not in player.columnChoices: # marker coords loaded with choice - 1 (1-1 = 0, the corresponding index)
            print("Column {choice} does not exist. Please try again.".format(choice = columnChoice))
            columnChoice = int(input("Column: "))
        else:
            # print("works")
            player.markerCoordinates[0] = columnChoice - 1
            return player.markerCoordinates[0]
            


    def stateRow(player):
        rowChoice = int(input("Row: "))
        while rowChoice not in player.rowChoices: # marker coords loaded with choice - 1 (1-1 = 0, the corresponding index)
            print("Row {choice} does not exist. Please try again.".format(choice = rowChoice))
            rowChoice = int(input("Row: "))
        else:
            player.markerCoordinates[1] = rowChoice - 1
            return player.markerCoordinates[0]
            

    
    def placeMarker(player, self):
        if self.board[player.markerCoordinates[1]][player.markerCoordinates[0]] == "-":
            self.board[player.markerCoordinates[1]][player.markerCoordinates[0]] = player.marker
            print("")
        else:
            print("You can't place a marker there!")
            columnCoordinate = Player.stateColumn(player)
            rowCoordinate = Player.stateRow(player)
            Player.placeMarker(player, self)



    def takeTurn(player, self):
        Board.__repr__(self)
        columnCoordinate = Player.stateColumn(player)
        rowCoordinate = Player.stateRow(player)
        Player.placeMarker(player, self)
        self.win = Board.winCheck(self, player)
        


turnCounter = 1

playerX = Player(1, "X")

playerO = Player(2, "O")

board = Board()

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

while board.win != True:

    if turnCounter >= 10:
        print("It's a draw!")

    if turnCounter % 2 == 1:
        print("Your turn, Player 1!")
        print("")
        Player.takeTurn(playerX, board)
    else:
        print("Your turn, Player 2!")
        print("")
        Player.takeTurn(playerO, board)

    if Board.winCheck(board, playerX) == True:
        print("Player 1 wins!")
        print("")
        Board.__repr__(board)

    elif Board.winCheck(board, playerO) == True:
        print("Player 2 wins!")
        print("")
        Board.__repr__(board)
    
    turnCounter += 1