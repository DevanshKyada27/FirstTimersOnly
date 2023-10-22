import random

# List of words to choose from
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

def choose_random_word():
    return random.choice(word_list)

def play_game():
    print("Welcome to the Random Word Guessing Game!")
    word_to_guess = choose_random_word()
    guessed_letters = []
    attempts = 6  # You can change the number of allowed attempts

    while attempts > 0:
        word_display = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                word_display += letter
            else:
                word_display += "_"

        print("\nWord to guess: " + word_display)
        print("Guessed letters: " + ", ".join(guessed_letters))
        print("Attempts remaining: " + str(attempts))

        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            print("Wrong guess!")
            attempts -= 1

        if "_" not in word_display:
            print("\nCongratulations! You guessed the word: " + word_to_guess)
            break

    if attempts == 0:
        print("\nOut of attempts. The word was: " + word_to_guess)

if __name__ == "__main__":
    play_game()
