IsWeekend = True
print("Is weekend =",IsWeekend)

Temprature = 25
print("Temprature =",Temprature)

ToDoList=' '
print("ToDoList =",ToDoList)

IsHappy = IsWeekend and Temprature >= 20 and ToDoList == ' '
print("IsHappy =",IsHappy)

IsHappy = not IsWeekend and Temprature < 20 and ToDoList != ''
print('IsHappy =',IsHappy)

IsHappy = IsWeekend and Temprature >= 20 and ToDoList == '' \
or not IsWeekend and Temprature < 20 and ToDoList != ''
print('IsHappy =',IsHappy)
