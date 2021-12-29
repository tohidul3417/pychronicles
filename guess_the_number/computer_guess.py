import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    guess = random.randint(low, high)
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        if feedback == 'l':
            print(f'{guess} is too low, guess again!')
            low = low + 1
        elif feedback == 'h':
            print(f'{guess} is too high, guess again')
            high = high - 1
        elif feedback == 'c':
            print(f'{guess} is right. Computer WON!')
        else:
            print('Invalid input! Please enter H, L, or C')

computer_guess(30)