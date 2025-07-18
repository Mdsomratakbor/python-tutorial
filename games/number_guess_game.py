import random

def run():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    # Generate secret number
    secret_number = random.randint(1, 10)

    # Ask user for number of tries
    while True:
        try:
            max_try_range = int(input('🔢 How many attempts would you like? '))
            if max_try_range <= 0:
                print("⚠️ Please enter a positive number.")
                continue
            break
        except ValueError:
            print("⚠️ Please enter a valid number.")

    # Start guessing loop
    for attempt in range(1, max_try_range + 1):
        while True:
            try:
                guess = int(input(f"Attempt {attempt}/{max_try_range} - Guess the number: "))
                if 1 <= guess <= 10:
                    break
                else:
                    print("⚠️ Please guess a number between 1 and 10.")
            except ValueError:
                print("⚠️ Invalid input! Enter a number.")

        if guess == secret_number:
            print("🎉 Winner! You guessed it right!")
            break
    else:
        print(f"💥 Sorry, you lost. The correct number was: {secret_number}")

# Run the game
#run()
