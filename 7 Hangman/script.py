from random_word import RandomWords

hangman_stages = [
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """]

print("Welcome to Hangman!")
r = RandomWords()
word = r.get_random_word()
word_length = len(word)

print(f"The word to guess has {word_length} letters.")
display = ['_'] * word_length
lives = 6
end_of_game = False
guessed_letters = []
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if(guess.isalpha() == False or len(guess) != 1):
        print("Please enter a single alphabetical character.")
        continue
    if guess in guessed_letters:
        print(f"You've already guessed the letter '{guess}'. Try again.")
        continue
    else:
        guessed_letters.append(guess)

    for position in range(word_length):
        letter = word[position]
        if letter == guess:
            display[position] = letter

    if guess not in word:
        lives -= 1
        print(f"The letter '{guess}' is not in the word. You have {lives} lives remaining.")
        if lives == 0:
            end_of_game = True
            print(f"The word was '{word}'.")
            print("You lose.")

    print(f"{' '.join(display)}")
    print(hangman_stages[lives])

    if '_' not in display:
        end_of_game = True
        print("You win.")