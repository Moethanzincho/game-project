# Game 2: Rock, Paper, Scissors
"""Authors : Julia Ueligitone
This Game 2 will allow a user to play multiple rounds of Rock, Paper, Scissors 
with a random computer opponent."""

import random

def rock_paper_scissors():
   """Runs a single round of Rock, Paper, Scissors against a computer opponent.
  The user will choose (Y/N) to begin the game. 
  The user will input a number between 1 and 3, then a random choice will be generated
   by the computer and determine a winner or draw. 
   The results will be printed and prompt the user to play again. 
   Authors: Julia Ueligitone""
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

if __name__ == "__main__":
    start_play = input("Do you want to play? (Y/N)").strip().lower()

    while start_play == "y":
        rock_paper_scissors()
        start_play = input("Do you want to play again? (Y/N)").strip().lower()
