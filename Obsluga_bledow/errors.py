# This program is lesson no 1 of Error handling
# Author: Mateusz Gąsior

import sys

file_path = r'c:\Users\HP\Documents\Python_Projects\Udemy_kurs_podstawowy\Obsluga_bledow\orders.csv'

with open(file_path, "r") as file:
    for line in file:
        line = line.replace('\n', '')
        order = line.split(',')

        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])

            print('Order from drugstore "%s", item "%s", amount %d' % (pharmacy_name, item, amount))

        except ValueError as e:
            print("\nSomething happen with data conversion in %s\n" % line)

        except IndexError as e:
            print('\nNot enough data in %s\n' % line)

        except:
            print("\nUnknow problem with line %s\n" % line)
            print(sys.exc_info()[0])

print("Processing finished")
