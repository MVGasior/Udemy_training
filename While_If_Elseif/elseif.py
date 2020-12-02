age = 23
isDrunk = True
isRestictedArea = False

if age < 18:
    print("You are too young to buy alcohol")
else:
    if isDrunk:
        print("Are yoi drunk? We cannot sell you alcohol")
    else:
        if isRestictedArea:
            print("Resticted area. Alcohol is forbidden")
        else:
            print("OK, you can buy alcohol")


print("----")

if age < 18:
    print("You are too young to buy alcohol")
elif isDrunk:
    print("Are yoi drunk? We cannot sell you alcohol")
elif isRestictedArea:
    print("Resticted area. Alcohol is forbidden")
else:
    print("OK, you can buy alcohol")

print("----")

num_likes = 499
num_shares = 100

LIKES = 500
SHARES = 100

if num_likes >= LIKES and num_shares >= SHARES:
    print("Congratulation! You get discount")
elif num_likes < LIKES:
    print("Not enought likes")
else:
    print("Not enought shares")

print("----")

isPizzaOrdered = False
isBigDrinkOrdered = True
isWeekend = False

if not isWeekend and (isPizzaOrdered or isBigDrinkOrdered):
    print("Congratulation! You get a burger")
elif isWeekend:
    print("Sorry, discount is not avaliable during weekend")
else:
    print("Sorry, you have to buy big drink or Pizza to get free burger")



    
    
    
    
