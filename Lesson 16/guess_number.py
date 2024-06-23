import sys
import random

def guess_number(name='Player1'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_guess_number():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins
        nonlocal game_count

        player_choice = input(f"\nHi {name}! \nPlease guess a number between 1 and 5!\n")
        
        if player_choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid entry. Please Choose a number between 1 and 5")
            return play_guess_number()
        
        player = int(player_choice)

        computer_choice = random.choice("12345")
        computer = int(computer_choice)

        print(f"\n{name} chose {player}.")
        print(f"Python was thinking of {computer}.\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins

            if player == computer:
                player_wins += 1
                return f"Correct! {name} is the winner! 🥳"
            else:
                python_wins += 1
                return "Incorrect! Python wins 🐍"
            
        game_result = decide_winner(player, computer)

        print(game_result)
        
        game_count += 1

        print(f"\nGame Count: {game_count}")
        print(f"{name}'s Wins: {player_wins}")
        print(f"Python's Wins: {python_wins}")
        print(f"\n{name}'s win percentage is: {player_wins / game_count: .2%}")

        print("\nWould you like to play again?")
        while True:
            play_again = input("\nY for Yes \nQ to Quit \n")
            if play_again.lower() not in ["y", "q"]:
                continue # Restart play_again loop if not Y or Q
            else:
                break

        if play_again.lower() == "y":
            return play_guess_number()
        else:
            print("\n🎉🎉🎉\n")
            print("Thank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye, {name}! 👋")
            else:
                return            

    return play_guess_number

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name", dest="firstname",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    guess_number_game = guess_number(args.firstname)
    guess_number_game()