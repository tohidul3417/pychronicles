import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board(width, height, num_mines):
    # Create an empty board
    board = [['0' for _ in range(width)] for _ in range(height)]
    
    # Place mines randomly
    mines_placed = 0
    while mines_placed < num_mines:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        
        if board[y][x] != 'M':
            board[y][x] = 'M'
            mines_placed += 1
    
    # Calculate numbers for adjacent cells
    for y in range(height):
        for x in range(width):
            if board[y][x] == 'M':
                continue
            
            # Count adjacent mines
            count = 0
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < width and 0 <= ny < height and board[ny][nx] == 'M':
                        count += 1
            
            board[y][x] = str(count)
    
    return board

def display_board(board, revealed, width, height, game_over=False):
    clear_screen()
    
    print("MINESWEEPER - 5x5 - 4 mines")
    print("Type: A1 (reveal) | h (help) | q (quit)")
    
    # Print column headers (A, B, C, etc.)
    print("  ", end="")
    for x in range(width):
        print(f"{chr(65 + x)}", end=" ")
    print()
    
    # Print rows with numbers (1, 2, 3, etc.)
    for y in range(height):
        print(f"{y + 1} ", end="")
        
        for x in range(width):
            if game_over and board[y][x] == 'M':
                print("M", end=" ")
            elif revealed[y][x]:
                print(board[y][x], end=" ")
            else:
                print(".", end=" ")
        print()

def show_help():
    clear_screen()
    print("MINESWEEPER HELP")
    print("Goal: Reveal all safe cells without hitting mines")
    print("Numbers show mines in adjacent cells")
    print("Legend: . (hidden) | 0-8 (safe) | M (mine)")
    print("Standard notation: A1, B3, etc (column + row)")
    print("Commands: A1 | h (help) | q (quit)")
    input("Press Enter to return...")

def parse_coordinates(move, width, height):
    if len(move) < 2:
        return None
    
    # First character should be a letter (column)
    col_char = move[0].upper()
    if not ('A' <= col_char <= chr(64 + width)):
        return None
    
    # Rest should be a number (row)
    try:
        row = int(move[1:])
        if not (1 <= row <= height):
            return None
    except ValueError:
        return None
    
    # Convert to 0-based indices
    x = ord(col_char) - 65  # A=0, B=1, etc.
    y = row - 1             # 1=0, 2=1, etc.
    
    return (x, y)

def play_game():
    # Game settings
    width = 5
    height = 5
    num_mines = 4
    
    # Create the game board
    board = create_board(width, height, num_mines)
    revealed = [[False for _ in range(width)] for _ in range(height)]
    game_over = False
    
    total_safe_cells = width * height - num_mines
    revealed_count = 0
    
    # Main game loop
    while not game_over:
        display_board(board, revealed, width, height)
        
        # Get user input
        move = input("> ").lower().strip()
        
        if move == 'q':
            return
        
        if move == 'h':
            show_help()
            continue
        
        # Parse coordinates like "A1", "B3", etc.
        coords = parse_coordinates(move, width, height)
        if coords:
            x, y = coords
            
            if revealed[y][x]:
                continue
            
            # Reveal the cell
            revealed[y][x] = True
            
            # Check if mine was hit
            if board[y][x] == 'M':
                game_over = True
                print("BOOM! Game over!")
            else:
                revealed_count += 1
                
                # Auto-reveal adjacent cells if the revealed cell has no adjacent mines
                if board[y][x] == '0':
                    queue = [(x, y)]
                    while queue:
                        cx, cy = queue.pop(0)
                        for dy in [-1, 0, 1]:
                            for dx in [-1, 0, 1]:
                                nx, ny = cx + dx, cy + dy
                                if (0 <= nx < width and 0 <= ny < height and 
                                    not revealed[ny][nx]):
                                    revealed[ny][nx] = True
                                    if board[ny][nx] != 'M':
                                        revealed_count += 1
                                    if board[ny][nx] == '0':
                                        queue.append((nx, ny))
                
                # Check for win
                if revealed_count == total_safe_cells:
                    game_over = True
                    print("You win!")
    
    # Show final board
    display_board(board, revealed, width, height, game_over=True)
    input("Game over. Press Enter to exit...")

if __name__ == "__main__":
    clear_screen()
    print("MINESWEEPER - 5x5 grid with 4 mines")
    print("Use standard notation: A1, B3, etc.")
    print("Type 'h' for help during the game")
    input("Press Enter to start...")
    
    play_game()