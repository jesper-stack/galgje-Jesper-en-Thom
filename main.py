import random
word_list = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

name = input("Wat is je naam? ")
print("Welkom " + name)
print("Oké dit zijn de spelregels. Er wordt een woord gegeven, en de bedoeling is dat je het woord te weten komt door middel van letters raden of het woord raden.")

def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()
    print("het woord heeft", len(word))


