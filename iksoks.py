from IPython.display import clear_output

def display_board(board):
    clear_output()
    print (board[7] + "|" + board[8] + "|" + board[9])
    print (board[4] + "|" + board[5] + "|" + board[6])
    print (board[1] + "|" + board[2] + "|" + board[3])

def player_input():
    marker = ""
    while not (marker == "X" or marker == "O"):
        marker = input("Choose X or O!").upper()
    if marker == "X":
        return ("X","O")
    else:
        return ("X","O")

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    if (board[1] == board[2] == board[3] == mark):
        return True
    elif (board[4] == board[5] == board[6] == mark):
        return True
    elif (board[7] == board[8] == board[9] == mark):
        return True
    elif (board[1] == board[2] == board[3] == mark):
        return True
    elif (board[1] == board[4] == board[7] == mark):
        return True
    elif (board[2] == board[5] == board[8] == mark):
        return True
    elif (board[3] == board[6] == board[9] == mark):
        return True
    elif (board[1] == board[5] == board[9] == mark):
        return True
    elif (board[3] == board[5] == board[7] == mark):
        return True
    else:
        return False

import random

def choose_first():
    
    player = random.randint(0, 1)
    
    if player == 0:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board, position):
    if board[position] == " ":
        return True
    else:
        return False

def full_board_check(board):
    if (board[1] != " " and board[2] != " " and board[3] != " " and board[4] != " " and board[5] != " " and board[6] != " " and board[7] != " " and board[8] != " " and board[9] != " "):
        return True
    else:
        return False

def player_choice(board):
    
    position = 0
    
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input("Choose a position from 1 - 9!"))
        
    return position

def replay():
    
    marker = input("Do you want to play again?")
    
    if marker == "yes":
        return True
    else:
        return False

print("Welcome to Tic Tac Toe!")

while True:
    
    board = [" "]*10
    
    player1,player2 = player_input()
    
    turn = choose_first()
    
    print (turn + " will go first!")

    play_game = input("Ready to play, yes or no?")
    
    if play_game == "yes":
        game_on = True
    else:
        game_on = False
        
    while game_on:
            
            if turn == "Player 1":
                
                display_board(board)
                position = player_choice(board)
                place_marker(board,player1,position)
                
                if win_check(board,player1):
                    print("Player 1 wins!!!")
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print("Its a tie!!!")
                        game_on = False
                    else:
                        turn = "Player 2"
            else:
                display_board(board)
                position = player_choice(board)
                place_marker(board,player2,position)
                
                if win_check(board,player2):
                    print("Player 2 wins!!!")
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print("Its a tie!!!")
                        game_on = False
                    else:
                        turn = "Player 1"
    if not replay():
        break