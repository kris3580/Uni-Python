# SARCINA 1

# b)
colorsList = [ "Green", "Purple", "Orange", "Cyan" ]

print(f"{colorsList[0]} {colorsList[2]}")

colorsList[1] = "Pink"

print(colorsList[2:4])

colorsList.append("Red")
print("lungimea colorsList: " + str(len(colorsList)) + "\n")
del(colorsList)

# c)
drinksTuple = ("Water", "Milk", "Juice", "Honey")

print(type(drinksTuple)) 

print(f"{drinksTuple[0]} {drinksTuple[2]}")

print(f"{min(drinksTuple)} {list(drinksTuple[1])} {len(drinksTuple[2])} \n")

# d)
numberSet = {2, 0, 0, 3, 3, 5, 8, 0}

print(numberSet)

numberSet.remove(0);
print(str(max(numberSet)) + "\n")

# e) 
flowerDictionary = {38: 'Tulip', 66: 'Rose', 81: 'Lily'}
animalsDictionary = {'AV': 'Bunny', 'SA': 'Cat', 'NT': 'Deer', 'LV': 'Fox'} 

print(animalsDictionary.keys()) 
print(animalsDictionary.values())

print(f"{len(flowerDictionary)} {sum(flowerDictionary)} \n")

# f)
drinksList = list(drinksTuple)

# SARCINA 2

# a)
foodList = [ "Pizza", "Pasta", "Tenders" ]
priceList = [ 100, 70, 60 ]
print("Menu: ------- \n{}: {} lei \n{}: {} lei \n{}: {} lei \n".format(foodList[0], priceList[0], foodList[1], priceList[1], foodList[2], priceList[2]))

# b)
print("enter age: ")
age = int(input())
ageAfterFiveYears = age + 5
print("after 5 years you will be " + str(ageAfterFiveYears) + " years old")

# c)
print(age in numberSet)
print(ageAfterFiveYears not in numberSet)
print(drinksTuple[0] in foodList)