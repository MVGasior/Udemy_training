# This program is a 5# lesson of In_Ou Udemy
# Author: Mateusz Gąsior

file_name = "c:\\Users\\HP\\Desktop\\Info_06082020.txt"

line = "Europe"

cities = ['London', 'Berlin', 'Paris', 'Warsaw', 'Madrid', 'Rome']

file = open(file_name, 'w+')

file.write(line)
file.write("\n")
# file.writelines(cities)

for city in cities:
    file.write(city + '\n')

file.close()



