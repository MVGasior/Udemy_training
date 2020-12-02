values=[10,43,12,48,12,11,18,98,57,28,19,27,49,19,74]

i = 0
max = len(values)-2

while i<max:
    #print(i,values[i],values[i+1],values[i+2])

    if values[i]<values[i+1] and values[i+1]<values[i+2]:
        print('\tFound: ',values[i],values[i+1],values[i+2])
        
    i+=1

numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

j = 0
maxx = len(numbers)-2

while j<maxx:
    #print(numbers[j],numbers[j+1])

    if numbers[j]**2==numbers[j+1] and numbers[j+1]**2==numbers[j+2]:
        print("FOUND: ",numbers[j],numbers[j+1],numbers[j+2])

    j+=1

texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

k = 0
maxi = len(texts) - 1

while k<maxi:
    #print(len(texts[k]),len(texts[k+1]))

    if len(texts[k])==len(texts[k+1]):
        print("Found: ",texts[k],"and",texts[k+1],"have",len(texts[k]),"letters")

    k+=1
