import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize the number of guesses
    num_guesses = 0
    
    while True:
        # Get user input for a guess
        guess = int(input("Guess a number between 1 and 100: "))
        
        # Increment the number of guesses
        num_guesses += 1
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {num_guesses} tries.")
            break

guess_number()