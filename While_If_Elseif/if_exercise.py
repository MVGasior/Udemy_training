musclePain = False
fever = True
weakness = True

print("suspicion of influenza" if musclePain and fever and weakness else "The flu is unlikly")


print("----")

if musclePain and fever and weakness:
    print("suspicion of influenza")
elif weakness:
    print("Just take a rest!")
else:
    print("you may be cold")

isMan = False

if musclePain and fever and weakness or isMan and (musclePain or fever or weakness):
    print("suspicion of influenza")
elif not isMan and weakness:
    print("Just take a rest!")
else:
    print("you may be cold")


print("----")

isCheckCompleted = False

print("CHECK IS COMPLETED" if isCheckCompleted else "CHECK NOT DONE YET!")




