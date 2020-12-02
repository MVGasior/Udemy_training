for number in range(1,21):
    if number %2 == 0:
        print('Number %2d is %s' % (number,'even'))
    else:
        print('Number %2d is %s' % (number,'odd'))
   

    
string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'
i=0

for i in range(10):
    print(string_A)

print('\n')

for i in range(9):
    if i % 2 == 0:
        print(string_A)
    else:
        print(string_B)

print('\n')

for i in range(1,10):
    print('x'*i)

print('\n')

for i in range(1,10):
    if i % 2 == 0:
        print('x'*i)
    else:
        print('o'*i)
