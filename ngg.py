import random

def number_guessing_game():
    while True:
        print("\nWelcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")

        secret_number = random.randint(1, 100)
        max_attempts = 10

        for attempt in range(1, max_attempts + 1):
            try:
                guess = int(input(f"\nAttempt {attempt}/{max_attempts}: Enter your guess: "))

                if guess < secret_number:
                    print("Too low!")
                elif guess > secret_number:
                    print("Too high!")
                else:
                    print(f"Congratulations! You guessed the number {secret_number} correctly in {attempt} attempt(s).")
                    break

            except ValueError:
                print("Please enter a valid integer.")
        else:
            print(f"\nGame Over! You've used all {max_attempts} attempts.")
            print(f"The correct number was {secret_number}.")

        play_again = input("\nDo you want to play again? (Yes/No): ").strip().title()

        if play_again != "Yes":
            print("Thanks for playing!")
            break

# Start the game
number_guessing_game()