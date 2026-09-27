#game 1: Guessing game

import random

def guessinggame():
        num = random.randint(1,100)
        '''print(num) (uncomment this line to spoil number for testing)'''
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
if __name__ == "__main__":
    cont = 'Y'
    while cont == 'Y':
        guessinggame()
        cont = input("Do you want to play again? (Y/N): ")
