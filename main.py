import random
#name = input("Zeg je naam ")
name = "jan"

print ("Welkom, " + name + ",Klaar voor een lekker potje galgje.")

word_list = ["ïnformatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

def get_word():
  word = random.choice(word_list)
  return word

woord = get_word()

print(woord)
print(len(woord))
print("_" + str(len(woord)))