# GUI: Graphic User Interface
#  https://www.youtube.com/watch?v=gQb3dE-y1S4
# assignment: watch the video above

# Algorithm: a group of rules or steps a computer follows to complete
# a task

board = [ "-", "-", "-"
        "-", "-", "-"
        "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True
    
# printing the game board 
def printBoard(board):
  
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5]) 
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# take player input
def player_input(board):
    inp = input(" Enter a number 1-9")
    if inp >= 1 and inp  <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer 
    else:
        print("Oops player is already in that stop!")


# check for win or tie
def checkhorizontle(board):
    global winner
    if board[0] == board[2]  and board[1] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return printBoard
     elif board[6] == board[7] == board[8] and board[6] != "-":

# switch the player

# check for win or tie again
