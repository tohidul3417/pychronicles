import random
import string
from collections import Counter

from words import words

def load_words():
    """
    Select a word from an imported list.

    Returns:
        str: The randomly chosen secret word.
    """
    return random.choice(words)

def display_words(word, guessed_letters):
    """
    Create a string representation of the secret word, showing guessed letters and underscores for missing letters.

    Args:
        word(str): The secret word.
        guessed_letters (set): A set of letters that have been guessed

    Returns:
        str: A string with correctly guessed letters revealed and underscores for letters not yet guessed
    """
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def get_valid_guess(guessed_letters):
    """
    Prompt for a valid guess that is a single, new, and enlgish alphabetical character.

    Args:
        guessed_letters (set): Letters already guessed

    Returns:
        str: A valid guessed letter
    """
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess in string.ascii_lowercase and guess not in guessed_letters:
            return guess
        print("Invalid input. Enter a single new letter")
    
def hangman():
    word = load_words() # Select a secret word
    guessed_letters = set() # Track guess word
    word_counter = Counter(word) # Count letters in word
    attempts = 6 # Allowed wrong attempts

    print("Welcome to Hangman!")

    while attempts > 0:
        print("\nWord:", display_words(word, guessed_letters))
        print(f"Attempts left: {attempts}")

        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word_counter:
            print("Good guess!")
            word_counter.subtract(guess)
            if all(count <= 0 for count in word_counter.values()):
                print("\nCongratulations! The word was:", word)
                return
        else:
            attempts -= 1
            print("Wrong Guess!")
    print("\nGame Over! The word was:", word)

if __name__ == "__main__":
    hangman()