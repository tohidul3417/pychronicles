"""
Tic Tac Toe Game
Classes:
    Board: Manages the game board state and logic
    Player: Represents a player in the game
    Game: Controls the game flow and coordinates players

Usage:
    Run this file directly to start the game:
    $ python tic_tac_toe/player.py
"""


class Board:
    """
    Represents the Tic Tac Toe game board.
    
    The board is implemented as a 3x3 grid where each cell can be:
    - None: Empty cell
    - 'X': Cell marked by the first player
    - 'O': Cell marked by the second player
    
    Attributes:
        cells (list): A 2D list representing the 3x3 game board
        moves_made (int): Counter for the number of moves made on the board
    """
    
    def __init__(self):
        """Initialize an empty 3x3 game board."""
        self.cells = [[None for _ in range(3)] for _ in range(3)]
        self.moves_made = 0
    
    def make_move(self, row, col, symbol):
        """
        Place a symbol on the board at the specified position.
        
        Args:
            row (int): Row index (0-2)
            col (int): Column index (0-2)
            symbol (str): Player symbol ('X' or 'O')
            
        Returns:
            bool: True if the move was successful, False if the position is
                 invalid or already occupied
        """
        # Validate coordinates are within board boundaries
        if not (0 <= row < 3 and 0 <= col < 3):
            return False
        
        # Check if the cell is already occupied
        if self.cells[row][col] is not None:
            return False
        
        # Place the symbol and increment the move counter
        self.cells[row][col] = symbol
        self.moves_made += 1
        return True

    def check_winner(self):
        """
        Check if there's a winner on the board.
        
        Examines all possible winning combinations (rows, columns, and diagonals)
        to determine if a player has won.
        
        Returns:
            str or None: The winning symbol ('X' or 'O') or None if no winner
        """
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
        """
        Check if the board is full (a draw).
        
        Returns:
            bool: True if all 9 cells are filled, False otherwise
        """
        return self.moves_made == 9
    
    def display(self):
        """
        Print the current state of the board to the console.
        
        Displays the board with row and column indices for reference.
        Empty cells are shown as dots, and filled cells show the player symbol.
        """
        print("\n 0 1 2")  # Column indices
        for i, row in enumerate(self.cells):
            print(f"{i}", end=" ")  # Row index
            for cell in row:
                if cell is None:
                    print(".", end=" ")  # Empty cell
                else:
                    print(cell, end=" ")  # Player symbol
            print()  # New line after each row
        print()  # Extra line after the board


class Player:
    """
    Represents a player in the Tic Tac Toe game.
    
    Attributes:
        symbol (str): The player's symbol ('X' or 'O')
        name (str): The player's name
    """
    
    def __init__(self, symbol, name=None):
        """
        Initialize a player with a symbol and optional name.
        
        Args:
            symbol (str): The player's symbol ('X' or 'O')
            name (str, optional): The player's name. If not provided,
                                 defaults to "Player X" or "Player O"
        """
        self.symbol = symbol
        self.name = name if name else f"Player {symbol}"
    
    def get_move(self, board):
        """
        Get the player's next move from user input.
        
        Prompts the player for row and column coordinates and validates
        the input format.
        
        Args:
            board (Board): The current game board (not used in this implementation
                          but might be useful for AI players in extensions)
            
        Returns:
            tuple: (row, col) coordinates for the player's move
        """
        while True:
            try:
                move = input(f"{self.name}'s turn ({self.symbol}). Enter row,col: ")
                row, col = map(int, move.split(","))
                return row, col
            except ValueError:
                print("Invalid input. Please enter row,col (e.g. 0,2)")


class Game:
    """
    Controls the flow of the Tic Tac Toe game.
    
    Manages the game board, players, and turn progression. Determines when
    the game ends and who wins.
    
    Attributes:
        board (Board): The game board
        players (list): List containing two Player objects
        current_player_idx (int): Index of the current player (0 or 1)
    """
    
    def __init__(self):
        """Initialize a new game with a board and two players."""
        self.board = Board()
        self.players = [
            Player('X'),
            Player('O')
        ]
        self.current_player_idx = 0  # Start with Player X

    def switch_player(self):
        """Switch to the other player for the next turn."""
        self.current_player_idx = 1 - self.current_player_idx

    @property
    def current_player(self):
        """
        Get the current player.
        
        Returns:
            Player: The current player object
        """
        return self.players[self.current_player_idx]

    def play(self):
        """
        Main game loop.
        
        Controls the flow of the game, including displaying the board,
        getting player moves, checking for game end conditions, and
        switching between players.
        """
        print("Welcome to Tic Tac Toe!")
        print("Enter moves as 'row,col' (e.g. 0,2 for top-right)")

        # Game loop
        while True:
            # Display the current state of the board
            self.board.display()

            # Get the current player's move
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
    """
    Main entry point of the program.
    
    Creates and runs the game, and handles the play again logic.
    """
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