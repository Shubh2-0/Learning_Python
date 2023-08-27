import random


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    choices = ["rock", "paper", "scissors"]
    player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    if player_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(player_choice, computer_choice)
    print(result)


# Main loop
while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
