import random

CHOICES = ["rock", "paper", "scissors"]

def get_user_choice():
    choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()
    if choice in CHOICES or choice == "quit":
        return choice
    print("Invalid choice. Try again.")
    return None

def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    return "You win!" if wins[user] == computer else "You lose!"

def play():
    while True:
        user = get_user_choice()
        if not user:
            continue
        if user == "quit":
            print("Thanks for playing!")
            break
        computer = random.choice(CHOICES)
        print(f"Computer chose: {computer}")
        print(get_winner(user, computer), "\n")

if __name__ == "__main__":
    play()