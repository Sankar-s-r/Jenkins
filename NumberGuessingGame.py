import random

def simple_auto_game():
    """Ultra-simple automatic guessing game for Jenkins"""
    print("Starting Automatic Number Guessing Game...")
    
    # Fixed settings
    min_num, max_num = 1, 50
    max_attempts = 8
    secret = random.randint(min_num, max_num)
    
    print(f"Target number between {min_num} and {max_num}")
    print(f"Max attempts: {max_attempts}")
    print("-" * 40)
    
    attempts = 0
    low, high = min_num, max_num
    
    while attempts < max_attempts:
        attempts += 1
        guess = (low + high) // 2
        
        print(f"Attempt {attempts}: Guessing {guess}")
        
        if guess == secret:
            print(f"✓ SUCCESS! Found {secret} in {attempts} attempts!")
            print("Game completed successfully!")
            return 0  # Exit code 0 for success
        
        elif guess < secret:
            print(f"  Too low!")
            low = guess + 1
        else:
            print(f"  Too high!")
            high = guess - 1
    
    print(f"✗ FAILED! Secret number was {secret}")
    print("Game completed!")
    return 0  # Still exit with 0 as game ran successfully

if __name__ == "__main__":
    simple_auto_game()