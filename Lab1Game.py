"""Lab 1
Group #: 3
Authors: Milo Stretton, Moe Cho, Julia Ueligitone
Date: September 27, 2026 """


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



# Game 2: Rock, Paper, Scissors

import random

def rock_paper_scissors():
  """Runs a single round of Rock, Paper, Scissors against a computer opponent.
  The user will choose (Y/N) to begin the game. 
  The user will input a number between 1 and 3, then a random choice will be generated
   by the computer and determine a winner or draw. 
   The results will be printed and prompt the user to play again. 
   Authors: Julia Ueligitone"""
  user_choice =int(input("Enter your choice: 1. paper, 2. scissors, 3. rock:"))
  if user_choice < 1 or user_choice > 3:
      print("Invalid choice! Choose 1, 2, or 3")
      return
  computer_choice = random.randint(1, 3)

  if user_choice == computer_choice: 
    print("It is a tie!")
  elif (user_choice == 1 and computer_choice == 3) or \
       (user_choice == 2 and computer_choice == 1) or \
       (user_choice == 3 and computer_choice == 2):
    print("You win!")
  else:
    print("Computer wins!")


        #main.py

def choose_game():
    """Displays game menu inside a loop and ask the player to choose Game 1 or Game 2.
    Author: Moe Cho"""
    while True:
        choice = input("Which game do you want to play? 1. Guessing Game, 2. Rock-paper-scissors. ").strip()
        if choice in ("1", "2"):
            return choice
        print("Invalid choice! Please enter 1 or 2.")
 

def run_game(choice):
    """Calls the game function that matches the user's choice.
    Author: Moe Cho"""
    if choice == "1":
        guessing_game()
    else:
        rock_paper_scissors()
 
 
def after_game():
    """Display options for nect action everytime after running the game
    Author: Moe Cho"""
    while True:
        answer = input("Do you want to play again (P), switch games (S), or quit (Q)? ").strip().upper()
        if answer in ("P", "S", "Q"):
            return answer
        print("Invalid choice! Please enter P, S, or Q.")
 
 
def main():
    choice = choose_game()
 
    while True:
        run_game(choice)
        answer = after_game()
 
        if answer == "S":
            choice = choose_game()
        elif answer == "Q":
            print("Thanks for playing!")
            break
 
 
if __name__ == "__main__":
    main()
 
