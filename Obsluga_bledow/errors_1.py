# This program is lesson no 1 of Error handling
# Author: Mateusz Gąsior
# C:\Users\HP\Documents\Python_Projects\Udemy_kurs_podstawowy\Obsluga_bledow\test.txt

import os

line = input("What is acceptable amount for udemy course: ")
file_path = input("Insert path of your file: ")

try:
    file = open(file_path, 'w+')
    file.write(line)
    file.close()

    value = int(line)
    print("The value saved in file is: ", value)

except FileNotFoundError as e:
    print("Error opening file", file_path, e)
except ValueError as e:
    print("The value entered cannot be converted to a number", line, e)
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')

else:
    print("Actions completed successfully")
