age = 27

if age >= 18:
    print("You are adult and you can buy alcohol")
else:
    print("You are too young to buy alcohol")

isDrunk = False

if age >= 18 and not isDrunk:
    print("You are adult and you can buy alcohol")
else:
    print("Sorry, we cannot sell you alcohol")



isRestictedArea = False

if age >= 18 and not isDrunk and not isRestictedArea :
    print("You are adult and you can buy alcohol")
else:
    print("Sorry, we cannot sell you alcohol")

MIN_LIKES = 500
MIN_SHARES = 100

num_likes = 600
num_shares = 99

if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:
    print("You get 10% discount")
else:
    print("Sorry, you need more likes / shares to get a discount")


isPizzaOrdered = False

isBigDrinkOrdered = True

isWeekend = False

if not isWeekend and (isPizzaOrdered or isBigDrinkOrdered):
    print("You get a ticket for free Burger")
else:
    print("Keep buying")


diskSize = 140

diskSizeUsed = 130

fileSize = 10

if fileSize <= (diskSize - diskSizeUsed):
    print("File can be downloaded")
else:
    print("Not enough space")
    
    
