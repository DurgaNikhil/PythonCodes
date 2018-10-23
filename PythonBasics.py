"""
The main contents of this Program is to 
Work with the logical operartors
such as and, or
we will be using the Boolean data type as a reference

"""

IsRainning = True
IsSunny = True

if IsRainning and IsSunny:
    print(" Then we get a rain bow")

#Using or operator
if IsSunny or IsRainning:
    print(" Then its going to be either rainy or sunny")

#Uing an array to check wether we have 
ages = [17, 22, 33, 10]

for age in ages:
    isAdult = age > 17
    if not isAdult:
        print(" You are not an adult " + str(age))


checkingvalue = 10 < 22

LastName = "Narayanadas"
len(LastName)
print(len(LastName))

listNum = [1, 2, 3, 4, 5]
i= 0
for i in range(i, len(listNum)):
    print(listNum[i])

#Printing dictionary
ditionary = {"name" : 10, "Nikhil": 22}
print(max("Nikhil", "Narayanadas"))


dictionary = {123 : "Mikihl"}
print(dictionary.get(123))


class car:
    pass

c = car()
convert = c
chekking = isinstance(c, car)

import math
import random
#Giving us the random number from 0 -1 
print(random.random())


#Printing out the random range from 0 -2
decider = random.randrange(2)
if decider == 0:
    print(" Heads ")
else:
    print(" TAILS ")

#Printing the random range from 1 - 6
print(random.randrange(1, 7))


#Printing the sample numbers from random 
print(random.sample(range(100), 5))


#Printing the random choice from the list containing the list of strings
ListOfStrings =  ["NIkhil", "Krishna"]
print(random.choice(ListOfStrings))