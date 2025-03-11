# SARCINA 1

age = int(input("Introduceti varsta: "))
if not (20 <= age and age <= 120): print("Varsta trebuie sa fie peste 20 de ani si sub 120 de ani!")

sex = input("Introduceti sexul (m/f): ")
if not (sex == "f" or sex == "m"): print("Sex invalid!")

weight = int(input("Introduceti greutatea (kg): "))
if not (45 <= weight and weight <= 300): print("Greutatea nu poate fi mai mica de 45 kg si mai mare de 300 kg!") 

height = int(input("Introduceti inaltimea (cm): "))
if not (150 <= height and height <= 220): print("Inaltimea nu poate fi mai mica de 150cm si mai mare de 220cm!")


def lorentz(age, sex, weight, height):
    if sex == "f":
        return height - 100 - ((height - 150) / 4 + (age - 20) / 4)
    elif sex == "m":
        return height - 100 - ((height - 150) / 2.5 + (age - 20) / 6)


idealWeight = lorentz(age, sex, weight, height)

print(f"Greutatea ta: {weight}kg, Greutatea ta ideala: {round(idealWeight, 2)}kg")

if round(weight) - round(idealWeight) > 0 :
    print("Greutatea este mai mare decat cea asteptata! Incercati sa slabiti.")
elif round(weight) - round(idealWeight) < 0 :
    print("Greutatea este mai mica decat cea asteptata! Incercati sa adaugati greutate.")
else :
    print("Aveti o greutate ideala!")    


# SARCINA 2

while (True):
    userInput = input("Pisica ta este mai mica decat un an? (da/yes/nu/no): ")

    if userInput == "yes" or userInput == "da":
        isYoungerThanAYear = True
        break
    elif userInput == "no" or userInput == "nu":
        isYoungerThanAYear = False
        break
    else:
        print("Intrare gresita!")

# daca e mica de un an
if (isYoungerThanAYear):
    catHumanAgeDictionary = {
        1 : "6 luni",
        2 : "10 luni",
        3 : "2 ani",
        4 : "5 ani",
        5 : "8 ani",
        6 : "14 ani",
        7 : "15 ani",
        8 : "16 ani",
        9 : "16 ani",
        10 : "17 ani",
        11 : "17 ani",
    }
    
    while (True):
        userInput = int(input("Cate luni are pisica? [1-11]: "))

        if 1 <= userInput and userInput <= 11: 
            print(f"In luni/ani omenesti, pisica ta are {catHumanAgeDictionary[userInput]}!")
            break
        else:
            print("Intrare gresita!")


# daca e mai mare de un an
else:
    while (True):
        userInput = int(input("Cati ani are pisica? [1-35): "))

        if 1 <= userInput and userInput < 35: 
            # daca are un an
            if userInput == 1: catAge = 18
            
            # daca are doi ani
            elif userInput == 2: catAge = 25
            
            # daca e intre 3-15 ani
            elif 3 <= userInput and userInput <= 15: catAge = userInput * 4
                
            # daca e de la 16 ani in sus
            else: catAge = userInput * 3

            print(f"In ani omenesti, pisica ta are {catAge} ani!")
            break
        
        else:
            print("Intrare gresita!")
