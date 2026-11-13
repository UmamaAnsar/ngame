import random

def number_guessing_game():
    print("Welcome to the number guessing game.")
    print("I have selected a number between 1 and 100.")
    print("You have 7 attempts to guess the number.")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess number: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1

        if guess == number_to_guess:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")

# Ask if you want to play again
while True:
    number_guessing_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break




if __name__ == "__main__":
    number_guessing_game()            