import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("You lose!")

def play_round():
    user_choice = ""
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, winner)
    return winner

def main():
    print("Welcome to Rock-Paper-Scissors Game!")
    user_score = 0
    computer_score = 0

    while True:
        winner = play_round()
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"Scores: You - {user_score}, Computer - {computer_score}")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing! Final Scores:")
    print(f"You: {user_score}, Computer: {computer_score}")
    print("Goodbye!")

if __name__ == "__main__":
    main()