import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins
        nonlocal game_count

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        player_choice = input("\n\nEnter ... \n1 for Rock,\n2 for Paper,\n3 for Scissors:\n\n")
        
        if player_choice not in ["1", "2", "3"]:
            print("Invalid entry. Please Select 1, 2, or 3.")
            return play_rps()
        
        player = int(player_choice)

        computer_choice = random.choice("123")
        computer = int(computer_choice)

        print(f"\nYou chose {str(RPS(player)).replace('RPS.', '')}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '')}.\n")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return "Winner! 🥳"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "Winner! 🥳"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "Winner! 🥳"
            elif player == computer:
                return "Tie! 😲"
            else:
                python_wins += 1
                return "Python wins 🐍"
            
        game_result = decide_winner(player, computer)

        print(game_result)
        
        game_count += 1

        print(f"\nGame Count: {str(game_count)}")
        print(f"Player Wins: {str(player_wins)}")
        print(f"Python Wins: {str(python_wins)}")

        print("\nWould you like to play again?")
        while True:
            play_again = input("\nY for Yes \nQ to Quit \n")
            if play_again.lower() not in ["y", "q"]:
                continue # Restart play_again loop if not Y or Q
            else:
                break

        if play_again.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉🎉\n")
            print("Thank you for playing!\n")
            sys.exit("Bye! 👋")

    return play_rps

play = rps()

play()