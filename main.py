import random
word_list = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

name = input("Wat is je naam? ")
print("Welkom " + name)
print("Oké dit zijn de spelregels. Er wordt een woord gegeven, en de bedoeling is dat je het woord te weten komt door middel van letters raden of het woord raden.")

def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()
    print("het woord heeft", len(word))

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Nu is het tijd om galgje te spelen!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Raad een letter of woord: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Je hebt", guess, "al geraden!")
            elif guess not in word:
                print(guess, "is niet het woord helaas :(")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Goed gedaan!", guess, "is juist!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Je hebt ", guess, "al geraden!")
            elif guess != word:
                print(guess, " Is niet het woord :(")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Kan niet")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Geficiteerd! je hebt gewonnen")
    else:
        print("Sorry, maar je hebt het woord niet geraden, het woord was " + word + ". Misschien volgende keer.")




def display_hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[tries]

def main():
    word = get_word(word_list)
    play(word)
    while input("Opnieuw? (Y/N) ").upper() == "Y":
        word = get_word(word_list)
        play(word)

if __name__ == "__main__":
    main()
