import random

def get_difficulty():
    """Let the player choose the difficulty level."""
    print("\nChoose difficulty level:")
    print("1. Easy (1-50, 10 guesses)")
    print("2. Medium (1-100, 7 guesses)")
    print("3. Hard (1-200, 5 guesses)")
    print("4. Custom (you choose the range and attempts)")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

def get_custom_settings():
    """Get custom game settings from the player."""
    while True:
        try:
            min_num = int(input("Enter minimum number: "))
            max_num = int(input("Enter maximum number: "))
            
            if min_num >= max_num:
                print("Maximum must be greater than minimum. Try again.")
                continue
                
            max_attempts = int(input("Enter number of attempts: "))
            
            if max_attempts <= 0:
                print("Attempts must be positive. Try again.")
                continue
                
            return min_num, max_num, max_attempts
        except ValueError:
            print("Please enter valid numbers.")

def play_game():
    """Main game function."""
    print("=" * 50)
    print("Welcome to the Number Guessing Game!")
    print("=" * 50)
    
    # Game settings based on difficulty
    difficulty = get_difficulty()
    
    if difficulty == 1:  # Easy
        min_num, max_num, max_attempts = 1, 50, 10
    elif difficulty == 2:  # Medium
        min_num, max_num, max_attempts = 1, 100, 7
    elif difficulty == 3:  # Hard
        min_num, max_num, max_attempts = 1, 200, 5
    else:  # Custom
        min_num, max_num, max_attempts = get_custom_settings()
    
    # Generate secret number
    secret_number = random.randint(min_num, max_num)
    attempts = 0
    
    print(f"\nI'm thinking of a number between {min_num} and {max_num}.")
    print(f"You have {max_attempts} attempts to guess it.")
    print("-" * 30)
    
    # Main game loop
    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts + 1
        
        try:
            guess = int(input(f"\nAttempt {attempts}/{max_attempts} (Remaining: {remaining}): "))
            
            # Check if guess is in valid range
            if guess < min_num or guess > max_num:
                print(f"Please guess between {min_num} and {max_num}.")
                attempts -= 1  # Don't count invalid attempts
                continue
                
            # Check the guess
            if guess == secret_number:
                print("=" * 50)
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                print("=" * 50)
                return True
            elif guess < secret_number:
                print(f"Too low! The number is higher than {guess}.")
            else:
                print(f"Too high! The number is lower than {guess}.")
                
            # Give hints based on how close the guess is
            difference = abs(secret_number - guess)
            if attempts >= max_attempts // 2:  # Give hints after half the attempts
                if difference <= 5:
                    print("Hint: You're very close!")
                elif difference <= 15:
                    print("Hint: You're getting warm...")
                    
        except ValueError:
            print("Please enter a valid number.")
            attempts -= 1  # Don't count invalid attempts
    
    # If player runs out of attempts
    print("=" * 50)
    print(f"💔 Game Over! You've used all {max_attempts} attempts.")
    print(f"The secret number was {secret_number}.")
    print("=" * 50)
    return False

def main():
    """Main program loop with replay option."""
    games_played = 0
    games_won = 0
    
    while True:
        games_played += 1
        
        if play_game():
            games_won += 1
        
        print(f"\n📊 Statistics: {games_won} wins out of {games_played} games")
        
        # Ask if player wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y', 'yeah', 'yep']:
            print("\nThanks for playing! Goodbye!")
            break

# Run the game
if __name__ == "__main__":
    main()