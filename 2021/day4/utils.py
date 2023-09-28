import copy


# Game State Class
class BingoGame(object):
    data = None
    numbers = []
    picked_numbers = []
    game_boards = []
    winners = []
    marker = "X"

    # Prepare the game data
    def __init__(self, data):
        self.data = data
        self.numbers = [int(item) for item in self.data.pop(0).split(",")]
        self.data.remove("")

        game_board = []
        for game_board_row in self.data:
            if game_board_row == "":
                self.game_boards.append(game_board)
                game_board = []
                continue
            game_board.append([int(item) for item in game_board_row.split()])

        self.game_boards.append(game_board)

    # Print a single game board (for debugging)
    def print_board(self, board):
        for row in board:
            for item in row:
                if len(str(item)) == 1:
                    print(f" {item}", end="")
                else:
                    print(item, end="")
                print(" ", end="")
            print()

    # Print the numbers and game boards (for debugging)
    def print_game(self):
        if self.picked_numbers:
            print(
                "Picked Numbers:",
                ", ".join(str(item) for item in self.picked_numbers),
                "\n",
            )

        if self.numbers:
            print(
                "Numbers Remaining:",
                ", ".join(str(item) for item in self.numbers),
                "\n",
            )

        print("Game Boards:")
        for i, game_board in enumerate(self.game_boards):
            if not any(
                winner.get("game_board_number") == i + 1 for winner in self.winners
            ):
                self.print_board(game_board)
                if i != len(self.game_boards) - 1:
                    print()

    # Pick the next number and return it
    def pick_number(self):
        number = self.numbers.pop(0)
        self.picked_numbers.append(number)
        return number

    # Update game boards
    def update_game_boards(self, number):
        for i in range(len(self.game_boards)):
            if not any(
                winner.get("game_board_number") == i + 1 for winner in self.winners
            ):
                for j in range(len(self.game_boards[i])):
                    for k, item in enumerate(self.game_boards[i][j]):
                        if item == number:
                            self.game_boards[i][j][k] = self.marker

    # Get the score for a board
    def get_score(self, board):
        unmarked_total = 0

        for row in board:
            for item in row:
                if item != self.marker:
                    unmarked_total += item

        return unmarked_total * self.picked_numbers[-1]

    # Check a board to see if it is a winner
    def check_winner(self, board):
        # Check rows
        for row in board:
            if all(item == row[0] for item in row):
                return True

        # Check columns
        for col in range(len(board)):
            if all(row[col] == self.marker for row in board):
                return True

    # Check all boards for winners
    def get_winners(
        self,
    ):
        for i, game_board in enumerate(self.game_boards):
            if not any(
                winner.get("game_board_number") == i + 1 for winner in self.winners
            ) and self.check_winner(game_board):
                self.winners.append(
                    {
                        "game_board_number": i + 1,
                        "game_board": copy.deepcopy(game_board),
                        "winning_number": self.picked_numbers[-1],
                        "score": self.get_score(game_board),
                    }
                )

        return self.winners

    # Print game winner information (for debugging)
    def print_winner(self, winner):
        board_number = winner["game_board_number"]
        winning_number = winner["winning_number"]
        print(f"Game board {board_number} won with number {winning_number}!\n")
        self.print_board(winner["game_board"])
        print()
        print(f"Score: {winner['score']}")

    # Run the game
    def play(self, first_winner_ends_game=True):
        while len(self.winners) < len(self.game_boards):
            number = self.pick_number()
            self.update_game_boards(number)
            self.get_winners()

            if self.winners and first_winner_ends_game:
                break

        if self.winners:
            print(self.winners[-1]["score"])
        else:
            print("There were no winners :(")
