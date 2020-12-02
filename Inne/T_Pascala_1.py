width = 60
height = 8

numbers = [1]                                   #Rozpoczęcie tablicy

line = ''
for n in numbers:
    line+="%3d " % (n)
print(line.center(width))                       #Loop for the breaks



for i in range(height - 1):

    newNumbers = [1]

    position = 0
    while position < len(numbers) -1:
        newNumbers.append(numbers[position]  + numbers[position+1])
        position+=1

    newNumbers.append(1)

    numbers = newNumbers.copy()

    line=''
    for n in numbers:
        line+="%3d " % (n)
    print(line.center(width))
    
    
