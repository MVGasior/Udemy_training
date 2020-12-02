# This program is an 1# example of In_Ou Udemy
# Author: Mateusz Gąsior

import os

while True:
    file_name = input("Please insert a path of the file: ")
    if os.path.isfile(file_name):
        break
    else:
        print("The path of the file is incorrect")

web_addresses = []

with open(file_name, 'r') as web_file:
    for address in web_file:

        address = address.replace("\n", "")
        web_addresses.append(address)

dir_name = os.path.dirname(file_name)
web_path_pl = os.path.join(dir_name, 'webs_pl.txt')
web_path_other = os.path.join(dir_name, 'webs_other.txt')

file_pl = open(web_path_pl, 'w')
file_other = open(web_path_other, 'w')

for line in web_addresses:
    if line.endswith('.pl'):
        file_pl.write(line + '\n')
    else:
        file_other.write(line + '\n')

file_pl.close()
file_other.close()

print(web_addresses)