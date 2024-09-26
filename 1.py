import cmath

# Integer
print(123, "is type of", type(123))

# Float
print(43.23, "is type of", type(43.23))

# Complex
print(4 - 1j, "is type of", type(4 - 1j))

 # String
print("How are you?", "is type of", type("How are you?"))

# Boolean
print(True, "is type of", type(True))


print(isinstance(123, int))
print(isinstance(43.23, int))
print(isinstance(4 - 1j, complex))
print(isinstance("How are you?", str))
print(isinstance(True, str))

