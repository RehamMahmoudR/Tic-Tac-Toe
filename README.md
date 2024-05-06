# Tic-Tac-Toe

#### Description:

    This Tic-Tac-Toe game serves as the final project developed as a part of the CS50P course offered by Harvard University. It showcases the principles and concepts learned throughout the course, presenting a hands-on application of Python programming and game development.

- Initially, to play this game, run:
```
    pip install -r requirements.txt
    python tictactoe.py

```

- This is a minimalistic Tic-Tac-Toe game, meticulously designed for two players to engage in friendly competition.

- Currently, the game is tailored for multiplayer gameplay and does not include a single-player mode. Players can enjoy the game with a friend, family member, or anyone interested in a quick strategic showdown.

### Video Demo: https://youtu.be/xy99MtYvM1E
### Description:
__________________________

#### tictactoe.py

> The game at beginning
    - Asks the first player to choose a marker
    - The second player gets assigned the other marker based on what the first player chooses

> If the players are okay with the markers chosen, the game begins

> tabulate library is used to display the game board

> Players can alternatively place their markers on the board but the first play will be for the player with the "X" marker

> Whenever there are consecutive 3 markers "X" or "O" placed, diagonally or horizontally or vertically, the game declares the player with the 3 markers as the winner

> If there are no three consecutive markers placed even after the entire board is filled, the game will be declared as a tie

> After each set of the game, players will be shown their points

> The game ends when one player wins or it's a draw. It's a simple and strategic game enjoyed by all ages.

### Unit tests
___________________________
*Used to check whether all the functions in the code are working as expected*

#### test_tictactoe.py

- To ensure the robustness, reliability, and accuracy of the game's functionalities, a series of unit tests have been diligently implemented and integrated into the game's development process.



> test_full_board_check()
    - used to check if there is any space left in the game board

> test_choose_first()
    - used to choose which player goes first

> test_space_check()
    - used to check if the specified position is free to insert marker

> test_marker_position()
    - used to check if the specified marker position is within the range of 1 to 10

### Game Features:
    Simplicity & Strategy:
    This Tic-Tac-Toe game is designed to be both simple and strategic, making it enjoyable for players of all ages.
