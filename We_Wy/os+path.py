# This program is a 2# lesson of In_Ou Udemy
# Author: Mateusz Gąsior

import os
import time

print("Current directory is:", os.getcwd())

currentDir = os.getcwd()
file_name = 'result.txt'
full_path = os.path.join(currentDir, file_name)
print("\nThe constructed file path is: ", full_path)

relativePath = 'output.txt'
print("\nThe absolute path is: ", os.path.abspath(relativePath))

file_path = "c:\\Users\HP\Documents\Faktura.pdf"
print("\nThe file name part is: ", os.path.basename(file_path))
print("The directory part is: ", os.path.dirname(file_path))

print("\nIs file existing? ", os.path.exists(file_path))

if os.path.exists(file_path):
    print("\nLast modify date is:", os.path.getatime(file_path))
    print("Last modify date is:", time.localtime(os.path.getatime(file_path)))

    print("\nFile size is: ", os.path.getatime(file_path))

    print("\nIs it a file?", os.path.isfile(file_path))
    print("Is it a dir? ", os.path.isdir(file_path))

    print("\nPath splitted:", os.path.split(file_path))
    print("Only file name part:", os.path.split(file_path)[1])

    print("\nPath splitted into drive:", os.path.splitdrive(file_path))
    print("Only drive:", os.path.splitdrive(file_path)[0])

print("-------------------------------------------------------------------------")

dir_path = input("Please insert file's path: ")

if not os.path.isdir(dir_path):
    print("%s must be a directory" % dir_path)
else:
    file = input("Please insert name of a file: ")
    dir_path = os.path.join(dir_path, file)

    if not os.path.exists(dir_path):
        print("The file doesn't exist")
    else:
        print("\nBelow, display of parameters of the file:")

        print("Last modify date is:", time.localtime(os.path.getatime(dir_path)))
        print("\nFile size is: ", os.path.getsize(dir_path))

        print('Current directory is: ', os.getcwd())
        print("\nThe absolute path is: ", os.path.abspath(dir_path))
