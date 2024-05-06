from pyfiglet import Figlet
from tabulate import tabulate

def main():
    POINT = [0, 0]
    figlet = Figlet()
    figlet.setFont(font="slant")
    print(figlet.renderText("Tic-Tac-Toe"))

    try:
        while True:
            boardgame = [" "]*10

            player1, player2 = player_input()
            turn = choose_first(player1)
            print("\n" + turn + " goes first")

            play_game = input('\nLets play the game? (Y or N): ')
            game_on = play_game.upper() == 'Y'

            while game_on:
                table = [["Player", "Point"]]

                if turn == "Player 1":
                    display_board(boardgame)
                    position = player_choice(boardgame)
                    place_marker(boardgame, player1, position)

                    if win_check(boardgame, player1):
                        display_board(boardgame)
                        POINT[0] += 1
                        print('Player 1 has WON the game!\n')
                        game_on = False
                    elif full_board_check(boardgame):
                        display_board(boardgame)
                        print('Well played, ended up as a tie!\n')
                        game_on = False
                    else:
                        turn = 'Player 2'
                else:
                    display_board(boardgame)
                    position = player_choice(boardgame)
                    place_marker(boardgame, player2, position)

                    if win_check(boardgame, player2):
                        display_board(boardgame)
                        POINT[1] += 1
                        print('Player 2 has WON the game!\n')
                        game_on = False
                    elif full_board_check(boardgame):
                        display_board(boardgame)
                        print('The game has been TIED!\n')
                        game_on = False
                    else:
                        turn = 'Player 1'

                if not game_on:
                    table.append(["P1", POINT[0]])
                    table.append(["P2", POINT[1]])
                    print(tabulate(table, headers="firstrow", tablefmt="grid"))
                print()

            if not replay():
                break

    except (EOFError, KeyboardInterrupt):
        print("\n\nAww! We are sad you left early🥲.")
    else:
        print("\n", tabulate([["Thank you for playing Tic-Tac-Toe!"]], tablefmt="grid"), "\n")

def display_board(board):
    print('\n'*100)
    table = [[board[1], board[2], board[3]], [board[4], board[5], board[6]], [board[7], board[8], board[9]]]
    print(tabulate(table, tablefmt="grid"))
    print("\n\n")

def player_input():
    pmark = input('Choose your marker (X or O): ').upper()
    table = [["Player", "Marker"]]

    while pmark.upper() not in ('X', 'O'):
        print('Sorry! Invalid marker chosen.')
        pmark = input('Choose your marker (X or O): ')

    table.append(["P1", pmark])

    if pmark.upper() == 'X':
        table.append(["P2", "O"])
        return 'X', 'O'
    else:
        table.append(["P2", "X"])
        return 'O', 'X'

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, marker):
    return (
        (board[1] == board[2] == board[3] == marker) or
        (board[4] == board[5] == board[6] == marker) or
        (board[7] == board[8] == board[9] == marker) or
        (board[1] == board[5] == board[9] == marker) or
        (board[3] == board[5] == board[7] == marker) or
        (board[1] == board[4] == board[7] == marker) or
        (board[2] == board[5] == board[8] == marker) or
        (board[3] == board[6] == board[9] == marker)
    )

def choose_first(player1):
    return f"Player {1 if player1 == 'X' else 2}"

def space_check(board, position):
    return board[position] == " "

def full_board_check(board):
    return " " not in board[1:]

def player_choice(board):
    while True:
        try:
            a = int(input('Enter your next position: '))
            if 1 <= a <= 9 and space_check(board, a):
                return a
            else:
                print('Invalid position entered or position is not empty\n')
        except ValueError:
            print("Invalid position entered\n")

def replay():
    replay = input('Would you like to play again by changing the markers? (Y or N): ')
    return replay.upper() == 'Y'

if __name__ == "__main__":
    main()

