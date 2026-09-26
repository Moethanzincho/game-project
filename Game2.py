# Game 2
import random

def play_game():
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
        play_game()
        start_play = input("Do you want to play again? (Y/N)").strip().lower()
