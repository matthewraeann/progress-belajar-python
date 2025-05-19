#19 Mei 2025

import os
from random import randint

def input_number(command:str) :
    while True :
        try :
            number = int(input(f'{command}: ').strip())
            return number
        except ValueError :
            print('\nPlease input an integers!')

def check(guess) :
    global chances_remaining,chances_used,fail
    chances_used += 1
    chances_remaining -= 1
    if guess == target_number :
        print(f'Congratulations you did it in {chances_used} try!')
        chances_remaining = 0
        fail = False
    else :
        fail = True
    if guess > target_number :
        print('You guessed to high!')
    if guess < target_number :
        print('You guessed to small!')

def check_playagain():
    while True :
        playagain = input('\nDo you want to play again? (y/n): ').lower().strip()
        if playagain in ['y','n'] :
            return playagain == 'y'
        else:
            print('Invalid input.\nPlease enter "y" for yes or "n" for no.')

os.system('cls' if os.name == 'nt' else 'clear')

print('\nGUESS THE NUMBER GAME')
while True :
    print('')
    while True :
        try : 
            lower_limit = input_number('Enter lower bound')
            upper_limit = input_number('Enter upper bound')
            target_number = randint(lower_limit,upper_limit)
            break
        except ValueError :
                print("\nThe upper bound can't be lower than the lower bound!")
                print('Please re-enter the bound!')

    while True :
        chances = input_number('Enter the maximum number of attemps')
        max_chances = (upper_limit-lower_limit+1)//2
        if chances < 1 :
            print("\nThe maximum number of attemps can't be lower than 1!")
        elif chances > max_chances :
            print(f"\nThe maximum number of attemps can't be higher than {max_chances}!")
        else :
            break

    chances_used = 0
    chances_remaining = chances

    print(f'\nYou have {chances} attempts to guess the integer between {lower_limit} and {upper_limit}!\n')

    while chances_remaining > 0:
        guess = input_number('Guess a number')
        check(guess)
    if fail :
        print(f'\nThe number was {target_number}.')
        print('Better lucky next time!')
    if not check_playagain() :
        break
print('\nTHANK YOU FOR PLAYING!\n')