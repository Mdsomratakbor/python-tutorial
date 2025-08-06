import random

print("🎮 Welcome to the Word Guessing Game!")
name = input("👋 What is your name? ")

print(f"\nGood Luck, {name}! Let's play. 🤞\n")

# List of possible words
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

# Randomly choose a word
word  = random.choice(words)



print("🔤 Guess the characters in the hidden word!")
print("You have 12 chances to guess the correct word.\n")


guesses = ''  # Store guessed letters
turns = 12    # Number of attempts


while turns > 0:
    failed = 0  # Count incorrect guesses in current word display

    print("Word: ", end="")
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    print()  # Newline

    # If all characters guessed
    if failed == 0:
        print("\n🎉 Congratulations! You guessed the word correctly.")
        print("✅ The word is:", word)
        break

    guess = input("\n🔎 Guess a character: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter only a single alphabetic character.")
        continue

    if guess in guesses:
        print("🔁 You've already guessed that letter. Try a different one.")
        continue

    guesses += guess  # Add guess to the list

    if guess not in word:
        turns -= 1
        print("❌ Incorrect guess.")
        print(f"💡 HINT: The word has {len(word)} letters.")
        print(f"🔄 Remaining attempts: {turns}")

        if turns == 0:
            print("\n😞 You've run out of guesses.")
            print("💀 Game Over!")
            print("📌 The correct word was:", word)
    else:
        print("✅ Good guess!")

print("\n🔚 Thank you for playing! Want to try again? Run the program again. 🎉")

