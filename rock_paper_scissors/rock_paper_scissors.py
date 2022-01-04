import random

CHOICES = ['r', 'p', 's']

def play():
    """Plays a round of Rock, Paper, and Scissors"""
    user = input("What's your choice? Enter 'r' for 'Rock', 'p' for 'Paper', and 's' for 'Scissors': ")

    if not user in CHOICES:
        return "Invalid choice! Please enter 'r', 'p', or 's'."
    
    computer = random.choice(CHOICES)
    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a tie"
    

    return "You won!" if did_player_win(user, computer) else "You lost!"
    

def did_player_win(player, opponent):
    """
    Determines if the player has won.
    Winning conditions:
    - Rock ('r') beats Scissors ('s')
    - Scissors ('s') beats Paper ('p')
    - Paper ('p') beats Rock ('r')
    """
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

if __name__ == "__main__":
    result = play()
    print(result)
