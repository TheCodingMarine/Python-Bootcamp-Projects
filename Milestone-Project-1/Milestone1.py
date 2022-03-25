"""Milestone project for 2022 Complete Python Bootcamp From Zero to Hero in Python, instructor: Jose Portilla
    of Pierian Data Inc.
    Coded by Tyler Miller, 9 January 2022"""
"""Changed from string parsing to boolean logic in turn function and game loop, per recommendation from mentor
    9 January 2022"""
"""Test change for git"""


import random


def player_marker_select():
    """Function allowing selection of player board markers"""
    global player_1_marker  # global variables used for universality
    global player_2_marker
    player_mark = input("Player 1, please select X's or O's: ")
    if player_mark == 'x' or player_mark == 'X':
        player_1_marker = 'X'
        player_2_marker = 'O'
    else:
        player_1_marker = 'O'
        player_2_marker = 'X'
    print("Player 1 is: ", player_1_marker)
    print("Player 2 is: ", player_2_marker)


def first_turn():
    """Function using random integer generation to choose who will go first."""
    if random.randint(0, 1) == 0:
        return True
    else:
        return False


def game_board(board):
    """Displays game board onscreen. List argument for board position assignment using list indexing"""
    print(board[7], ' | ', board[8], '| ', board[9])
    print('--', '|', '--', '|', '--')
    print(board[4], ' | ', board[5], '| ', board[6])
    print('--', '|', '--', '|', '--')
    print(board[1], ' | ', board[2], '|', board[3])


def check_spaces(board, lst):
    """Function to check board position list for empty spaces."""
    return board[lst] == ' '


def check_board(board):
    """Takes board position list and iterates over it with the check_spaces function. If no spaces are left
        game is then declared a draw by returning false. Else game proceeds."""
    for i in range(1, 10):
        if check_spaces(board, i):
            return False
    return True


def win_condition(lst, marker):
    """"""
    return ((lst[7] == marker and lst[8] == marker and lst[9] == marker) or  # across
            (lst[4] == marker and lst[5] == marker and lst[6] == marker) or  # across
            (lst[1] == marker and lst[2] == marker and lst[3] == marker) or  # across
            (lst[1] == marker and lst[5] == marker and lst[9] == marker) or  # diagonal
            (lst[3] == marker and lst[5] == marker and lst[7] == marker) or  # diagonal
            (lst[1] == marker and lst[4] == marker and lst[7] == marker) or  # horizontal
            (lst[2] == marker and lst[5] == marker and lst[8] == marker) or  # horizontal
            (lst[3] == marker and lst[6] == marker and lst[9] == marker))  # horizontal


def move_player1(lst):
    """Function for determining player 1 move. Takes in board positions list as argument. Asks for player input inside
        of a while loop. Checks player choice against list of positions to see if chosen space is occupied.
        If space is occupied, passes back to beginning of loop, otherwise assigns player marker to positions list
        using reassignment via list indexing"""
    moving = True
    while moving:
        player1move = int(input("Player 1: "))
        if lst[player1move] == "X" or lst[player1move] == "O":
            print("Please choose another move.")
            pass
        else:
            moving = False
    lst[player1move] = player_1_marker


def move_player2(lst):
    """Function for determining player 2 move. Takes in board positions list as argument. Asks for player input inside
            of a while loop. Checks player choice against list of positions to see if chosen space is occupied.
            If space is occupied, passes back to beginning of loop, otherwise assigns player marker to positions list
            using reassignment via list indexing"""
    moving = True
    while moving:
        player2move = int(input("Player 2: "))
        if lst[player2move] == "X" or lst[player2move] == "O":
            print("Please choose another position.")
            pass
        else:
            moving = False
    lst[player2move] = player_2_marker


def replay():
    """Simple function asking if players would like to play again."""
    return input('Would you like to play again? Enter Yes or No: ').lower().startswith('y')


while True:  # main program loop
    position = [' '] * 10  # board position list used to track player choices and display via game_board()
    player_marker_select()
    turn = first_turn()  # assigning first turn to local variable
    if turn == True:
        print("Player 1 will go first.")
    else:
        print("Player 2 will go first.")

    play_game = input("Are you ready to play: ")  # boolean setting game state for game loop
    if play_game.lower()[0] == 'y':
        playing = True
    else:
        playing = False

    while playing:  # game loop

        if turn:  # conditional encompassing player 1's turn
            game_board(position)  # displays game board on screen
            move_player1(position)  # takes player movement
            if win_condition(position, player_1_marker):  # checks for winning condition
                game_board(position)
                print("You win!")
                playing = False  # breaks out of game loop
            else:  # if not a winning condition, checks for draw
                if check_board(position):
                    game_board(position)
                    print("Draw!")
                    break  # if draw, breaks out of game loop
                else:
                    turn = False  # if neither draw nor win, sets to player 2's turn

        else:  # conditional encompassing player 2's turn
            game_board(position)  # displays game board
            move_player2(position)  # takes player movement
            if win_condition(position, player_2_marker):  # checks of winning condition
                game_board(position)  # displays board
                print("You win!")
                playing = False  # breaks out of game loop
            else:
                if check_board(position):  # if not winning condition, checks of draw
                    game_board(position)
                    print("Draw!")
                    break  # if draw, breaks out of game loop
                else:
                    turn = True  # if neither draw nor win, sets player 1 turn

    if not replay():  # after win or draw, asks for replay state
        break  # if replay not desirable, breaks out of main loop and ends program
