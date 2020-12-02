import datetime

print('Minimum and maximum',datetime.MINYEAR, datetime.MAXYEAR)

dl = datetime.timedelta(days=1,hours=2,minutes=-30)
print(dl)

d2 = datetime.timedelta(days=-1,hours=-2,minutes=-3)
print(d2)

print("timedelta sum",dl+d2)
print('-----------------------------------------\n\n\n')



print('Today is',datetime.date.today())
print('\n')


today = datetime.date.today()
daysToPay = datetime.timedelta(days=7)
print("Today is ",today)
print("Bills should be paid within:", daysToPay.days,"days")
print("The bill shuld be paid till:",today + daysToPay)
print("\n")

endOfTheWorld = datetime.date.max
print("The final end of the world will happen (by Python):",endOfTheWorld)
print(endOfTheWorld.weekday())
print('\n')

bornDate = datetime.date(1999,2,26)
today = datetime.date.today()
print(today - bornDate)
print('-----------------------------------------\n\n\n')


print('now()\t',datetime.datetime.now())
print('today()\t',datetime.datetime.today())
print('utcnow()\t',datetime.datetime.utcnow())
print('weekday()\t',datetime.datetime.today().weekday())

print("%a",datetime.datetime.now().strftime("%a"))
print("%A",datetime.datetime.now().strftime("%A"))
print("%w",datetime.datetime.now().strftime("%w"))
print("%a %A %w",datetime.datetime.now().strftime("%a %A %w"))
print("%Y-%m-%d_%H_%M_%S_%f",datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S_%f"))


print("\n\n\n")
print("*****************************************************\n\n")

inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

print(len(inputdata))
print(len(factortable))

if len(inputdata) == len(factortable):
    print('TRUE')
    for i in range(len(inputdata)):
        minvalue = inputdata[i] - factortable[i] * inputdata[i]
        maxvalue = inputdata[i] + factortable[i] * inputdata[i]
        print(minvalue)
        print(maxvalue)
        print('\n')
else:
    print('inputdata and factortable need to have equal number of elements')
