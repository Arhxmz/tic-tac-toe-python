# Name : Muhammad Arham Hassan
# Roll no : 281133984
# Programming II (A)
# Title  ' Tic Tac Toe '
# date : 6 march 2025


import random

board = [ '-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']              
       # player 'X' will start the game   
winner = None               # no winner yet
gamerunning = True           # Game is active & should continue

#printing board for the game 
choose_mode = input("Enter the mode (1 for single-player, 2 for two-player & Q for quitting the game ): ")



if choose_mode.upper() == 'Q':
    print("Thanks for playing!") # for quitting the game
    exit()

def printBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 9)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 9)
    print(board[6] + " | " + board[7] + " | " + board[8])
print('lets toss')
toss=random.randint(0,1)
if toss == 1:
    print('X won the toss')
    current_player='X'
else:
    print('O won the toss')
    current_player= 'O' 

# prints the board elements & separate each row with dashes

#take player input
def player_Input():
    turn = int(input(f"Player {current_player}, Enter a spot (1-9): "))
    if board[turn-1] == "-":                     # checking for empty slot  
        #and turn-1 adjust the list indexing as game board has 0 to 8 index but input is 1-9
        board[turn-1] = current_player         
    else:
        print("Invalid input or spot already taken. Try again.")



def computer_move(): 
    available_spots = []
    for i, spot in enumerate(board):         # gives both index and value at that index
        if spot == "-":
            available_spots.append(i)     # if spot is empty its added to available spot
    if available_spots:
        move = random.choice(available_spots)    # picking a random spot 
        board[move] = 'O'

# checking  for win 
def checkwin():
    global winner
    win_conditions = [(0,1,2), (3,4,5), (6,7,8),  # Rows
                       (0,3,6), (1,4,7), (2,5,8),  # Columns
                       (0,4,8), (2,4,6)]           # Diagonals
    
    for condition in win_conditions:
        a, b, c = condition                                          # variables which are basically indexes
        if board[a] == board[b] == board[c] and board[a] != '-':     # checking if three board positions are same
            winner = board[a] 
            return True
    return False     

def checkTie():
    global gamerunning
    if '-' not in board and winner is None:         # when no empty slot left
        printBoard()
        print("It's a tie!")
        gamerunning = False

#switching the player
def switch_player():
    global current_player
    current_player = 'O' if current_player == 'X' else 'X' 


while gamerunning:
    printBoard()
    if winner or '-' not in board:      
        break
    
    if choose_mode == '1' and current_player == 'O':   # mode 1 is computer mode
        computer_move()
    else:
        player_Input()
    
    if checkwin():   # if winner is decided then checkwin function will break
        break
    checkTie()
    switch_player()

printBoard()
if winner:
    print(f'Winner is {winner}')
else:
    print("It's a tie!")
