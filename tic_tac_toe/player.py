class Board:
    def __init__(self):
        self.cells = [[None for _ in range(3)] for _ in range(3)]
        self.moves_made = 0
    
    def make_move(self, row, col, symbol):
        if not (0 <= row < 3 and 0 <= col < 3):
            return False
        
        if self.cells[row][col] is not None:
            return False
        
        self.cells[row][col] = symbol
        self.moves_made += 1
        return True

    def check_winner(self):
        # Check rows
        for row in self.cells:
            if (row[0] is not None and row[0] == row[1] == row[2]):
                return row[0]
        
        # Check columns
        for col in range(3):
            if (self.cells[0][col] is not None and
                self.cells[0][col] == self.cells[1][col] == self.cells[2][col]):
                return self.cells[0][col]
            
        # Check diagonals
        if (self.cells[0][0] is not None and
            self.cells[0][0] == self.cells[1][1] == self.cells[2][2]):
            return self.cells[0][0]
        
        if (self.cells[0][2] is not None and
            self.cells[0][2] == self.cells[1][1] == self.cells[2][0]):
            return self.cells[0][2]
        
        return None
    
    def is_full(self):
        # Check if the board is full (a draw)
        return self.moves_made == 9
    
    def display(self):
        print("\n 0 1 2")
        for i, row in enumerate(self.cells):
            print(f"{i}", end=" ")
            for cell in row:
                if cell is None:
                    print(".", end=" ")
                else:
                    print(cell, end=" ")
            print()
        print()


class Player:
    def __init__(self, symbol, name=None):
        self.symbol = symbol
        self.name = name if name else f"Player {symbol}"
    
    def get_move(self, board):
        while True:
            try:
                move = input(f"{self.name}'s turn ({self.symbol}). Enter row,col: ")
                row, col = map(int, move.split(","))
                return row, col
            except ValueError:
                print("Invalid input. Please enter row,col (e.g. 0,2)")


class Game():
    def __init__(self):
        self.board = Board()
        self.players = [
            Player('X'),
            Player('O')
        ]
        self.current_player_idx = 0

    def switch_player(self):
        self.current_player_idx = 1 - self.current_player_idx

    @property
    def current_player(self):
        return self.players[self.current_player_idx]

    def play(self):
        print("Welcome to Tic Tac Toe!")
        print("Enter moves as 'row,col' (e.g. 0,2 for top-right)")

        # Game loop
        while True:
            self.board.display()

            player = self.current_player
            row, col = player.get_move(self.board)

            # Make the move
            if not self.board.make_move(row, col, player.symbol):
                print("Invalid move. Try again.")
                continue

            # Check for win
            winner = self.board.check_winner()
            if winner:
                self.board.display()
                print(f"{player.name} wins!")
                break

            # Check for draw
            if self.board.is_full():
                self.board.display()
                print("It's a draw!")
                break
            
            # Switch player for next turn
            self.switch_player()


def main():
    """Main entry point of the program"""
    game = Game()
    game.play()

    # Ask to play again
    while True:
        play_again = input("Play again? (y/n): ").lower()
        if play_again == 'y':
            game = Game()
            game.play()
        elif play_again == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()