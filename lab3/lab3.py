# 1
#
# greet_user = lambda name : print('Hello My Dear, ', name)
# user_name = input("What is your name? ")
# greet_user(user_name)
# 
# Prima linie de cod va crea o variabilă în componența căreia va fi
# o funcție anonimă care va lua ca parametru name, și va afișa la consolă
# "Hello My Dear, " și apoi conținutul parametrului name.
# 
# A doua linie de cod va afișa la consolă "What is your name? " iar apoi
# va cere de la tastatură un nume, care va fi apoi stocat în variabila user_name
# 
# Următoarea linie de cod presupune apelarea la funcția lambda stocată în greet_user.
# Ca parametru va lua user_name, rezultatul în consolă fiind, de exemplu:
# "Hello My Dear, Kris"

# 2
tupleList = [(3, 11), (1, 7), (7, 8), (16, 88), (23, 15)]
print(sorted(tupleList, key=lambda x: x[1]))

# 3 exemplu: suma a două numere
showSum = lambda a, b: print(a + b)
showSum(33, 77)

# 4
def pi():
    return 3.14

def modul(a):
    if a < 0:
        return a * -1
    else:
        return a
    
def diferenta(a = 0, b = 1):
    return a - b

# 5
# circumferinta cercului
r = 3
print(2 * pi() * r)

# determinarea distantei dintre doua puncte   
import math     

point1 = [2, 8]
point2 = [-5, 3]

def distanta(pointA, pointB):
    dx = modul(diferenta(pointB[0], pointA[0]))
    dy = modul(diferenta(pointB[1], pointA[1]))
    return math.sqrt(dx * dx + dy * dy)

print("distanta: ", distanta(point1, point2))
