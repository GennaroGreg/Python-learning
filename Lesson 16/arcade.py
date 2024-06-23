import sys
from rps import rps
from guess_number import guess_number

def arcade(name='Player1'):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade! Please select an option:")

        print("\n1 = Rock Paper Scissors")
        print("2 = Guess the Number")
        print("x = Exit the Arcade")

        arcade_choice = input("\nSelect: ")

        if arcade_choice not in ["1", "2", "x", "X"]:
            print("\nInvalid entry. Please select 1, 2, or x.")
            arcade()

        welcome_back = True

        if arcade_choice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif arcade_choice == "2":
            guess_number_game = guess_number(name)
            guess_number_game()
        else:
            print("Thank you for playing!\n")
            sys.exit(f"Bye, {name}! 👋")


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

    start_arcade = arcade(args.firstname)
    start_arcade()

        