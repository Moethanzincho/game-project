#game 1: Guessing game

import random

'''Guessing game function that generates a random number between 1 and 100.
   Gives the user 5 attempts to guess what number it is.
   After each guess, it gives feedback to the user on whether their guess was higher or lower than the random number.
   After either guessing the correct number or guessing 5 times incorrectly, the user is met with a congrats message or a lose message revealing the number respectively.
   The user can choose to keep playing this game using Y/N,running the function again if the user chooses Y, ending the loop if the user chooses N.
   Author: Milo Stretton'''
def guessing_game():
        num = random.randint(1,100)
        guess = int(input("I'm thinking of a number between 1 and 100.\nGuess what it is. You have 5 tries: "))
        num_of_guesses = 4
        while guess != num and (num_of_guesses >= 1):
            if guess > num:
                guess = int(input(f"Nope! Too high. Try again ({num_of_guesses} tries left): " if num_of_guesses > 1 else f"Nope! Too high. Try again (1 try left): "))
                num_of_guesses -= 1
            else:
                guess = int(input(f"Nope! Too low. Try again ({num_of_guesses} tries left): " if num_of_guesses > 1 else f"Nope! Too low. Try again (1 try left): "))
                num_of_guesses -= 1
        if guess != num:
            print("Nope! You lost. The number was",num)
        else:
            print("You got it!")
'''Runs the function and the loop that asks if the user wishes to continue playing the game
   Author: Milo Stretton'''
if __name__ == "__main__":
    cont = 'Y'
    while cont == 'Y':
        guessing_game()
        cont = input("Do you want to play again? (Y/N): ")
