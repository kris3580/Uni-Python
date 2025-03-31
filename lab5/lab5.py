# SARCINA 1
# a)
# Mai întâi se atribuie lui sum 0, apoi lui i se atribuie sum. După care, atât timp cât i e mai mic sau egal cu 4, atunci
# sum se adună cu i și rezultatul acestuia i se va atribui lui sum. Variabila i este incrementată cu 1. 
# Ciclul se repetă iar într-un final sum este afișat la ecran. (10)
#
# b)
# Într-un ciclu se iterează prin fiecare caracter din "PYTHON STRING".
# În acest ciclu, se verifică dacă char este un spațiu, dacă da, atunci se iese din ciclu.
# Dacă nu, atunci se afișează caracterul respectiv fără a se trece pe un rând nou.
# Se verifică dacă caracterul este egal cu "O", dacă da, atunci continuă iterația ciclului, trecând peste
# instrucțiunea de mai jos, care va afișa la ecran "*", tot fără a scrie de rând nou.
# Rezultat: P*Y*T*H*ON*

# SARCINA 2
# a)
# userInput = input()

# if userInput == "y":
#     print("Da")
# elif userInput == "n":
#     print("Nu")
# else:
#     print("Ai introdus altceva.")
    

# b)

# lista = ["a", "b", "c", "d", "e"]    
# dictionar = {1: "c", 2: "d", 3: "e", 4: "f", 5: "g"}
# text = "abcdefghi"

# valueToFind = "e"
# c = 0;


# allCharactersList = list(lista + list(dictionar.values()) + list(text))
# print(allCharactersList)

# for character in allCharactersList:
#     if character == valueToFind:
#         c += 1;

# print(f"Caracterul \"{valueToFind}\" a fost găsit de {c} ori.")


import functions as f

shopping_list = []

while True:
    print("\nAlegeți o opțiune: 1 - Afișare listă 2 - Adăugare produs 3 - Ștergere produs 4 - Ieșire")
    userInput = input()
    if userInput == "1":
        f.print_list(shopping_list)
    elif userInput == "2":
        f.add_product(shopping_list)
    elif userInput == "3":
        f.delete_product(shopping_list)
    elif userInput == "4":
        break
    else:
        print("Eroare!")           
                 




