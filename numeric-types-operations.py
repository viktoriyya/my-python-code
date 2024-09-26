import math

a = 24 + 12
print(a)
b = 85 - 83
print(b)
c = 8 * 32
print(c)
d = 16 / 4
print(d)
e = 2 ** 10
print(e)
f = 30 % 7
print(f)

# complex numbers


complex_number = 3 + 2j
print(complex_number)

g = True * False
print(g)

#h = 37348 / 0 #devision by 0 
#print(h)

# type error

# task 2 
output = f"""
max(4, 3.5, 5) = {max(4, 3.5, 5)}
max(True, False, 0.9) = {max(True, False, 0.9)}
min(94, 27, 45.25) = {min(94, 27, 45.25)}
min(False, True, 1) = {min(False, True, 1)}
abs(-58.234) = {abs(-58.234)}
abs(3 + 4j) = {abs (3 + 4j)}
pow(3, 7) = {pow(3, 7)}
ceil(84 / 3) = {math.ceil(84 / 3)}
ceil(2.84) = {math.ceil(2.83)}
floor(78.9) = {math.floor(78.9)}
"""
print(output)

