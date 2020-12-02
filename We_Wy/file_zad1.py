# This program is an 1# example of In_Ou Udemy
# Author: Mateusz Gąsior

import os

web_addresses = []
line = input("Insert web site address, if you want to STOP press Enter: ")

while line != '':
    web_addresses.append(line)
    line = input("Insert web site address, if you want to STOP press Enter: ")

dir_name = os.getcwd()
file_name = input("Insert name of new file: ")

file_path = os.path.join(dir_name, file_name)

file = open(file_path, 'w')

for adress in web_addresses:

    file.write(adress + "\n")

file.close()
