#PRINTING OUT A BOARD
from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print(board[7]+"|"+board[8]+"|"+board[9])
    print(board[4]+"|"+board[5]+"|"+board[6])
    print(board[1]+"|"+board[2]+"|"+board[3])

def player_input():
    ask=""
    while ask!="X" and ask!="O":
        ask=input("Player 1, would you like to be X or O: ")
        if ask=="X":
            player1 = "X"
            player2 = "O"
        else:
            player1 = "O"
            player2 = "X"
    return(player1,player2)

#TAKES IN AN INPUT AND REPLACES THE BOARD
def place_marker(board, marker, position):
    board[position]= marker

# DIFFERENT WAYS TO WIN
def win_check(board,mark):
    if mark==board[1]==board[2]==board[3] or mark==board[4]==board[5]==board[6] or mark==board[7]==board[8]==board[9] or mark==board[1]==board[4]==board[7] or mark==board[2]==board[5]==board[8] or (mark==board[3]==board[6]==board[9]) or mark==board[1]==board[5]==board[9] or mark==board[7]==board[5]==board[3]:
        return(True)
    else:
        return(False)

def choose_first():
    goesfirst=random.randint(0,1)
    if goesfirst==0:
        return("Player 1 will go first.")
    else:
        return("Player 2 will go first.")

def space_check(board, position):
    return(board[position]=="   ")

def full_board_check(board):
    for x in range(1,10):
        if space_check(board, x):
            return(False)
    return(True)

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position from spaces 1-9: '))
        
    return position

def replay():
    again=input("Do you want to play again? Yes or No")
    return(again=="Yes")

#GAMEPLAY
print('Welcome to Tic Tac Toe!')

while True:
    gameBoard=['#','   ','   ','   ','   ','   ','   ','   ','   ','   ']
    p1,p2=player_input()
    turn = choose_first()
    print(turn + " will go first!")
    
    play_game=input("Ready to start? Yes or No")
    if play_game=="Yes":
        game_on=True
    else:
        game_on=False
        
    while game_on:
        # PLAYER 1 TURN
        if turn == "Player 1":
        #SHOW BOARD, ASK FOR CHOICE, CHECK FOR WIN
            display_board(gameBoard)
            position = player_choice(gameBoard)
            place_marker(gameBoard, p1, position)
            if win_check(gameBoard, p1):
                display_board(gameBoard)
                print("Player 1 WINS!")
                game_on=False
            else:
                if full_board_check(gameBoard):
                    display_board(gameBoard)
                    print("TIE GAME.")
                    game_on=False
                else:
                    turn = "Player 2"
                    
        else:
            display_board(gameBoard)
            position = player_choice(gameBoard)
            place_marker(gameBoard, p2, position)
            if win_check(gameBoard, p2):
                display_board(gameBoard)
                print("Player 2 WINS!")
                game_on=False
            else:
                if full_board_check(gameBoard):
                    display_board(gameBoard)
                    print("TIE GAME.")
                    game_on=False
                else:
                    turn = "Player 1"
    replay()
    if not replay():
        break