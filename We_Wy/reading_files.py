# This program is a 4# lesson of In_Ou Udemy
# Author: Mateusz Gąsior

file = open("c:\\Users\\HP\\Desktop\\Python requirement.txt", "r")

content = file.read()
print(content)

file.close()
"""
with open("c:\\Users\\HP\\Desktop\\Python requirement.txt",'r') as file:
    content = file.read()
    print(content)

with open("c:\\Users\\HP\\Desktop\\Python requirement.txt",'r') as file:
    for line in file:
        print(line)
"""

file = open("c:\\Users\\HP\\Desktop\\Python requirement.txt", "r")

# Warto wykorzystywać do odczytywania fragmentów pliku

fragment = file.read(10)
while fragment:
    print(file.tell(), fragment)
    fragment = file.read(10)

file.close()

print("-----------------------------------------------------------------------")

file_path = "c:\\Users\\HP\\Documents\\Python_Projects\\Udemy_kurs_podstawowy\\We_Wy\\orders.csv"

with open(file_path, 'r') as file:
    for line in file:

        line = line.replace('\n', '')
        order = line.split(";")

        if len(order) == 4:
            print('Order from drugstore "%s", item "%s", amount %s' % (order[0], order[1], order[2]))
        else:
            print("Line %s malformed!!!" % line)

print("Process finished")
