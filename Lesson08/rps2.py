import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

play_again = True

while play_again:

    player_choice = input("\n\nEnter ... \n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n")
    player = int(player_choice)

    if player < 1 or player > 3:
        sys.exit("Invalid entry. Please Select 1, 2, or 3.")

    computer_choice = random.choice("123")
    computer = int(computer_choice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".\n")

    if player == 1 and computer == 3:
        print("Winner! 🥳")
    elif player == 2 and computer == 1:
        print("Winner! 🥳")
    elif player == 3 and computer == 2:
        print("Winner! 🥳")
    elif player == computer:
        print("Tie! 😲")
    else:
        print("Python wins 🐍")

    play_again = input("\nWould you like to play again? \nY for Yes \nQ to Quit \n\n")

    if play_again.lower() == "y":
        continue
    else:
        print("\n🎉🎉🎉\n")
        print("Thank you for playing!\n")
        play_again = False

sys.exit("Bye! 👋")