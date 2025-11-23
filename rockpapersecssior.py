# ------- TASK - 4 --- ROCK, PAPER, SCISSOR GAME ----------
import random

def get_computer_choice():
    """Returns a random choice for the computer"""
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def decide_winner(user, computer):
    """Determines the winner based on game rules"""
    if user == computer:
        return "draw"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    print("===== Rock Paper Scissors Game =====")

    while True:
        print("\nChoose: rock / paper / scissors")
        user_choice = input("Enter your choice: ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input! Please choose correctly.")
            continue

        computer_choice = get_computer_choice()

        print("Your choice     :", user_choice)
        print("Computer choice :", computer_choice)

        result = decide_winner(user_choice, computer_choice)

        if result == "draw":
            print("Result: It's a Draw ")
        elif result == "user":
            print("Result: You Win ")
            user_score += 1
        else:
            print("Result: Computer Wins ")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            print("\nThank you for playing!")
            break

# Program Execution
if __name__ == "__main__":
    play_game()
