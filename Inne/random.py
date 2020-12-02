import random
print("One random number:",random.randint(1,100))
print("\n")

print("Choosing rundom number from a range",random.choice(range(1,100)))
print("\n")

print("Choosing rundom number from a range - easier",random.randrange(1,100))
print("\n")

list=['John','Ann','Peter','Susan','Emuly','Greg','Chris']
random.shuffle(list)
print("Reordered list:",list)
print("\n")

print("Just a random float",random.random())
print("\n")

print("----------------------------------------------------------")

from random import *

for i in range(10):
    print(i,randint(1,100))

print("****************************************")

number1 = randint(1,100)
print(number1)

counter = 1

number2 = randint(1,100)

while number1 != number2:
    counter+=1
    number2 = randint(1,100)
    print(counter, number2)

print('I need %d attempts to generate %d again'%(counter,number1))

print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]

shuffle(countries)

groupNumber = 0

for i in range(len(countries)):
    if i % 4 == 0:
        groupNumber += 1
        print("========== Group %d ==========" % (groupNumber))
    print(countries[i])
