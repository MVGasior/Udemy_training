f_smaller = 3.141592653589793
f_bigger  = 3.87756392764

import math

print(math.ceil(f_smaller),math.ceil(f_bigger))
print("\n")

print(math.floor(f_smaller),math.floor(f_bigger))
print("\n")

print(math.ceil(-f_smaller),math.ceil(-f_bigger))
print("\n")

print(math.floor(-f_smaller),math.floor(-f_bigger))
print("\n")

print(pow(2,8),pow(9,0,5))
print("\n")

print(math.sqrt(16))
print("\n")

print(math.pi, math.e)
print("\n")

print(math.sin(math.pi/2), math.cos(math.pi/4))
print("\n")

print("-----------------------------------------------------------")

from math import *

degree = 45

print(degree * pi/180)
print(radians(degree))

small_pizza_r  = 22
big_pizza_r    = 27
family_pizza_r = 38

small_pizza_price  = 11.5
big_pizza_price    = 15.6
family_pizza_price = 22.0

small_pizza_surface  = pow(small_pizza_r,2)*pi/10000
big_pizza_surface    = pow(big_pizza_r,2)*pi/10000
family_pizza_surface = pow(family_pizza_r,2)*pi/10000

print('small_pizza',small_pizza_surface)
print('bif_pizza',big_pizza_surface)
print('family_pizza',family_pizza_surface)

print('small pizza cost for meter ',small_pizza_price/small_pizza_surface)
print('big pizza cost for meter   ',big_pizza_price/big_pizza_surface)
print('family pizza cost for meter',family_pizza_price/family_pizza_surface)

math_ls = dir(math)
print(math_ls)
