import random

def get_user_choice():
    """Get the user's choice of Rock, Paper, or Scissors."""
    while True:
        user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice! Please choose either 'Rock', 'Paper', or 'Scissors'.")

def get_computer_choice():
    """Get the computer's random choice."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the game rules."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Play the Rock, Paper, Scissors game."""
    print("Welcome to Rock, Paper, Scissors!")
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYour choice: {user_choice.capitalize()}")
    print(f"Computer's choice: {computer_choice.capitalize()}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Run the game
if __name__ == "__main__":
    play_game()
