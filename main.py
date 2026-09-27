#main.py

import guessing_game 
import rock_paper_scissors

def choose_game():
    """Displays game menu inside a loop and ask the player to choose Game 1 or Game 2.
    Author: Moe"""
    while True:
        choice = input("Which game do you want to play? 1. Guessing Game, 2. Rock-paper-scissors. ").strip()
        if choice in ("1", "2"):
            return choice
        print("Invalid choice! Please enter 1 or 2.")
 
 
def run_game(choice):
    """Calls the game function that matches the user's choice.
    Author: Moe"""
    if choice == "1":
        guessing_game.guessing_game()
    else:
        rock_paper_scissors.rock_paper_scissors()
 
 
def after_game():
    """Display options for nect action everytime after running the game
    Author: Moe"""
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
 
