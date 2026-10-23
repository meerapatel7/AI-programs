import random

board = [" " for _ in range(9)]

HUMAN = "X"
COMPUTER = "O"

WINNING_POSITIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

def display_board():
    print("\n")
    print("     |     |")
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}")
    print("_____|_____|_____")
    print("     |     |")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}")
    print("_____|_____|_____")
    print("     |     |")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}")
    print("     |     |")
    print()

def check_winner(player):
    for a, b, c in WINNING_POSITIONS:
        if board[a] == player and board[b] == player and board[c] == player:
            return True
    return False

def heuristic(player):
    opponent = "O" if player == "X" else "X"
    score = 0

    for a, b, c in WINNING_POSITIONS:
        line = [board[a], board[b], board[c]]

        # Three player's symbols
        if line.count(player) == 3:
            score += 100

        # Two player's symbols and one empty
        elif line.count(player) == 2 and line.count(" ") == 1:
            score += 10

        # One player's symbol and two empty
        elif line.count(player) == 1 and line.count(" ") == 2:
            score += 1

        # Opponent has a winning opportunity
        if line.count(opponent) == 2 and line.count(" ") == 1:
            score -= 10

    # Center position is valuable
    if board[4] == player:
        score += 3

    # Corners are slightly valuable
    for corner in (0, 2, 6, 8):
        if board[corner] == player:
            score += 1

    return score

def display_heuristic():
    x_score = heuristic("X")
    o_score = heuristic("O")

    print("--------------------------------")
    print("        HEURISTIC VALUES")
    print("--------------------------------")
    print("You (X) Score     :", x_score)
    print("Computer (O) Score:", o_score)

    if x_score > o_score:
        print("Current board advantage: You (X)")
    elif o_score > x_score:
        print("Current board advantage: Computer (O)")
    else:
        print("Current board evaluation: Balanced")
    print("--------------------------------")

def is_draw():
    return " " not in board

def get_human_move():
    while True:
        try:
            position = int(input(f"Your turn ({HUMAN}), enter position (1-9): "))

            if position < 1 or position > 9:
                print("Enter a number between 1 and 9.")
                continue

            index = position - 1

            if board[index] != " ":
                print("That position is already occupied.")
                continue

            board[index] = HUMAN
            break

        except ValueError:
            print("Please enter a valid number.")

def get_computer_move():
    best_score = None
    best_moves = []

    for i in range(9):
        if board[i] != " ":
            continue

        # Try the move
        board[i] = COMPUTER

        # Evaluate: computer's heuristic minus the human's heuristic
        score = heuristic(COMPUTER) - heuristic(HUMAN)

        # Undo the move
        board[i] = " "

        if best_score is None or score > best_score:
            best_score = score
            best_moves = [i]
        elif score == best_score:
            best_moves.append(i)

    move = random.choice(best_moves)   # break ties randomly
    board[move] = COMPUTER
    print(f"Computer ({COMPUTER}) chooses position {move + 1}")

def play_game():
    current_player = HUMAN

    print("=" * 50)
    print("       USER vs COMPUTER TIC-TAC-TOE")
    print("       USING HEURISTIC FUNCTION")
    print("=" * 50)
    print(f"\nYou are {HUMAN}. Computer is {COMPUTER}.")

    print("\nBoard Positions:")
    print()
    print("  1  |  2  |  3")
    print("-----|-----|-----")
    print("  4  |  5  |  6")
    print("-----|-----|-----")
    print("  7  |  8  |  9")

    while True:
        display_board()

        if current_player == HUMAN:
            get_human_move()
        else:
            get_computer_move()

        # Show board after move
        display_board()

        # Show heuristic values
        display_heuristic()

        # Check winner
        if check_winner(current_player):
            print("\n" + "=" * 50)
            if current_player == HUMAN:
                print("        YOU WIN!")
            else:
                print("        COMPUTER WINS!")
            print("=" * 50)
            print("Final Heuristic Score:", heuristic(current_player))
            break

        # Check draw
        if is_draw():
            print("\n" + "=" * 50)
            print("              GAME DRAW")
            print("=" * 50)
            break

        # Switch player
        current_player = COMPUTER if current_player == HUMAN else HUMAN

play_game()
