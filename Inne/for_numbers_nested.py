##for x in range(1,6):
##    line = str(x)
##    for y in range(1,6):
##        line += '\t%3d' % (x*y)
##    print(line)
##
##print('\n')

i=10
result=1

for j in range(1,i+1):
    result = j * result
   

print(i, result)
print('\n')

for a in range(1,11):
    wynik = a
    for b in range(1,a):
        wynik = b * wynik
    print(a, wynik)

print('\n')

list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for noun in list_noun:
    for adj in list_adj:
        print(adj,noun)
        
