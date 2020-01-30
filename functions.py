def scanForLetter(letter, wordToGuess, current):
    n = -1
    found = False
    for x in wordToGuess:
        n += 1
        if letter == x:
            current[n] = x
            found = True
    if found:
        print(" ".join(current))
        return True
    else:
        return False


def guess(letter, wordToGuess, current):
    if len(letter) != 1:
        print("Enter ONE letter at a time.")
    else:
        return scanForLetter(letter, wordToGuess, current)
