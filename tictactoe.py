import random

def display_board(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1, please pick a marker 'X' or 'O': ").upper()
        if marker != 'X' and marker != 'O':
            print("Invalid input. Please pick 'X' or 'O'.")
    return marker

def place_marker(board, marker, position):
    board[position] = marker

def check_win(board, mark):
    return ((board[7] == board[8] == board[9] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[1] == board[2] == board[3] == mark) or
            (board[7] == board[4] == board[1] == mark) or
            (board[8] == board[5] == board[2] == mark) or
            (board[9] == board[6] == board[3] == mark) or
            (board[7] == board[5] == board[3] == mark) or
            (board[9] == board[5] == board[1] == mark))

def choose_first():
    first_player = random.randint(1, 2)
    return f"Player {first_player} goes first."

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return ' ' not in board[1:]

def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        try:
            position = int(input('Choose your next position: (1-9) '))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
    return position

def replay():
    return input("Do you want to play again? Enter 'Yes' or 'No': ").lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
    
    the_board = [' '] * 10
    player1_marker = player_input()
    if player1_marker == 'X':
        player2_marker = 'O'
    else:
        player2_marker = 'X'
    turn = choose_first()
    print(turn)

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if check_win(the_board, player1_marker):
                display_board(the_board)
                print('Congratulations! Player 1 has won the game!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
           
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if check_win(the_board, player2_marker):
                display_board(the_board)
                print('Congratulations! Player 2 has won the game!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
