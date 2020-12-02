cargo = [40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]
cargo.sort()
cargo.reverse()

print("The cargo list is:",cargo)

boxCapacity = 90
box = []
i = 0

while i<len(cargo) and (boxCapacity - sum(box)) >= min(cargo):
    if (boxCapacity - sum(box))>= cargo[i]:
        box.append(cargo[i])
    i+=1


print("The collected items sum is:",sum(box))
print("The elements are:",box)

print("-----")


number=1
previousNumber=0

while number<=50:
    print(previousNumber,'+',number,'=',previousNumber+number)

    previousNumber = number
    number+=1
    

import random
my_number = random.randint(0,20)
trial = 0

guess = -1
print("Guess my number from 0 to 20!")

while guess!=my_number:
    guess = int(input())
    trial+=1
    if guess > 20 or guess < 0:
        print("Number out of range")
    elif guess == my_number:
        print("Congratulation. You made it in:",trial,"trys")
    elif guess > my_number:
        print("Sorry- my number is smaller than your guess, Try again!")
    else:
        print("Sorry- my number is greater than your guess, Try again!")

input('Press enter to continue...')



