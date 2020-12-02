# This program is a 3# lesson of In_Ou Udemy
# Author: Mateusz Gąsior

import os

while True:

    file_name = input("Enter path to results file: ")

    if os.path.isfile(file_name):
        break
    else:
        print("File name is not correct, try again!")

print("The results file is %s" % file_name)

print("----------------------------------------------------")

import datetime

data_input_catalog = r'c:\temp\data_input'
data_output_catalog = r'c:\temp\data_output'

today = datetime.date.today()
today_output_catalog = os.path.join(data_output_catalog, today.strftime("%Y-%m-%d"))

is_input_catalog_ok = os.path.exists(data_output_catalog) and os.path.isdir(data_output_catalog)

is_today_output_catalog_ok = not os.path.exists(today_output_catalog)

if is_input_catalog_ok == True and is_today_output_catalog_ok == True:

    print("Conditions met! We can continue!")
else:
    print("We can't continue. There is a mistake!")

    if not os.path.exists(data_output_catalog):
        print("%s not existing" % data_output_catalog)
    elif not os.path.isdir(data_output_catalog):
        print("%s is not a direction" % data_output_catalog)
    else:
        print("%s is not existing" % today_output_catalog)