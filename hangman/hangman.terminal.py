from word import words  # make sure word.py is in the same folder
import random

# pick a random word
word = random.choice(words)

# hide the word
display = ["_"] * len(word)

# track guessed letters
guessed_letters = []

# max wrong guesses
tries = 6

# hangman stages for drawing
hangman_stages = [
    """
      -----
      |   |
          |
          |
          |
          |
    --------
    """,
    """
      -----
      |   |
      O   |
          |
          |
          |
    --------
    """,
    """
      -----
      |   |
      O   |
      |   |
          |
          |
    --------
    """,
    """
      -----
      |   |
      O   |
     /|   |
          |
          |
    --------
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
          |
          |
    --------
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     /    |
          |
    --------
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    --------
    """
]

print("Welcome to Hangman")

# main game loop
while "_" in display and tries > 0:
    print("\nWord:", " ".join(display))
    print("Tries left:", tries)
    print(hangman_stages[6 - tries])  # draw hangman

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that")
        continue

    guessed_letters.append(guess)

    # check guess and update display
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("Good job")
    else:
        tries -= 1
        print("Nope")

# final message
if "_" not in display:
    print("\nYou won! The word was:", word)
else:
    print("\nYou lost! The word was:", word)
    print(hangman_stages[6])