import random

def user_guess(x):
    secret_number = random.randint(1, x)
    guess = 0
    while guess != secret_number:
        guess = input(f'Guess a number between 0 and {x}: ')
        guess = int(guess)
        print(f'You guessed {guess}.')

        if guess > x:
            print(f'Only choose number less than {x}')
        elif guess < 1:
            print('Only choose number greater than 0')
        else:
            print('That is wrong! Guess again!')
    print(f'YOU WON! {secret_number} is the secret number.')
    
user_guess(10)

