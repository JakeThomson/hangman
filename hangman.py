from getpass import getpass
from functions import *

gameState = None
lives = 8
wordToGuess = getpass("Enter secret word/sentence (HIDDEN): ").upper()
current = []
[current.append("_") for i in range(len(wordToGuess))]

scanForLetter(" ", wordToGuess, current)
print(" ".join(current))

while gameState is None:
    if not guess(input("\nGuess a letter: ").upper(), wordToGuess, current):
        lives -= 1
        print(f"Incorrect. Lives left: {lives}")

    if lives < 1:
        gameState = False
        print()
        print("************")
        print("    LOSE!   ")
        print("************")

    if "_" not in current:
        gameState = True
        print()
        print("************")
        print("    WIN !   ")
        print("************")
