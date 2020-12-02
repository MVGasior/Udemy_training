# This program is a 1# lesson of In_Ou Udemy
# Author: Mateusz Gąsior

# filename = input("Enter filename: ")

# print("The file name is: %s" % filename)


file_size = int(input("Enter the max file size (MB): "))

print("The max size is %d" % file_size)

print("Size in KB is %d" % (file_size * 1024))

print("-------------------------------------------------------")


def check_int(s):
    """
    This function checking if number is int
    :param s:number to check
    :return:True or False
    """
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


input_a = input("Please insert parameter a of quadratic equation: ")
input_b = input("Please insert parameter b of quadratic equation: ")
input_c = input("Please insert parameter c of quadratic equation: ")

if not check_int(input_a) or not check_int(input_b) or not check_int(input_c):

    print("The inserted values are not correct")
else:
    a = int(input_a)
    b = int(input_b)
    c = int(input_c)
    if a == 0:

        print("This is not a quadratic equation !!!")
    else:
        delta = b ** 2 - 4 * a * c

        if delta < 0:
            print("The is no solution of that quadratic equation.")
        elif delta == 0:
            x1 = (- b - delta ** 0.5) / (2 * a)
            print("The only one zero point is: ", x1)
        else:
            x1 = (- b - delta ** 0.5) / (2 * a)
            x2 = (- b + delta ** 0.5) / (2 * a)

            print("The zero points are: ", x1, x2)

