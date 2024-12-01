import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game SHLINGY!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    while True:
        guess = input("Enter your guess: ")
        
        # Validate the input
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number_to_guess:
            print("Too low GAVO! Try again.")
        elif guess > number_to_guess:
            print("Too high SLINGY! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

# Run the game
number_guessing_game()