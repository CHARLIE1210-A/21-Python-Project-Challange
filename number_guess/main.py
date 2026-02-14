import random

# ================= CONFIGURATION =================
DIFFICULTY_LEVELS = {
    "1": {"name":"Easy", "range": 10, "attempts": 5},
    "2": {"name":"Medium", "range": 50, "attempts": 7},
    "3": {"name":"Hard", "range": 100, "attempts": 10},
}

# ================= UTILITY FUNCTION =================

def choose_difficulty():
    print("\nChoose a difficulty level: ")
    print("1 - Easy (Number between 1-10, 5 attempts)")
    print("2 - Medium (Number between 1-50, 7 attempts)")
    print("3 - Hard (Number between 1-100, 10 attempts)")
    
    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice in DIFFICULTY_LEVELS:
            return DIFFICULTY_LEVELS[choice]
        else:
            print("Invalid choice. Please try again.")
            
def get_guess():
    while True:
        try:
            return int(input("Enter your guess: "))
        except:
            print("Invalid input. Please enter a number, try again.")
            
def calculate_score(attempts_left, difficulty):
    base_score = 100
    penalty = (difficulty["attempts"] - attempts_left) * (difficulty["range"] // 10)
    return max(base_score - penalty, 0)

# ================= CORE GAME =================
def play_game():
    settings = choose_difficulty()
    secret_number = random.randint(1, settings['range'])
    attempts = settings['attempts']
    
    print(f"\nDifficulty: {settings['name']}"
          f"\nGuess a number between 1 and {settings['range']}"
          f"\nAttempts left: {attempts}\n"
        )
    while attempts > 0:
        guess = get_guess()
        
        if guess == secret_number:
            score = calculate_score(attempts, settings)
            print(f"Congratulaations! You've guessed the number.")
            print(f"Your score: {score}\n")
            return 
        
        elif guess < secret_number:
            print("Too Low!!, Try again.\n")
        
        else:
            print("Too High!!, Try Again.\n")
            
        attempts -= 1
        print(f"Attempts left: {attempts}")
        
    print(f"Sorry, you've run out of attempts. The number was {secret_number}.")
    
# ================= ENTRY POINT =================
def main():
    print("Welcome to the Number Guessing Game!")
    while True:
        play_game()
        again = input("Do you want to play again? (y/n):").lower()
        
        if again != 'y':
            print("Thank you for playing! Goodbye!")
            break
        
if __name__ == "__main__":
    main()
    
    
    